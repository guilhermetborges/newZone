# Prompt 11 - Observabilidade, Seguranca e Resiliencia

## Copie e envie este prompt para a IA
Voce e um SRE + Security Engineer. Fortaleca o SaaS para operacao estavel, segura e auditavel.
Considere backend FastAPI + workers Celery + frontend Next.js separados, com PostgreSQL no Supabase.

### Objetivo
Adicionar padroes minimos de producao para backend, workers e frontend.
Cobrir observabilidade e seguranca tambem para operacao no Supabase.

### Observabilidade obrigatoria
- Logs estruturados JSON com `trace_id`, `user_id`, `assessment_id`, `roadmap_id`.
- Metricas de negocio:
  - tempo medio de score
  - tempo medio de roadmap
  - taxa de erro por provider LLM
  - taxa de conversao free->pro
- Metricas tecnicas:
  - fila Celery (pendente/processando/falha)
  - latencia p95 endpoints criticos
  - disponibilidade por servico
  - conexoes ativas no Postgres (Supabase)
  - query lenta e erro de transacao no banco

### Seguranca obrigatoria
- Rate limit em auth e endpoints de criacao.
- Protecao de webhook Stripe por assinatura.
- Secrets apenas via env/secret manager.
- Sanitizacao e validacao de entrada (Zod no front, Pydantic/FastAPI no back).
- Politica de permissao por recurso (RBAC simples + ownership).
- CORS estrito por ambiente.
- RLS no Supabase para dados multi-tenant.
- Separacao de chaves: `anon` no frontend e `service_role` somente backend/workers.
- Nenhuma chave sensivel no bundle do frontend.

### Confiabilidade
- Circuit breaker/fallback para provider LLM.
- Dead letter / quarantine para tasks falhadas.
- Retry policy diferenciada para erro transitorio vs erro definitivo.
- Jobs idempotentes.

### Entregaveis obrigatorios
- Middlewares e configuracoes de seguranca.
- Dashboard basico de metricas (mesmo que simples em Prometheus/Grafana local).
- Runbook de incidentes em markdown.
- Checklist de hardening do Supabase (RLS, policies, rotacao de chaves, backups).

### Criterios de aceite
- Sistema continua operante mesmo com falha do provider LLM.
- Endpoints criticos protegidos contra abuso.
- Equipe consegue rastrear qualquer erro por `trace_id`.
- Usuario nao consegue acessar dados de outro tenant (validado por policy RLS).
