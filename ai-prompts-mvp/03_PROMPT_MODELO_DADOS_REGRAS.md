# Prompt 03 - Modelagem de Dados para Regras de Imigracao (Sem Hardcode)

## Copie e envie este prompt para a IA
Voce e um Data Architect + FastAPI Engineer. Modele o banco para suportar regras de imigracao dinamicas e versionadas no tempo.

### Objetivo
Criar modelos e migracoes que permitam alterar regras sem deploy de codigo.

### Entidades obrigatorias
- `Country`
- `ImmigrationProgram`
- `ProgramVersion`
- `RuleGroup`
- `RuleCondition`
- `RuleOutcome`
- `SourceDocument`
- `SourceExtraction`
- `UserProfileSnapshot`
- `Assessment`
- `AssessmentResult`
- `AssessmentResultItem`
- `Roadmap`
- `RoadmapStep`
- `Plan`, `Subscription`, `Entitlement`

### Regras de modelagem obrigatorias
1. Toda regra deve estar ligada a `ProgramVersion`.
2. `ProgramVersion` precisa de:
   - `version`
   - `effective_from`
   - `effective_to` (nullable)
   - `status` (`draft`, `active`, `archived`)
3. `RuleCondition` com operador generico:
   - `operator` (`eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `between`, `in`, `not_in`, `exists`)
   - `value_json` (JSONB)
4. `RuleOutcome` precisa suportar:
   - pontuacao positiva/negativa
   - bloqueio (`is_blocking`)
   - mensagem explicavel
5. `UserProfileSnapshot` imutavel (nao atualizar, so criar novo).
6. `AssessmentResult` deve guardar hash da versao de regras aplicada para auditoria.

### Entregaveis obrigatorios
- Models SQLAlchemy + revisoes Alembic + schemas Pydantic.
- Indices no Postgres para consultas criticas.
- Constraints de integridade para evitar versoes ativas sobrepostas no mesmo programa.
- Documentacao ERD em markdown.

### Criterios de aceite
- Banco representa regras sem if/else hardcoded.
- Possivel ativar nova versao de programa sem quebra de historico.
- Query de auditoria responde: "qual regra gerou este score?".
