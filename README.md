# Louis — codex-gif

Repositório de referências e produção de sprites de Louis para MMO RPG 2D isométrico em oito direções.

## Documentação oficial

- [Arte Louis.md](Arte%20Louis.md): identidade visual congelada, roupas, lateralidade, cores e regras de fidelidade.
- [Padrão de movimentação Louis.md](Padr%C3%A3o%20de%20movimenta%C3%A7%C3%A3o%20Louis.md): análise dos oito quadros, grade, ancoragem e produção futura.
- [roadmap.md](roadmap.md): etapas e entregas pendentes.
- [state.ai](state.ai): estado para retomada por outra sessão.
- [analise/medicoes.json](analise/medicoes.json): dimensões, hashes e caixas medidas.
- [analise/medir.py](analise/medir.py): reprodução das medidas (Python, Pillow e NumPy).

## Inventário

| Arquivo | Dimensões | Uso |
|---|---|---|
| [referencias/arte congelada Louis.png](referencias/arte%20congelada%20Louis.png) | 1254 × 1254 | Arte principal, frente |
| [referencias/Idle front Louis.png](referencias/Idle%20front%20Louis.png) | 1448 × 1086 | Idle frontal: 8 quadros, 4 × 2 |

Ambos são PNG RGBA opacos com fundo magenta variável. Não são exports transparentes prontos para o motor. Oito direções são o objetivo; a referência recebida cobre somente a frente. Os originais não foram alterados.

## Nova arte para aprovação

- [Louis de costas, parado — v2](artes/louis-costas-parado-v2.png): uma arte estática de 1254 × 1254, sem frames; proposta ainda não congelada.
- [Registro e validação](artes/louis-costas-parado-v2.md) e [prompt real](prompts/louis-costas-parado-v2.txt).

## Estado atual

L0 concluída. L1: arte posterior estática v2 corrigida, aguardando aprovação do usuário para congelamento. Nenhuma animação nova foi gerada. Manter fontes e resultados aqui e atualizar README, roadmap e state.ai em cada entrega.

Regra obrigatória: [posição e oclusão dos equipamentos](docs/oclusao-equipamentos.md), com [contrato JSON](docs/oclusao-equipamentos.json). V1 preservada apenas como histórico; v2 corrige bolsa e adaga na vista posterior.
