# Prompt 04 - API REST: Rotas, Contratos e Semantica

## Copie e envie este prompt para a IA
Voce e um API Designer Senior. Defina e implemente as rotas REST do MVP com versionamento e contratos claros para frontend separado.
O backend ja esta padronizado em FastAPI; siga esse padrao.

### Objetivo
Entregar API `v1` consistente para fluxo completo: onboarding, score gratuito, roadmap pago, e painel de historico.

### Padroes obrigatorios
- Prefixo: `/api/v1`
- JSON only
- Erros padronizados: `{ code, message, details, trace_id }`
- Paginacao cursor ou page/size (escolher e padronizar)
- Idempotency-Key para endpoints sensiveis (criacao de assessment/checkout)

### Rotas obrigatorias
1. Auth
- `POST /auth/register`
- `POST /auth/login`
- `POST /auth/refresh`
- `POST /auth/logout`
- `GET /auth/me`

2. Catalogo
- `GET /countries`
- `GET /countries/{country_code}/programs`
- `GET /programs/{program_id}`

3. Perfil do usuario
- `POST /profiles` (cria snapshot)
- `GET /profiles/latest`
- `GET /profiles/{profile_id}`

4. Score gratuito
- `POST /assessments` (retorna `202` + `assessment_id`)
- `GET /assessments/{assessment_id}` (status + resultado)
- `GET /assessments` (historico)
- `GET /assessments/{assessment_id}/breakdown`

5. Roadmap pago
- `POST /roadmaps` (dispara job assincrono, exige entitlement)
- `GET /roadmaps/{roadmap_id}`
- `GET /roadmaps/{roadmap_id}/steps`

6. Freemium/billing
- `GET /plans`
- `GET /entitlements/me`
- `POST /billing/checkout-session`
- `POST /billing/webhook/stripe`

7. Ingestao interna (protegido)
- `POST /internal/ingestion/runs`
- `GET /internal/ingestion/runs/{run_id}`

### Interface ideal por rota (frontend)
- `/` landing: CTA para "Calcular Score Gratis"
- `/onboarding` formulario multi-step (idade, escolaridade, profissao, idiomas, renda)
- `/results/{assessment_id}` score + breakdown por criterio + CTA "Gerar Roadmap"
- `/pricing` planos Free/Pro
- `/roadmaps/{roadmap_id}` checklist de passos com prioridade
- `/dashboard` historico de scores/roadmaps
- `/settings/subscription` status de assinatura

### Entregaveis obrigatorios
- Routers/dependencies/schemas Pydantic implementados.
- OpenAPI com exemplos de request/response.
- Colecao HTTP (`.http` ou Postman) para teste manual.
- Testes de contrato para pelo menos 10 rotas.

### Criterios de aceite
- API navegavel e documentada.
- Todos os codigos HTTP coerentes (`200`, `201`, `202`, `400`, `401`, `402`, `403`, `404`, `409`, `422`).
- Frontend consegue implementar sem duvidas de contrato.
