# From Abel's Identity to Liouville's Formula (version 10)

The full Python source for Figures 3, 4 and 5 is reproduced verbatim in Appendix A of the LaTeX article. The executable script is also included as `liouville_examples.py`.

## Contents

- `liouville_formula_paper.tex` — complete article and embedded Python appendix
- `liouville_formula_paper.pdf` — compiled article (39 A4 pages)
- `liouville_examples.py` — source script reproduced in Appendix A
- `figures_volume_factors.png` — computed volume factors
- `figures_oscillator_phase_space.png` — damped oscillator trajectories
- `figures_oscillator_area.png` — transported polygon and area-ratio consistency check

## Reproduce the figures

Install dependencies: `python -m pip install numpy scipy matplotlib`

Run: `python liouville_examples.py`

The three PNG files are saved beside the Python script. The article can be compiled with `latexmk -pdf liouville_formula_paper.tex` using a standard TeX installation with the `listings` package.
