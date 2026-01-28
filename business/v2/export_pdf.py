#!/opt/homebrew/bin/python3.14
"""
Professional PDF Export Script for MILO Business Documentation
Creates CEO-ready PDF with clickable Table of Contents
"""

import re
import markdown
from weasyprint import HTML, CSS

# Professional CSS styling for executive documents
CSS_STYLE = """
@page {
    size: A4;
    margin: 2.5cm 2cm 2.5cm 2cm;
    @top-center {
        content: "MILO - Business Executive Summary v2.0";
        font-size: 9pt;
        color: #666;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    @bottom-center {
        content: counter(page);
        font-size: 9pt;
        color: #666;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    @bottom-right {
        content: "DeepmAInd B.V. | Confidential";
        font-size: 8pt;
        color: #999;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
}

@page :first {
    @top-center { content: none; }
    @bottom-center { content: none; }
    @bottom-right { content: none; }
}

* {
    box-sizing: border-box;
}

body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.6;
    color: #1a1a1a;
    max-width: 100%;
}

/* Cover page */
.cover {
    text-align: center;
    page-break-after: always;
    padding-top: 80pt;
}

.cover h1 {
    font-size: 42pt;
    color: #0d1b2a;
    margin-bottom: 8pt;
}

.cover h2 {
    font-size: 20pt;
    color: #415a77;
    border-bottom: none;
    margin-top: 0;
    margin-bottom: 16pt;
}

.cover h3 {
    font-size: 14pt;
    color: #778da9;
    font-weight: 400;
    font-style: italic;
    margin-top: 0;
    margin-bottom: 40pt;
}

.cover .meta {
    margin-top: 60pt;
    font-size: 11pt;
    color: #4a5568;
    line-height: 2;
}

.cover .badges {
    margin-top: 40pt;
}

/* Headers */
h1 {
    font-size: 28pt;
    font-weight: 700;
    color: #0d1b2a;
    margin-top: 0;
    margin-bottom: 12pt;
    text-align: center;
    border-bottom: none;
}

h2 {
    font-size: 18pt;
    font-weight: 600;
    color: #1b263b;
    margin-top: 30pt;
    margin-bottom: 12pt;
    padding-bottom: 6pt;
    border-bottom: 2px solid #415a77;
    page-break-after: avoid;
}

h3 {
    font-size: 14pt;
    font-weight: 600;
    color: #415a77;
    margin-top: 20pt;
    margin-bottom: 10pt;
    page-break-after: avoid;
}

h4 {
    font-size: 12pt;
    font-weight: 600;
    color: #778da9;
    margin-top: 16pt;
    margin-bottom: 8pt;
}

/* Paragraphs */
p {
    margin-bottom: 10pt;
    text-align: justify;
}

/* Links */
a {
    color: #1b4965;
    text-decoration: none;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 16pt 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}

th {
    background-color: #1b263b;
    color: white;
    padding: 10pt 8pt;
    text-align: left;
    font-weight: 600;
    font-size: 9pt;
}

td {
    padding: 8pt;
    border-bottom: 1px solid #e5e5e5;
    vertical-align: top;
}

tr:nth-child(even) {
    background-color: #f8f9fa;
}

/* Code blocks */
pre {
    background-color: #f8f9fa;
    border: 1px solid #ddd;
    border-radius: 6px;
    padding: 14pt;
    font-family: 'Menlo', 'Monaco', 'Consolas', monospace;
    font-size: 7.5pt;
    line-height: 1.3;
    overflow-x: auto;
    white-space: pre;
    page-break-inside: avoid;
    margin: 14pt 0;
}

code {
    font-family: 'Menlo', 'Monaco', 'Consolas', monospace;
    font-size: 9pt;
    background-color: #f0f0f0;
    padding: 2pt 4pt;
    border-radius: 3px;
}

/* Blockquotes */
blockquote {
    border-left: 4px solid #415a77;
    margin: 16pt 0;
    padding: 12pt 16pt;
    background-color: #f8f9fa;
    font-style: italic;
    color: #4a5568;
}

blockquote p {
    margin: 0;
}

/* Lists */
ul, ol {
    margin: 10pt 0;
    padding-left: 24pt;
}

li {
    margin-bottom: 6pt;
}

/* Horizontal rules */
hr {
    border: none;
    border-top: 1px solid #e5e5e5;
    margin: 24pt 0;
}

/* Center aligned content */
.center {
    text-align: center;
}

/* Status badges */
.badge {
    display: inline-block;
    padding: 4pt 12pt;
    margin: 3pt 4pt;
    border-radius: 12pt;
    font-size: 9pt;
    font-weight: 600;
    color: white;
}

.badge-blue { background-color: #3182ce; }
.badge-green { background-color: #38a169; }
.badge-orange { background-color: #dd6b20; }
.badge-red { background-color: #e53e3e; }

/* Emphasis */
strong {
    font-weight: 700;
    color: #1b263b;
}

em {
    font-style: italic;
    color: #4a5568;
}
"""


def preprocess_markdown(content):
    """Pre-process markdown to handle special cases"""

    # Create a proper cover page by extracting the header section
    # Find the first centered div section (cover page)
    cover_match = re.search(
        r'<div align="center">\s*\n\s*# \*\*(.+?)\*\*\s*\n\s*## (.+?)\s*\n\s*### \*(.+?)\*\s*\n\s*---\s*\n(.*?)</div>',
        content, re.DOTALL
    )

    if cover_match:
        title = cover_match.group(1)
        subtitle = cover_match.group(2)
        tagline = cover_match.group(3)
        meta_content = cover_match.group(4)

        # Parse meta content
        meta_lines = []
        for line in meta_content.strip().split('\n'):
            line = line.strip()
            if line and not line.startswith('!') and not line.startswith('---'):
                # Convert **text:** format to clean HTML
                line = re.sub(r'\*\*(.+?):\*\*\s*(.+)', r'<strong>\1:</strong> \2', line)
                line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
                if line:
                    meta_lines.append(line)

        # Build cover page HTML
        cover_html = f'''<div class="cover">
<h1>{title}</h1>
<h2>{subtitle}</h2>
<h3>{tagline}</h3>
<div class="meta">
{'<br>'.join(meta_lines)}
</div>
<div class="badges">
<span class="badge badge-blue">Status: Pre-Launch</span>
<span class="badge badge-green">Funding: Seed Round</span>
<span class="badge badge-orange">Stage: MVP Complete</span>
<span class="badge badge-red">Projections: Conservative</span>
</div>
</div>
'''
        # Replace the original cover section
        content = re.sub(
            r'<div align="center">\s*\n\s*# \*\*(.+?)\*\*\s*\n\s*## (.+?)\s*\n\s*### \*(.+?)\*\s*\n\s*---\s*\n(.*?)</div>\s*\n*---',
            cover_html,
            content, flags=re.DOTALL, count=1
        )

    # Remove any remaining shield.io badges
    content = re.sub(r'!\[.*?\]\(https://img\.shields\.io/.*?\)\s*', '', content)

    # Convert remaining <div align="center"> sections with ## headers
    def convert_centered_header(match):
        header_text = match.group(1)
        # Remove ** markers
        header_text = header_text.replace('**', '')
        return f'<h2 style="text-align: center; border-bottom: none;">{header_text}</h2>'

    content = re.sub(
        r'<div align="center">\s*\n\s*## (.+?)\s*\n\s*</div>',
        convert_centered_header,
        content
    )

    # Handle any other centered divs
    content = re.sub(r'<div align="center">', '<div class="center">', content)

    return content


def convert_md_to_pdf(md_file, pdf_file):
    """Convert markdown file to professional PDF"""

    # Read markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Pre-process the markdown
    md_content = preprocess_markdown(md_content)

    # Configure markdown extensions
    md = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'toc',
        'attr_list',
        'md_in_html',
        'sane_lists'
    ])

    # Convert to HTML
    html_content = md.convert(md_content)

    # Wrap in complete HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MILO - Business Executive Summary v2.0</title>
</head>
<body>
{html_content}
</body>
</html>"""

    # Generate PDF
    html = HTML(string=full_html)
    css = CSS(string=CSS_STYLE)

    html.write_pdf(pdf_file, stylesheets=[css])

    print(f"✅ PDF exported successfully: {pdf_file}")
    return pdf_file


if __name__ == "__main__":
    md_file = "/Users/gillesmoenaert/Documents/projects/DeepmAInd/business/v2/business-executive-summary/business-executive-summary.md"
    pdf_file = "/Users/gillesmoenaert/Documents/projects/DeepmAInd/business/v2/business-executive-summary/MILO_Business_Executive_Summary_v2.pdf"

    convert_md_to_pdf(md_file, pdf_file)
