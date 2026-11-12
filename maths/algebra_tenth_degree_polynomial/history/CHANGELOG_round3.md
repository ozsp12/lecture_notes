# Revision round 3 — 11 November 2026

## Editorial changes

1. In the opening paragraph of Section 4.4, replaced “and then recover the quadratic relations commonly called Girard's relations” with “and then recover the quadratic case”. The qualified reference to Girard following Equation (4.18) remains unchanged.
2. Renamed Section 4 from “Applications” to “Solution of the motivating equation”. The running heads and PDF bookmark inherit the new title. Retained the existing internal label `sec:applications` to avoid unnecessary cross-reference changes.
3. In the abstract, replaced “a tenth-degree polynomial equation with missing coefficients” with “a tenth-degree polynomial equation with vanishing coefficients at $x^3$ and $x^7$”.

## Bibliographic verification

Reviewed the four requested DOI identifiers against the sources detailed in `DOI_VERIFICATION_round3.md`. No identifier was changed. Metadata correspondence and successful HTTP resolution are distinguished explicitly: direct DOI resolution could not be certified in this environment. The prior bibliography file remains byte-for-byte unchanged.

## Validation

Compiled with pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX. The final PDF has 29 A4 pages. The final LaTeX log contains no warnings, undefined references, multiply defined labels, overfull boxes, or underfull boxes. BibTeX completed without warnings.

A source comparison confirms that all 71 displayed-mathematics environment blocks, every label, every cross-reference and every citation command are unchanged. This is an integrity check, not a new independent proof review. The source diff contains exactly the three editorial replacements listed above.

Rendered all 29 pages. Inspected page contact sheets and the affected section-title page at larger scale. No clipping or overlap was observed. The four DOI link targets in the PDF match the bibliography.

## Package

The package includes `main.tex`, `references.bib`, the generated `main.bbl`, `main.pdf`, this change log, the DOI verification report, and a README with build instructions. No external figure files are needed; the drawings are implemented in TikZ in `main.tex`.
