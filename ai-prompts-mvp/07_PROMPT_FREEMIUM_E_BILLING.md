# Prompt 07 - Freemium, Entitlements e Billing

## Copie e envie este prompt para a IA
Voce e um Senior Backend Engineer de SaaS. Implemente o modelo freemium com controle de uso e assinatura Pro.
Use o backend FastAPI existente com dependencias de seguranca e regras por entitlement.

### Objetivo de negocio
- Free: score e breakdown basico
- Pro: roadmap IA + historico estendido + comparacao entre paises

### Regras de monetizacao (MVP)
- Free:
  - ate 3 assessments por mes
  - sem roadmap IA
- Pro:
  - assessments ilimitados
  - roadmap IA liberado
  - prioridade em processamento

### Entidades obrigatorias
- `Plan`
- `Subscription`
- `Entitlement`
- `UsageCounter` (janela mensal)
- `BillingEvent`

### Integracao de pagamento
- Stripe Checkout
- Webhook assinado para:
  - `checkout.session.completed`
  - `invoice.paid`
  - `customer.subscription.updated`
  - `customer.subscription.deleted`

### Entregaveis obrigatorios
1. Middleware/permission para bloquear recurso sem entitlement.
2. Endpoint de checkout:
   - `POST /api/v1/billing/checkout-session`
3. Endpoint de webhook:
   - `POST /api/v1/billing/webhook/stripe`
4. Endpoint de consulta:
   - `GET /api/v1/entitlements/me`
5. Testes cobrindo upgrade/downgrade/cancelamento.

### Requisitos de seguranca
- Validar assinatura de webhook.
- Nao confiar em valor vindo do frontend para plano.
- Idempotencia em eventos de webhook.

### Criterios de aceite
- Usuario free bloqueado corretamente no roadmap.
- Upgrade para Pro libera roadmap sem intervencao manual.
- Downgrade/cancelamento reflete entitlements corretamente.
