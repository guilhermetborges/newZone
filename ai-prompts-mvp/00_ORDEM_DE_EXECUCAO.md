# Ordem de Execucao dos Prompts (MVP SaaS de Imigracao)

## Objetivo
Este pacote foi criado para voce enviar os prompts para um agente de IA em partes, com baixo risco de retrabalho, mantendo base escalavel para evoluir o MVP.

## Stack escolhida (recomendada)
- Backend: FastAPI + SQLAlchemy 2 + Alembic + PostgreSQL + Redis + Celery
- Frontend: Next.js (App Router) + TypeScript + Tailwind + React Query
- Infra local: Docker Compose
- Billing: Stripe
- LLM: OpenAI (camada de provider abstrata para permitir Claude no futuro)

## Ordem correta de envio para a IA
1. `ai-prompts-mvp/01_PROMPT_ARQUITETURA_BASE.md`
2. `ai-prompts-mvp/02_PROMPT_BACKEND_SETUP.md`
3. `ai-prompts-mvp/03_PROMPT_MODELO_DADOS_REGRAS.md`
4. `ai-prompts-mvp/04_PROMPT_API_ROTAS_E_CONTRATOS.md`
5. `ai-prompts-mvp/05_PROMPT_ENGINE_SCORE.md`
6. `ai-prompts-mvp/06_PROMPT_CELERY_E_LLM_ROADMAP.md`
7. `ai-prompts-mvp/07_PROMPT_FREEMIUM_E_BILLING.md`
8. `ai-prompts-mvp/08_PROMPT_FRONTEND_BASE.md`
9. `ai-prompts-mvp/09_PROMPT_FRONTEND_FLUXOS.md`
10. `ai-prompts-mvp/10_PROMPT_INGESTAO_DADOS_LEGAIS.md`
11. `ai-prompts-mvp/11_PROMPT_OBSERVABILIDADE_SEGURANCA.md`
12. `ai-prompts-mvp/12_PROMPT_TESTES_CI_CD_RELEASE.md`
13. `ai-prompts-mvp/13_PROMPT_SEED_15_PAISES_E_FONTES.md`

## Regras de uso
- Envie um prompt por vez.
- So avance para o proximo quando os criterios de aceite do prompt atual forem atendidos.
- Sempre pedir para a IA:
  - criar revisoes Alembic,
  - atualizar testes,
  - atualizar documentacao,
  - e devolver lista de arquivos alterados.

## Base de paises para o MVP (15 paises)
Criterio: maiores comunidades brasileiras no exterior, usando o relatorio oficial do MRE (Estatisticas 2023) e priorizando paises soberanos.

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

Observacao:
- Se voce quiser incluir territorio nao soberano no ranking, a Guiana Francesa (Franca) entra com volume alto e pode substituir a Belgica no top 15.

## Fontes principais utilizadas
- MRE - Comunidade brasileira no exterior (Estatisticas 2023):
  - https://www.gov.br/mre/pt-br/assuntos/portal-consular/comunidade-brasileira-no-exterior-estatisticas-2023
  - PDF oficial: https://www.gov.br/mre/pt-br/assuntos/portal-consular/BrasileirosnoExterior2023.pdf
- Contexto complementar (top 10 com os mesmos valores do MRE):
  - https://agenciabrasil.ebc.com.br/geral/noticia/2024-08/portugal-supera-japao-e-vira-2o-pais-com-mais-brasileiros-no-mundo
