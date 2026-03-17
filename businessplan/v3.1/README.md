# Milo Business Plan — Version 3.1 (March 2026)

## What's New in V3.1

- **NEW Section 3**: "Market Validation: The Algori Case Study" — detailed analysis of Algori/PROMOS as proof the receipt panel model works in Europe
- **Expanded Section 9**: "Milo vs PROMOS: B2C App Comparison" — 12-row comparison table + five structural advantages
- **Algori added to Comparable Companies** table
- **Sources [23]-[29]** added covering Algori funding, PROMOS app testing, Trustpilot reviews
- All sections renumbered (16 total sections, up from 15)

## Compilation

Requires XeLaTeX with TeX Gyre Heros font:

```bash
sudo apt-get install texlive-xetex texlive-latex-extra texlive-fonts-extra texlive-science texlive-pictures fonts-texgyre
cd businessplan/v3.1/latex/
xelatex -interaction=nonstopmode milo-business-plan-v3.1.tex
xelatex -interaction=nonstopmode milo-business-plan-v3.1.tex  # Run twice for TOC
```

## Files

- `latex/milo-business-plan-v3.1.tex` — LaTeX source (1,841 lines)
- `latex/milo-logo.png` — Logo file (place your real logo here)
- `research/algori-promos-competitive-analysis.md` — Research notes on Algori/PROMOS
