# Prompt 01 - Arquitetura Base (MVP Escalavel)

## Copie e envie este prompt para a IA
Voce e um Staff Software Architect. Quero iniciar um SaaS de imigracao do zero com foco em escalabilidade e velocidade de entrega de MVP.

### Contexto do produto
- Produto: SaaS de Imigracao (Freemium)
- Funcionalidade gratuita: score de chance de sucesso por pais/programa
- Funcionalidade paga: roadmap personalizado gerado por IA
- Usuarios: brasileiros interessados em imigrar
- Time inicial: 1 dev backend/data (eu), com IA codando por etapas

### Decisoes obrigatorias
- Backend obrigatoriamente em Python com FastAPI.
- Usar arquitetura modular por dominios (routers, services, repositories, models, schemas).
- Adotar SQLAlchemy 2 + Alembic + Pydantic Settings.
- Frontend separado do backend.
- Infra local via Docker Compose.
- Jobs assincronos obrigatorios para score/roadmap.

### Entregaveis obrigatorios
1. Diagrama textual de arquitetura (componentes + fluxo fim a fim).
2. Estrutura de repositorios sugerida:
   - Opcao A: monorepo (`apps/api`, `apps/web`, `infra`, `docs`)
   - Opcao B: 2 repos separados
   - Indicar recomendacao final e por que.
3. Estrutura de pastas detalhada para backend e frontend.
4. Definicao de ambientes (`dev`, `staging`, `prod`) e variaveis de ambiente por servico.
5. Plano de escalabilidade em 3 niveis:
   - MVP (baixo custo)
   - Growth (1k-10k usuarios ativos)
   - Scale (10k+)
6. Decisoes de dados:
   - PostgreSQL como fonte de verdade
   - Redis para fila/cache
   - S3-compativel para documentos brutos (se necessario)
7. Roadmap tecnico em 12 semanas (sprints semanais).

### Requisitos de qualidade
- Nao usar regras de imigracao hardcoded no codigo.
- Tudo com versionamento temporal de regra (`effective_from`, `effective_to`).
- Score deve ser deterministicamente reproduzivel.
- Roadmap por LLM deve sempre referenciar gaps concretos do score.

### Criterios de aceite
- Arquitetura apresentada com prós e contras claros.
- Estrutura de pastas pronta para implementacao imediata.
- Dependencias principais listadas.
- Sequencia de implementacao sem ambiguidade.
