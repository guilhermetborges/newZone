# Prompt 12 - Testes, CI/CD e Release do MVP

## Copie e envie este prompt para a IA
Voce e um Engenheiro de Plataforma. Estruture o ciclo de qualidade e deploy para o MVP.

### Objetivo
Garantir entrega continua com confianca em regressao minima.

### Testes obrigatorios
- Backend
  - unitarios (engine de score)
  - integracao (API + PostgreSQL no Supabase)
  - contrato (OpenAPI)
  - tasks Celery
- Frontend
  - unitarios de componentes criticos
  - E2E dos fluxos:
    - onboarding -> score
    - upgrade -> roadmap

### CI obrigatorio
- Lint + format check
- Testes backend
- Testes frontend
- Build de imagens Docker
- Bloquear merge se pipeline falhar
- Subir Supabase local (ou Postgres equivalente compativel) no pipeline para testes de integracao

### CD (MVP)
- Deploy em staging automatico na branch principal
- Deploy em producao manual com aprovacao
- Revisoes Alembic executadas de forma segura no Supabase (staging antes de producao)

### Entregaveis obrigatorios
1. Pipeline CI em arquivo versionado (`.github/workflows/...` ou equivalente).
2. Estrategia de rollback documentada.
3. Checklist de release (`docs/release-checklist.md`).
4. Seed inicial e smoke tests pos-deploy.
5. Passo de migracao/validacao para projeto Supabase de staging e producao.

### Criterios de aceite
- PR so mergeia com testes verdes.
- Ambiente staging reproduzivel.
- Release com rollback claro em menos de 15 min.
- Migracoes e seed executam sem ajuste manual no Supabase de staging.
