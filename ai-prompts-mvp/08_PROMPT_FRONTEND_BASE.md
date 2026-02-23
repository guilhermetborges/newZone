# Prompt 08 - Frontend Base (Separado do Backend)

## Copie e envie este prompt para a IA
Voce e um Senior Frontend Engineer. Construa a base do frontend separado para consumir a API do SaaS de imigracao.

### Stack obrigatoria
- Next.js (App Router)
- TypeScript
- Tailwind CSS
- React Query
- Zod + React Hook Form

### Objetivo
Criar shell de aplicacao com layout, autenticacao, estado global e cliente HTTP tipado.

### Rotas frontend obrigatorias
- `/` landing
- `/login`
- `/register`
- `/onboarding`
- `/results/[assessmentId]`
- `/pricing`
- `/roadmaps/[roadmapId]`
- `/dashboard`
- `/settings/subscription`

### Interface ideal (UX)
1. Landing
- Hero com proposta clara
- CTA "Calcular Score Gratis"
- Cards comparando Free vs Pro

2. Onboarding (multi-step)
- Step 1: idade + escolaridade
- Step 2: profissao + anos experiencia
- Step 3: idiomas + nivel
- Step 4: renda atual + paises de interesse
- Barra de progresso e validacao por step

3. Resultado de score
- Score principal (0-100)
- Breakdown por criterio
- Lista de gaps
- CTA contextual para roadmap Pro

4. Roadmap
- Passos em formato checklist
- Prioridade (alta/media/baixa)
- Prazo estimado
- Dependencias entre passos

### Entregaveis obrigatorios
- Design system minimo (tokens de cor, tipografia, espacamento).
- Cliente API centralizado com interceptors de auth.
- Guards de rota para paginas privadas.
- Paginas com estados de loading/empty/error.

### Criterios de aceite
- Frontend sobe em ambiente local e conversa com backend.
- Fluxos principais navegaveis ponta a ponta.
- Layout responsivo mobile + desktop.

