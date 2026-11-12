# Euler–Liouville theorem: short note

This directory contains a self-contained English translation and conservative editorial revision of the original Portuguese geometric derivation, expanded with three worked mathematical examples.

- `main.tex`: the **only active LaTeX source**, including the geometric argument and worked examples.
- `main.pdf`: compiled English note (4 A4 pages).
- `original/`: the three archived historical source files, unchanged.

## Worked examples

1. Compensating expansion and contraction: diagonal flow and rectangle area.
2. Rotation and area preservation: skew-symmetric generator and rotation matrix.
3. Time-dependent trace-free deformation: nonautonomous transition matrix `Phi(t,tau)`.

The examples compare explicitly computed determinants with Liouville's volume formula. No physics applications are included.

## Build

```bash
latexmk -pdf -halt-on-error -interaction=nonstopmode main.tex
```

The original transported-region derivation is preserved, with clarified matrix normalization, Jacobian signs, and terminology.
