# Prompt 10 - Ingestao Automatizada de Regras de Imigracao (Data Engineering)

## Copie e envie este prompt para a IA
Voce e um Data Engineer Senior. Implemente pipeline de coleta e normalizacao de regras de imigracao para alimentar o backend sem hardcode.
Integre com o backend FastAPI usando PostgreSQL no Supabase (via SQLAlchemy/Alembic) e jobs Celery.

### Objetivo
Construir pipeline confiavel para coletar, versionar e publicar regras oficiais por pais/programa com trilha de auditoria.

### Arquitetura de dados obrigatoria
- Bronze: documento bruto (HTML/PDF/JSON) em Supabase Storage + metadados + hash
- Silver: texto limpo e segmentado por secao/artigo
- Gold: regras normalizadas em tabelas PostgreSQL do Supabase (`ProgramVersion`, `RuleCondition`, `RuleOutcome`)

### Componentes obrigatorios
1. `SourceRegistry` (cadastro de fontes)
2. `Crawler/Fetcher` com suporte a:
   - HTML estatico
   - PDF
   - API publica
3. `Extractor` (parser deterministico primeiro, LLM apenas fallback)
4. `Validator` (schema com Pydantic)
5. `Publisher` (grava nova `ProgramVersion` sem sobrescrever historico)
6. `Diff Engine` (detecta mudancas por hash + diff semantico)
7. `SupabaseDataGateway` para persistencia e leitura (pool de conexao, retries e transacao)

### Politicas obrigatorias
- Respeitar `robots.txt` e termos de uso.
- Agendamento com Celery Beat.
- Retry com backoff e quarentena para fontes problematicas.
- Nao publicar automaticamente quando confianca < threshold.
- Exigir `manual_review_required=true` para casos ambiguos.
- Usar chave `service_role` apenas no backend/workers (nunca no frontend).
- Aplicar RLS nas tabelas expostas ao app e isolar tabelas internas de ingestao.

### Fontes publicas iniciais (MVP)
Use estas fontes oficiais como `seed` no `SourceRegistry`:

1. Estados Unidos
- USCIS: https://www.uscis.gov/
- US Visas (Dept. of State): https://travel.state.gov/content/travel/en/us-visas.html

2. Portugal
- AIMA: https://aima.gov.pt/

3. Paraguai
- Direccion General de Migraciones: https://www.migraciones.gov.py/

4. Reino Unido
- GOV.UK Visas and Immigration: https://www.gov.uk/browse/visas-immigration

5. Japao
- MOFA Visa: https://www.mofa.go.jp/j_info/visit/visa/index.html
- Immigration Services Agency (referencia institucional): https://www.isa.go.jp/en/

6. Alemanha
- Make it in Germany: https://www.make-it-in-germany.com/en/
- BAMF: https://www.bamf.de/EN/

7. Espanha
- Ministerio de Inclusion, Seguridad Social y Migraciones: https://www.inclusion.gob.es/en/

8. Italia
- Ministero degli Affari Esteri (visti/ingresso): https://www.esteri.it/en/servizi-consolari-e-visti/ingressosoggiornoinitalia/

9. Canada
- IRCC: https://www.canada.ca/en/services/immigration-citizenship.html

10. Argentina
- Direccion Nacional de Migraciones: https://www.argentina.gob.ar/interior/migraciones

11. Franca
- France-Visas: https://france-visas.gouv.fr/

12. Irlanda
- Immigration Service Delivery: https://www.irishimmigration.ie/

13. Paises Baixos
- IND: https://ind.nl/en

14. Suica
- SEM: https://www.sem.admin.ch/sem/en/home/themen/einreise.html

15. Belgica
- Immigration Office (DOFI): https://dofi.ibz.be/en

### Entregaveis obrigatorios
- Jobs de ingestao por fonte/pais.
- Tabela de execucao de pipeline (`ingestion_run`, `ingestion_run_item`).
- Estrategia de versionamento de regra ativando novas versoes sem apagar antigas.
- CLI/endpoint interno protegido para reprocessar uma fonte especifica.
- Testes de parser para ao menos 5 fontes na primeira entrega.
- Migracoes Alembic compativeis com Supabase (sem perder historico).

### Criterios de aceite
- Pipeline executa ponta a ponta em ambiente local com Supabase (local ou cloud).
- Mudanca na fonte gera nova versao de regra (quando aplicavel).
- Auditoria responde: origem, quando coletado, parser usado, confianca, diff.
