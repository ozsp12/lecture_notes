# A Tenth-Degree Polynomial Equation

**Roots of Unity, Cyclotomic Factorization, and Root Multiplicities of Products of Geometric Sums**

Osvaldo L. Santos-Pereira  
Physics Institute, Universidade Federal do Rio de Janeiro (UFRJ)

Teaching note on polynomial factorization, roots of unity, cyclotomic polynomials, root multiplicities, Vieta's formulas, reciprocal reduction through Dickson polynomials, and products of finite geometric sums.

## Files

- [main.pdf](main.pdf): compiled teaching note.
- [main.tex](main.tex): self-contained LaTeX source; all figures are defined in TikZ.
- [references.bib](references.bib): BibTeX bibliography.
- [main.bbl](main.bbl): bibliography supplied with the revised source package.
- [history/](history/): editorial change logs and bibliographic verification reports.

The source corresponds to the 28-page `layout_v2` version revised on 11 November 2026, including the compact first-page glossary, author identifiers below the name, centered page numbers, and the pagination adjustments to Equations (5.6) and (5.13). The manuscript and bibliography are imported without textual modifications.

## Compilation

Run in this directory with a LaTeX distribution containing pdfLaTeX, BibTeX, Latin Modern, TikZ, and the packages declared in `main.tex`:

```sh
latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex
```

Alternatively:

```sh
pdflatex -halt-on-error main.tex
bibtex main
pdflatex -halt-on-error main.tex
pdflatex -halt-on-error main.tex
```

No external figure files or custom fonts are required. The `.bbl` is intentionally tracked to accompany the preprint source. The reports in `history/` preserve the status and limitations recorded in each editorial round; their bibliographic checks are not new checks performed for this repository import.
