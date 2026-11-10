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
| [Idle Oeste W v1 PNG](animacoes/louis-idle-w-v1.png) | 1448 × 1086 | Aprovado e congelado; 8 quadros em 4 × 2 |
| [GIF de validação W v1](animacoes/louis-idle-w-v1.gif) | 362 × 543 | Aprovado; 8 frames, 120 ms/quadro |

Ambos são PNG RGBA opacos com fundo magenta variável. Não são exports transparentes prontos para o motor. Oito direções são o objetivo; a referência recebida cobre somente a frente. Os originais não foram alterados.

## Arte posterior congelada

- [Louis de costas, parado — v2](artes/louis-costas-parado-v2.png): uma arte estática de 1254 × 1254, sem frames; aprovada e congelada pelo usuário em 10/11/2026.
- [Registro e validação](artes/louis-costas-parado-v2.md) e [prompt real](prompts/louis-costas-parado-v2.txt).

## Estado atual

L0 concluída. L1 concluída: arte posterior estática v2 aprovada e congelada em 10/11/2026. Usar a v2 como referência obrigatória para costas e derivações posteriores. L3 iniciada: arte estática Leste v1 aprovada e congelada em 10/11/2026; Idle E v1 aprovado e congelado. L2: Idle N (costas) v1 aprovado e congelado em 10/11/2026; PNG original e prévia GIF publicados. O prompt real desta geração não foi recuperado; a lacuna está registrada. Manter fontes e resultados aqui e atualizar README, roadmap e state.ai em cada entrega.

Regra obrigatória: [posição e oclusão dos equipamentos](docs/oclusao-equipamentos.md), com [contrato JSON](docs/oclusao-equipamentos.json). V1 preservada apenas como histórico; v2 corrige bolsa e adaga na vista posterior.

## Idle posterior aprovado e congelado

- [Folha Idle N v1](animacoes/louis-idle-n-v1.png): 1448 × 1086, RGB opaco, oito quadros em grade 4 × 2; original preservado sem edição.
- [Prévia GIF](animacoes/louis-idle-n-v1.gif): leitura por linhas, 120 ms/quadro; timing de prévia, sem validação em motor.
- [Registro de aprovação e limites](animacoes/louis-idle-n-v1.md) e [metadados](animacoes/louis-idle-n-v1.json).
- A folha é referência congelada de Idle N. Alterações exigem nova versão e aprovação; manter a arte estática v2 como autoridade de design posterior.

## Arte Leste aprovada e congelada

- [Louis Leste parado v1](artes/louis-leste-parado-v1.png): 1254 × 1254, pose única olhando para a direita, aprovada e congelada em 10/11/2026.
- [Registro e regras de visibilidade](artes/louis-leste-parado-v1.md), [metadados](artes/louis-leste-parado-v1.json) e [prompt literal](prompts/louis-leste-parado-v1.txt).
- Referência estática obrigatória para Idle E. PNG original preservado; mudanças exigem nova versão e aprovação. Idle E v1 aprovado e congelado.

## Idle E v1 — aprovado e congelado em 10/11/2026

[Folha PNG](animacoes/louis-idle-e-v1.png), [prévia GIF](animacoes/louis-idle-e-v1.gif), [registro](animacoes/louis-idle-e-v1.md), [metadados](animacoes/louis-idle-e-v1.json) e [prompt literal](prompts/louis-idle-e-v1.txt) publicados. Oito quadros, grade 4 × 2, 1448 × 1086; GIF com 120 ms/quadro. Aprovação explícita: “aprovado! publique e atualize a documentação”. Preservar PNG e prompt sem sobrescrever; mudanças exigem nova versão e aprovação. Timing de prévia; integração e ancoragem exata no motor ainda pendentes. Próxima ação/direção a definir pelo usuário.

## Arte Oeste aprovada e congelada — 10/11/2026

[Louis Oeste parado v1](artes/louis-oeste-parado-v1.png): pose única olhando para a esquerda da tela (W), 1254 × 1254, RGB, fundo magenta opaco. Aprovada e congelada pelo usuário: “ficou boa! congele e publique. atualize os documentos do repositorio também.” PNG original e prompt literal preservados, sem recorte ou redimensionamento. [Registro](artes/louis-oeste-parado-v1.md), [metadados](artes/louis-oeste-parado-v1.json) e [prompt](prompts/louis-oeste-parado-v1.txt).

Lado esquerdo anatômico próximo: ombreira metálica única e adaga anterior esquerda visíveis, com sobreposição pelo braço. Bolsa anterior direita, faixa direita e tira da coxa direita ficam no lado distante, ocultas nesta pose; marca da bochecha direita não aparece. Não espelhar E para obter W. Esta arte é a autoridade estática para Idle W v1, junto das referências frontal, posterior v2 e E. Alterações exigem nova versão e aprovação. A etapa estática não incluiu animação. O Idle W v1 foi publicado posteriormente, conforme registro abaixo; validação em motor pendente.

## Idle Oeste W v1 aprovado e congelado — 10/11/2026

Folha PNG e GIF de validação recuperados da conversa anterior e publicados sem alteração de bytes. Oito quadros, grade 4 × 2; GIF com 120 ms/quadro e ciclo de 960 ms. [Registro de aprovação, procedência e limites](animacoes/louis-idle-w-v1.md) e [metadados com hashes](animacoes/louis-idle-w-v1.json). Não sobrescrever; mudanças exigem nova versão e aprovação. A arte Oeste parada v1 continua como autoridade estática. Prompt literal do Idle W não recuperado nesta publicação. Transparência, atlas e validação em motor permanecem em L5. L3 em andamento; próxima ação/direção a definir pelo usuário.
