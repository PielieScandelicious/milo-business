# Adding the KBC Logo to the Business Report

The front page currently has a placeholder for the Start it @KBC logo.

## To Add the Official KBC Logo:

1. **Download the KBC logo:**
   - Visit [KBC Belgium's press/media page](https://www.kbc.com/en/press-room.html)
   - Or contact Start it @KBC for their official logo file
   - Accepted formats: PNG, JPG, or PDF

2. **Save the logo file:**
   - Place it in: `milo-business/business/v3/images/`
   - Name it: `kbc-logo.png` (or `.jpg`, `.pdf`)

3. **Update the LaTeX file:**
   - Open `milo-business-report-v3.tex`
   - Find line ~181 (search for "KBC Logo")
   - **Uncomment** this line:
     ```latex
     \includegraphics[height=2cm]{images/kbc-logo.png}
     ```
   - **Comment out or delete** the placeholder box (lines 183-189)

4. **Recompile the PDF:**
   ```bash
   cd milo-business/business/v3
   pdflatex milo-business-report-v3.tex
   pdflatex milo-business-report-v3.tex
   ```

## Current Setup:

The document now includes:
- ✅ "Start it @KBC Belgium" placeholder box at the top
- ✅ "Prepared for" text
- ✅ "Application for Start it @KBC Belgium" in the footer
- ✅ Tone and content aligned with KBC selection criteria

The placeholder will work fine if you don't have access to the official logo file.
