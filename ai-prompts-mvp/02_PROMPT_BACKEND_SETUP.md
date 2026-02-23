# Prompt 02 - Setup Backend e Infra Local

## Copie e envie este prompt para a IA
Voce e um Senior Backend Engineer. Implemente o bootstrap de backend para o SaaS de imigracao, sem regras de negocio ainda.

### Stack obrigatoria
- Python 3.12+
- FastAPI
- SQLAlchemy 2
- Alembic
- Pydantic v2 / pydantic-settings
- PostgreSQL
- Redis
- Celery + Celery Beat
- Poetry ou uv (escolha uma e padronize)
- Docker Compose

### Objetivo desta etapa
Subir backend limpo e modular com healthchecks, autenticacao JWT, padrao de configuracao por ambiente e observabilidade minima.

### Estrutura de modulos (obrigatoria)
- `apps/accounts`
- `apps/immigration_rules`
- `apps/assessments`
- `apps/roadmaps`
- `apps/billing`
- `apps/ingestion`
- `apps/common`
- `app/api` (roteadores v1)
- `app/core` (config, seguranca, observabilidade)
- `app/db` (engine, session, base, migrations)

### Entregaveis obrigatorios
1. Projeto FastAPI criado com configuracao por ambiente:
   - `app/core/config/base.py`
   - `app/core/config/dev.py`
   - `app/core/config/prod.py`
2. Docker Compose com servicos:
   - `api`
   - `worker`
   - `beat`
   - `postgres`
   - `redis`
3. Health endpoints:
   - `GET /health/live`
   - `GET /health/ready`
4. Auth JWT inicial:
   - `POST /api/v1/auth/register`
   - `POST /api/v1/auth/login`
   - `POST /api/v1/auth/refresh`
   - `GET /api/v1/auth/me`
5. Ferramentas de qualidade:
   - Ruff
   - Black
   - Pytest
   - pre-commit
6. OpenAPI automatica:
   - `GET /openapi.json`
   - `GET /docs`
   - `GET /redoc`

### Requisitos de implementacao
- Timezone UTC end-to-end (`datetime` timezone-aware).
- `.env.example` completo com todas as variaveis.
- Logging em JSON (nivel info/debug por ambiente).
- CORS configurado para frontend separado.
- Alembic configurado e pronto para autogenerate.
- Dependencia de banco via `Depends(get_db)` e sessions curtas por request.

### Criterios de aceite
- `docker compose up` sobe tudo sem erro.
- Migracoes Alembic rodam sem ajuste manual.
- Endpoints de auth e health respondem.
- Testes smoke de auth + health presentes.
