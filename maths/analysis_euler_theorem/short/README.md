# Euler–Liouville theorem: short note

This directory contains a short, self-contained English translation and conservative editorial revision of the original Portuguese geometric derivation.

- `main.tex`: the **only active LaTeX source**. It does not depend on external `.tex` files.
- `main.pdf`: compiled English short note (2 A4 pages).
- `original/`: the three archived historical source files, kept unchanged for provenance.

## Build

```bash
latexmk -pdf -halt-on-error -interaction=nonstopmode main.tex
```

The original formulation is retained, including the transported-region integral, while mathematical corrections clarify the initial-time normalization, the absolute Jacobian determinant, and the Jacobi/Liouville terminology.
