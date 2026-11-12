# Auditoria bibliográfica — rodada 4

Data da consulta: 11 de novembro de 2026.

## Escopo

Conferência dos quatro identificadores questionados em `references.bib`, com atenção à edição e ao ano. Esta rodada não reavalia o conteúdo matemático nem modifica `main.tex`, `references.bib` ou o PDF da rodada 3. A associação entre DOI e obra é distinguida do teste técnico de redirecionamento pelo resolvedor doi.org.

## 1. Needham: o DOI da edição de 1997 está confirmado

A página oficial da Oxford Academic para *Visual Complex Analysis*, de Tristan Needham, apresenta os seguintes dados no mesmo registro:

- Publicação: 23 January 1997.
- DOI: `10.1093/oso/9780198534471.001.0001`.
- ISBN impresso: `9780198534471`.
- ISBN eletrônico: `9781383025378`.
- Editora: Oxford University Press.

Fonte primária consultada diretamente: https://academic.oup.com/book/52945

A edição comemorativa tem um registro distinto, com publicação em 28 February 2023, ISBN impresso `9780192868916`, ISBN eletrônico `9780191964947` e DOI `10.1093/oso/9780192868916.001.0001`.

Fonte primária para comparação: https://academic.oup.com/book/45765

**Decisão:** manter a referência de 1997 e seu DOI. A existência do identificador da edição de 2023 não invalida o identificador diferente registrado pela editora para 1997. Não se verificou a alegada incompatibilidade entre ano e DOI.

A data exata de 23 de janeiro é a informada na plataforma Oxford Academic; o manuscrito cita apenas 1997, sem dia ou mês, de modo que diferenças de datas comerciais entre catálogos não alteram a referência.

## 2. Mason–Handscomb: 2003 confirmado no próprio livro

Foi consultada a amostra editorial em PDF de *Chebyshev Polynomials*, de J. C. Mason e D. C. Handscomb. A folha de rosto identifica Chapman & Hall/CRC. Seu verso apresenta copyright de 2003 em nome dos autores e ISBN impresso `0-8493-0355-9`. A verificação foi feita também pela imagem da página: quinta página do PDF, índice zero 4.

Fonte primária, amostra editorial hospedada em PagePlace:
https://api.pageplace.de/preview/DT0400.9781420036114_A25126189/preview-9781420036114_A25126189.pdf

A página comercial da Routledge encontrada na busca usa 2002. Isso confirma a existência da divergência entre o registro comercial e o ano de copyright do volume, sem justificar substituir silenciosamente a data bibliográfica usada no manuscrito.

Página comercial:
https://www.routledge.com/Chebyshev-Polynomials/Handscomb-Mason/p/book/9780429191381

**Decisão:** manter 2003. Esta conclusão se apoia no verso da folha de rosto da amostra consultada nesta rodada; não se afirma ter identificado o exemplar pessoal usado pelo autor. O DOI `10.1201/9781420036114` permanece inalterado. A abertura direta da plataforma Taylor & Francis foi bloqueada por HTTP 403; esta rodada não certifica seu redirecionamento de ponta a ponta.

## 3. Barbeau: associação corroborada, resolução direta não concluída

O DOI em discussão é `10.1007/978-1-4612-4524-7`.

A página oficial da Springer confirma Edward J. Barbeau, *Polynomials*, a série *Problem Books in Mathematics* e copyright de 1989. O registro acessível informa a brochura ISBN `978-0-387-40627-5`, publicada em 9 de outubro de 2003, mas não exibe o DOI do livro eletrônico.

Fonte primária consultada diretamente:
https://link.springer.com/book/9780387406275

A referência 3 do artigo “105.04 Polynomials with no real zeros”, em Cambridge Core, associa explicitamente a obra de 1989 ao DOI `10.1007/978-1-4612-4524-7`. Esse trecho foi recuperado pelo índice de busca; a abertura direta da página do artigo retornou HTTP 429.

Fonte de corroboração indireta:
https://www.cambridge.org/core/journals/mathematical-gazette/article/abs/10504-polynomials-with-no-real-zeros/EF820828887AD53825571642B9BE2AE0

Foram tentados o resolvedor doi.org, dx.doi.org, a página Springer pelo DOI e os registros Crossref. Essas tentativas não produziram uma resposta utilizável na ferramenta de navegação. No ambiente de execução, o cliente HTTP falhou na resolução DNS de doi.org e api.crossref.org, antes de receber resposta HTTP desses servidores.

**Decisão:** não substituir nem declarar inválido o DOI com base em falhas de acesso. O identificador permanece no arquivo original, mas a verificação direta continua pendente. A corroboração por citação publicada não deve ser descrita como um teste bem-sucedido de resolução do DOI.

## 4. Hardy–Wright: DOI e sexta edição confirmados

A página oficial da Oxford Academic apresenta, no mesmo registro, *An Introduction To The Theory Of Numbers*, G. H. Hardy e E. M. Wright, publicação em 31 July 2008 e DOI `10.1093/oso/9780199219858.001.0001`. O ISBN impresso é `9780199219858` e o eletrônico é `9781383035957`. A descrição identifica expressamente a sexta edição.

Fonte primária consultada diretamente:
https://academic.oup.com/book/54489

**Decisão:** manter ano, edição e DOI. A correspondência bibliográfica está confirmada diretamente pela editora, embora o acesso pelo resolvedor doi.org não tenha sido concluído.

## Conclusão e limite de verificação

A hipótese de erro na referência de Needham não foi confirmada: a Oxford registra o DOI indicado para 1997. O DOI de Hardy–Wright está associado à sexta edição de 2008 no registro da editora. O ano 2003 de Mason–Handscomb tem apoio no próprio verso da folha de rosto. Para Barbeau, a associação do DOI à obra está corroborada indiretamente, mas a abertura direta solicitada continua sem confirmação.

Não foi feita alteração bibliográfica sem evidência de erro. Não foi produzido um novo PDF nem realizada nova compilação, porque os fontes permanecem idênticos aos da rodada 3.

## Integridade dos arquivos preservados

- `main.tex`: SHA-256 `b3326fced4a6f1ca2d1dec6e99756eb21128fbd15c66c5dfd50269e36bb347a9`. Idêntico ao arquivo no pacote da rodada 3: sim.
- `references.bib`: SHA-256 `0f22df15d983c729cd328d25bc603a0666fa7bd60bf3393b2d7dcad0f4f94922`. Idêntico ao arquivo no pacote da rodada 3: sim.
