# Prompt 05 - Engine de Score Deterministica

## Copie e envie este prompt para a IA
Voce e um Senior Backend Engineer com foco em regras de negocio. Implemente a engine de score do MVP sem uso de LLM no calculo principal.
Use o backend FastAPI existente (routers + services + repositories + SQLAlchemy).

### Objetivo
Calcular "Score de Chance de Sucesso" por pais/programa de forma auditavel, deterministica e reproduzivel.

### Entradas obrigatorias
- idade
- escolaridade
- profissao (com mapeamento padronizado, ex: ISCO/NOC quando aplicavel)
- idiomas (nivel por idioma, ex: CEFR ou IELTS equivalente)
- renda atual

### Regras de implementacao
1. Motor de regras baseado em dados (`RuleCondition` + `RuleOutcome`).
2. Sem if/else hardcoded por pais no codigo.
3. Ordem de avaliacao:
   - validacoes bloqueantes
   - pontuacao acumulada
   - normalizacao 0-100
4. Resultado deve incluir:
   - score final
   - faixa (`baixo`, `medio`, `alto`)
   - fatores positivos
   - gaps criticos
   - versao do programa usada
5. Cada item do breakdown precisa apontar para a regra que gerou o ponto.

### Entregaveis obrigatorios
- Servico de dominio `ScoreEngine` com testes unitarios robustos.
- Fixtures de regras para ao menos 3 paises na primeira entrega.
- Endpoint `/assessments/{id}/breakdown` com explicabilidade.
- Documento de formula de score.

### Casos de teste obrigatorios
- Perfil com bloqueio imediato.
- Perfil com score alto mas gap de idioma.
- Perfil que muda de faixa ao alterar apenas 1 variavel.
- Reprocessamento do mesmo snapshot com mesmo resultado.

### Criterios de aceite
- Engine reprodutivel e auditavel.
- Explicabilidade por criterio disponivel via API.
- Cobertura de testes de negocio acima de 80% no modulo de score.
