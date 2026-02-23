# Prompt 06 - Processamento Assincrono (Celery) e Roadmap com LLM

## Copie e envie este prompt para a IA
Voce e um Arquiteto de Sistemas Distribuidos. Implemente fila assincrona para nao travar requests e gere roadmap por LLM apenas para usuarios pagos.
Use o backend FastAPI existente e mantenha contratos de API estaveis.

### Objetivo
Separar processamento em duas filas:
- `score_queue`: calculo rapido deterministico
- `roadmap_queue`: geracao textual estruturada por LLM

### Fluxo obrigatorio
1. `POST /assessments` cria registro com status `PENDING`.
2. Worker processa score e muda status para `COMPLETED` ou `FAILED`.
3. `POST /roadmaps` valida entitlement Pro.
4. Worker LLM gera roadmap com base em gaps reais do score.
5. Roadmap salvo em estrutura (`Roadmap`, `RoadmapStep`).

### Requisitos tecnicos
- Celery retries com exponential backoff.
- Idempotencia por `assessment_id` e `roadmap_id`.
- Timeout por tarefa e dead-letter strategy (ou equivalente).
- Logs com `trace_id` e metrica de duracao por job.
- Provider LLM com interface abstrata:
  - `LLMProvider.generate_roadmap(input) -> output`
- Implementar provider OpenAI e stub de provider Claude.

### Prompt engineering obrigatorio (interno do sistema)
- Entrada: perfil, score, breakdown, gaps, programa alvo.
- Saida JSON estruturada:
  - objetivo
  - passos priorizados
  - prazo estimado por passo
  - dependencia entre passos
  - risco por passo
  - criterio de conclusao por passo
- Proibir alucinacao legal: se faltar confianca, marcar `manual_review_required=true`.

### Entregaveis obrigatorios
- Tasks Celery + configuracao worker/beat.
- Endpoint de polling de status.
- Persistencia completa do roadmap.
- Testes de task (sucesso, retry, timeout, erro de provider).

### Criterios de aceite
- Request web retorna rapido (`202`) sem bloquear.
- Roadmap sempre vinculado a um assessment valido.
- Falhas de LLM nao derrubam API principal.
