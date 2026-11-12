# Verificação dos quatro DOI — 11 de novembro de 2026

## Escopo e resultado

Foram conferidos os quatro identificadores já presentes em `references.bib`, a sua associação às obras e os endereços efetivamente incorporados ao PDF. Não foi identificado erro de transcrição nos identificadores. A bibliografia foi mantida sem alterações.

Esta verificação distingue correspondência bibliográfica de resolução HTTP: as tentativas de abrir diretamente os quatro endereços `https://doi.org/...` retornaram erro de acesso na ferramenta de navegação. A tentativa adicional por cliente HTTP no ambiente de execução falhou por indisponibilidade de resolução DNS, antes de obter resposta do servidor. Portanto, **não foi possível certificar nesta sessão o redirecionamento HTTP de ponta a ponta de nenhum dos quatro endereços**. Isso não demonstra que os DOI estejam quebrados.

## Evidências por obra

### Edward J. Barbeau — *Polynomials* (1989)

DOI mantido: `10.1007/978-1-4612-4524-7`.

A página oficial da Springer confirma título, autor e copyright de 1989, mas a página acessível da edição impressa não exibe o DOI. O identificador exato está associado à obra na referência 3 do artigo “105.04 Polynomials with no real zeros”, publicado em *The Mathematical Gazette*, conforme o registro indexado de Cambridge Core. O acesso direto ao artigo retornou HTTP 429 nesta sessão. A associação é corroborada bibliograficamente; a resolução direta do DOI permanece não verificada.

Fontes:
- Springer: https://link.springer.com/book/9780387406275
- Cambridge Core: https://www.cambridge.org/core/journals/mathematical-gazette/article/abs/10504-polynomials-with-no-real-zeros/EF820828887AD53825571642B9BE2AE0

### Tristan Needham — *Visual Complex Analysis* (1997)

DOI mantido: `10.1093/oso/9780198534471.001.0001`.

A página oficial da Oxford Academic foi aberta e apresenta o mesmo título, autor, ano e DOI. Correspondência bibliográfica confirmada diretamente na editora; redirecionamento via `doi.org` não verificado.

Fonte: https://academic.oup.com/book/52945

### G. H. Hardy e E. M. Wright — *An Introduction to the Theory of Numbers*, 6.ª edição (2008)

DOI mantido: `10.1093/oso/9780199219858.001.0001`.

A página oficial da Oxford Academic foi aberta e apresenta o mesmo título, autores, ano e DOI; sua descrição identifica a sexta edição. Correspondência bibliográfica confirmada diretamente na editora; redirecionamento via `doi.org` não verificado.

Fonte: https://academic.oup.com/book/54489

### J. C. Mason e D. C. Handscomb — *Chebyshev Polynomials*

DOI mantido: `10.1201/9781420036114`.

O registro bibliográfico CiNii Research do National Institute of Informatics foi aberto. Ele identifica explicitamente Crossref como fonte e apresenta título, autores, editora e o mesmo DOI. A referência publicada no *Ukrains’kyi Matematychnyi Zhurnal* também associa o identificador à obra. Os acessos diretos à plataforma Taylor & Francis foram impedidos por erro de acesso/HTTP 403; redirecionamento via `doi.org` não verificado.

A referência de 2003 utilizada no manuscrito foi preservada: o DLMF também cita a obra nesse ano. O registro eletrônico Crossref reproduzido pelo CiNii informa 17 de setembro de 2002. Não se substituiu silenciosamente o ano da edição citada pelo ano do registro eletrônico.

Fontes:
- CiNii/Crossref: https://cir.nii.ac.jp/crid/1361981469824489216
- Artigo com a referência: https://umj.imath.kiev.ua/index.php/umj/article/view/2380
- DLMF, bibliografia M, entrada Mason–Handscomb: https://dlmf.nist.gov/bib/M

## Integridade dos arquivos

Os quatro endereços DOI nos links do PDF recompilado coincidem com os de `references.bib`. O arquivo BibTeX é idêntico, byte a byte, ao da rodada anterior. Nenhum DOI foi removido ou substituído sem evidência.

Conclusão: correspondência bibliográfica conferida, com os níveis de evidência descritos acima; teste de redirecionamento HTTP de ponta a ponta não concluído devido às limitações de acesso desta sessão.
