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

## Estado atual

Etapa L0 concluída: referências preservadas e analisadas; documentação inicial criada. Aguardando próxima instrução do usuário. Nenhuma animação nova foi gerada. A cada entrega, salvar fontes e resultados aqui e atualizar README, roadmap e state.ai. Não criar uma nova direção ou ação antes da próxima instrução.
