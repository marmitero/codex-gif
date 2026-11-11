# Auditoria de integridade — Louis — 11/11/2026

**Resultado: nenhuma falha de decodificação, link local quebrado ou divergência de hash nos metadados verificados após o commit manual e a conclusão documental de L3.6.**

Base binária auditada: commit `823a1871c1b7938e171ca8f65576e1326fbfa2be` (“etapa manual”). Esta revisão não modifica imagens.

## Cobertura

| Verificação | Resultado |
|---|---|
| PNGs | 15 fontes decodificadas integralmente; estrutura verificada pelo Pillow |
| GIFs | 7 arquivos, 56 frames decodificados; todos com oito frames de 120 ms |
| Dimensões e SHA-256 documentados | Conferidos nos metadados JSON que registram esses campos |
| JSON | Todos os arquivos analisados com parser; caminhos de assets, referências e prompts conferidos |
| Links locais | Markdown, imagens HTML e referências do state.ai conferidos pelo script |
| Corte nas folhas PNG | Inspeção visual de todas as folhas + teste aproximado de margem por célula; nenhum personagem encostando nos limites das células |
| GIFs | Inspeção visual dos 56 quadros, sem partes do personagem cortadas pelo canvas |
| Inventário atual | 7/8 direções com arte + Idle: S/N/E/W/SE/SW/NE |

Medições detalhadas, hashes, contagens e margens: [integridade.json](../analise/integridade.json). Reproduzir com `python analise/validar_integridade.py`, com Pillow e NumPy instalados. [Script](../analise/validar_integridade.py).

## O que o commit manual corrigiu

- Acrescentou PNG e GIF Idle NE, cujos hashes coincidem com os originais recuperados na publicação anterior. JSON e registro Markdown adicionados nesta revisão.
- Substituiu o PNG **Oeste (W)** incompleto por um arquivo de 1.761.945 bytes, plenamente decodificável, com SHA-256 `c105e779c594d392c9445b110121653571b3224dcb539911f91c7341c95d047f`, igual ao registro de congelamento existente.
- O PNG **SW não mudou** nesse commit: SHA-256 `520ca8c2da452066984f089ba662722ca6369f9275b8a2507b68de27acfaad11`. Abre completo, com oito personagens sem corte observado.

## Pendências e diferenças preservadas

- NW ainda não foi produzido; sua ausência é planejada. L3.7 será a arte estática NW; L3.8, Idle NW + GIF. Locomoção nas oito direções também segue pendente.
- As folhas SW e NE medem 1491 × 1055, não 1448 × 1086. São fontes de apresentação, não atlas regulares de células 362 × 543. Não recortar automaticamente usando a grade cardinal.
- O GIF frontal recebido tem apresentação escura/transparente e tratamento visual diferente da folha magenta frontal; equivalência pixel a pixel com a folha não foi certificada. Preservado como recebido, com procedência explícita no [JSON S](../animacoes/louis-idle-s-v1.json).
- A prévia NE apresenta variação/retângulo de magenta no fundo. Isso já está nos bytes aprovados; não é corte do personagem. A normalização de fundo pertence à preparação para integração.
- A arte posterior v1 contém o erro histórico de oclusão já documentado. Está preservada para histórico; a autoridade posterior é v2.
- Prompts literais dos Idles N, W e NE não foram recuperados. Não existem arquivos de prompt inventados para preencher essas lacunas.
- Transparência, atlas, pivôs e validação em motor continuam em L5. A revisão visual e o teste aproximado de margens não certificam identidade de cada pixel, qualidade temporal em jogo ou profundidade geométrica. URLs externas e âncoras de seção não fazem parte do teste de links locais.

Os registros datados de etapas anteriores descrevem o estado na data de cada publicação. O estado atual está no inventário do README, no cabeçalho do state.ai e em L3.6.
