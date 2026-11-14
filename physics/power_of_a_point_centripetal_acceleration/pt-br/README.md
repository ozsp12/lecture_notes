# Potência de um Ponto e Aceleração Centrípeta — PT-BR

Projeto LaTeX completo, em português brasileiro, com PDF compilado.

## Conteúdo

- `main.tex`: manuscrito integral, classe nativa `article` (A4, 12 pt).
- `centripetal.bib`: referências bibliográficas em BibTeX.
- `centripetal_fig1.png`, `steinerpop.png`, `steinerpop2.png`: figuras originais.
- `main.pdf`: versão compilada e verificada (19 páginas).

## Compilação

```
lualatex main.tex
bibtex main
lualatex main.tex
lualatex main.tex
```

## Ajustes editoriais desta versão

O glossário foi mantido integralmente na página 2, com maior espaçamento vertical entre as 16 entradas, próximo ao limite inferior da área útil da página. A quebra forçada de página entre as referências bibliográficas e o apêndice foi removida, permitindo que o apêndice comece na própria página 16. A primeira figura do apêndice foi posicionada antes da proposição correspondente, sem alterar seu conteúdo. Foram mantidos os rulers, as notas de ORCID/e-mail e as margens da última revisão.
