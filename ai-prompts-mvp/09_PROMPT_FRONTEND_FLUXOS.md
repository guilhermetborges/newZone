# Prompt 09 - Frontend: Fluxos, Estados e Integracao por Rota

## Copie e envie este prompt para a IA
Voce e um Product Engineer. Implemente fluxos completos no frontend com base nas rotas de API e regras freemium.

### Objetivo
Conectar toda interface aos endpoints reais, com tratamento de estados assincronos e gating de monetizacao.

### Mapeamento rota frontend -> API
1. `/onboarding`
- `POST /api/v1/profiles`
- `POST /api/v1/assessments`
- redirect para `/results/{assessmentId}`

2. `/results/[assessmentId]`
- polling `GET /api/v1/assessments/{id}` ate `COMPLETED`
- `GET /api/v1/assessments/{id}/breakdown`
- CTA "Gerar Roadmap" chama `POST /api/v1/roadmaps`

3. `/pricing`
- `GET /api/v1/plans`
- `POST /api/v1/billing/checkout-session`

4. `/roadmaps/[roadmapId]`
- `GET /api/v1/roadmaps/{id}`
- `GET /api/v1/roadmaps/{id}/steps`

5. `/dashboard`
- `GET /api/v1/assessments`
- lista historico e atalhos

6. `/settings/subscription`
- `GET /api/v1/entitlements/me`
- status da assinatura e limites de uso

### Requisitos de UX
- Polling com backoff e timeout amigavel.
- Erros de entitlement (`402/403`) com modal de upgrade.
- Skeleton loading nas listas e cards.
- Mensagens de erro acionaveis (ex: "tente novamente", "fazer upgrade").

### Requisitos de tracking
- Instrumentar eventos:
  - `onboarding_started`
  - `assessment_requested`
  - `assessment_completed`
  - `roadmap_upgrade_clicked`
  - `checkout_started`
  - `roadmap_generated`

### Entregaveis obrigatorios
- Hooks por dominio (`useAssessment`, `useRoadmap`, `useSubscription`).
- Componentes reutilizaveis para score/gaps/checklist.
- Testes de interface basicos (RTL ou Playwright).

### Criterios de aceite
- Jornada Free completa funcionando.
- Jornada de upgrade para Pro funcionando.
- Roadmap pago exibido de ponta a ponta.

