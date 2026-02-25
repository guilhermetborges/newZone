# Prompt 13 - Seed Inicial dos 15 Paises + Programas + Fontes

## Copie e envie este prompt para a IA
Voce e um Data/Backend Engineer. Crie seed inicial para o MVP com 15 paises prioritarios e estrutura de fontes oficiais.
Implemente no backend FastAPI com PostgreSQL no Supabase (SQLAlchemy + Alembic + CLI de aplicacao).

### Objetivo
Popular o sistema com dados base para comecar testes reais de score e ingestao.
Garantir seed idempotente e segura para ambientes Supabase (local/staging/producao).

### Paises alvo (MVP)
Use estes 15 paises como seed inicial (estimativas MRE 2023):
1. Estados Unidos (2.085.000)
2. Portugal (513.000)
3. Paraguai (263.200)
4. Reino Unido (230.000)
5. Japao (210.471)
6. Alemanha (170.400)
7. Espanha (161.944)
8. Italia (159.000)
9. Canada (143.500)
10. Argentina (101.502)
11. Franca (95.000)
12. Irlanda (80.000)
13. Paises Baixos (80.000)
14. Suica (64.000)
15. Belgica (50.000)

### Referencia de priorizacao
- Relatorio oficial do MRE (Estatisticas 2023):
  - https://www.gov.br/mre/pt-br/assuntos/portal-consular/comunidade-brasileira-no-exterior-estatisticas-2023
  - https://www.gov.br/mre/pt-br/assuntos/portal-consular/BrasileirosnoExterior2023.pdf

Observacao:
- Se quiser incluir territorio nao soberano na priorizacao, Guiana Francesa (Franca) tem 92.493 e pode substituir a Belgica no top 15.

### Seed minimo por pais
Para cada pais, criar:
- `Country`
- 1 a 3 `ImmigrationProgram` iniciais (exemplos: trabalho qualificado, estudante, residencia)
- `SourceDocument` e `SourceRegistry` apontando para paginas oficiais
- `ProgramVersion` inicial em estado `draft`
- Relacoes e constraints para permitir upsert sem duplicidade

### Fontes oficiais para seed
- EUA: USCIS + US Visas
- Portugal: AIMA
- Paraguai: Migraciones
- Reino Unido: GOV.UK visas
- Japao: MOFA visa + ISA
- Alemanha: Make it in Germany + BAMF
- Espanha: Ministerio de Inclusion/Migraciones
- Italia: Esteri (visti/ingresso)
- Canada: IRCC
- Argentina: DNM
- Franca: France-Visas
- Irlanda: ISD
- Paises Baixos: IND
- Suica: SEM
- Belgica: DOFI

### Entregaveis obrigatorios
1. Arquivo de seed idempotente.
2. Comando unico para popular dados (ex: `python -m app.cli seed-mvp` ou equivalente).
3. Fixtures de exemplos de regra para pelo menos 5 paises.
4. Documento `docs/mvp-country-catalog.md` com:
   - pais
   - programas
   - fonte oficial
   - status da cobertura de regra
5. Script/check opcional para validar contagem final no Supabase apos seed.

### Criterios de aceite
- Ambiente local (Supabase) sobe com seed carregado.
- API `/countries` e `/countries/{code}/programs` retornam catalogo util.
- Dados de fontes oficiais ficam rastreaveis para ingestao futura.
- Reexecucao do seed nao duplica registros (idempotencia comprovada).
