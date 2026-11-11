# L3.9 — Conferência final das oito direções

Data: 11/11/2026. Base auditada: `c99ad131a214f265b0e9bd572f950d0da399f3d6`.

**Resultado: conjunto de repouso completo nas oito direções, com ressalvas de integração registradas.** Nenhuma imagem aprovada foi modificada. Esta conferência não constitui nova aprovação artística nem encerra a locomoção prevista em L3.

## Inventário conferido

| Direção | Autoridade estática | Folha Idle | GIF e registros |
|---|---|---|---|
| S | [PNG](../referencias/arte%20congelada%20Louis.png) | [PNG](../referencias/Idle%20front%20Louis.png) | [GIF](../animacoes/louis-idle-s-v1.gif) · [MD](../animacoes/louis-idle-s-v1.md) · [JSON](../animacoes/louis-idle-s-v1.json) |
| N | [PNG](../artes/louis-costas-parado-v2.png) | [PNG](../animacoes/louis-idle-n-v1.png) | [GIF](../animacoes/louis-idle-n-v1.gif) · [MD](../animacoes/louis-idle-n-v1.md) · [JSON](../animacoes/louis-idle-n-v1.json) |
| E | [PNG](../artes/louis-leste-parado-v1.png) | [PNG](../animacoes/louis-idle-e-v1.png) | [GIF](../animacoes/louis-idle-e-v1.gif) · [MD](../animacoes/louis-idle-e-v1.md) · [JSON](../animacoes/louis-idle-e-v1.json) |
| W | [PNG](../artes/louis-oeste-parado-v1.png) | [PNG](../animacoes/louis-idle-w-v1.png) | [GIF](../animacoes/louis-idle-w-v1.gif) · [MD](../animacoes/louis-idle-w-v1.md) · [JSON](../animacoes/louis-idle-w-v1.json) |
| SE | [PNG](../artes/louis-sudeste-parado-v1.png) | [PNG](../animacoes/louis-idle-se-v1.png) | [GIF](../animacoes/louis-idle-se-v1.gif) · [MD](../animacoes/louis-idle-se-v1.md) · [JSON](../animacoes/louis-idle-se-v1.json) |
| SW | [PNG](../artes/louis-sudoeste-parado-v1.png) | [PNG](../animacoes/louis-idle-sw-v1.png) | [GIF](../animacoes/louis-idle-sw-v1.gif) · [MD](../animacoes/louis-idle-sw-v1.md) · [JSON](../animacoes/louis-idle-sw-v1.json) |
| NE | [PNG](../artes/louis-nordeste-parado-v1.png) | [PNG](../animacoes/louis-idle-ne-v1.png) | [GIF](../animacoes/louis-idle-ne-v1.gif) · [MD](../animacoes/louis-idle-ne-v1.md) · [JSON](../animacoes/louis-idle-ne-v1.json) |
| NW | [PNG](../artes/louis-noroeste-parado-v1.png) | [PNG](../animacoes/louis-idle-nw-v1.png) | [GIF](../animacoes/louis-idle-nw-v1.gif) · [MD](../animacoes/louis-idle-nw-v1.md) · [JSON](../animacoes/louis-idle-nw-v1.json) |

## Verificação técnica

- 26 imagens: 18 PNGs e oito GIFs, incluindo fontes duplicadas e arte N v1 histórica. Decodificação integral com Pillow.
- Oito GIFs, 64 frames: 362 × 543 px, oito frames de 120 ms por arquivo, ciclo de 960 ms e loop infinito.
- JSONs válidos; caminhos e hashes registrados conferidos. Hashes atuais de todas as imagens disponíveis no [relatório de medições](../analise/integridade-l3-9.json).
- Links locais Markdown/HTML/state.ai verificados; nenhuma falha. URLs externas e âncoras não verificadas.
- Teste aproximado de margens nas células PNG sem contato do personagem com os limites. Não equivale a máscara semântica.
- Reprodução: `python analise/validar_integridade.py --output analise/integridade-l3-9.json`. O script agora identifica o commit de entrada dinamicamente, sem atribuir a revisão atual ao antigo commit manual.

## Conferência visual

Comparação lado a lado das oito artes oficiais, das 64 células Idle e dos 64 frames dos GIFs, na ordem temporal por linhas, incluindo os extremos 8→1. Não observado corte de cabelo, pés ou equipamento pelo canvas, direção ausente, membros extras evidentes ou troca grosseira de identidade. Cabelo castanho, couro marrom, creme, bordô e metal prateado mantêm a família visual. Há pequenas variações desenhadas entre poses; esta revisão não certifica escala ou pivô numericamente estáveis.

A ombreira permanece no lado esquerdo anatômico: próxima em W/SW/NW e distante em E/SE/NE; não há evidência visual de espelhamento simples entre os pares. N usa a arte v2 oficial. Bolsa e adaga anteriores permanecem ocultas nas vistas posteriores neutras, em acordo geral com o contrato de oclusão. Faixa lateral/posterior mantém visibilidade independente. A conferência é visual, sem geometria 3D ou teste em motor.

## Ressalvas preservadas

1. Artes oficiais: 1254 × 1254. Folhas S/N/E/W/SE: 1448 × 1086, grade 4 × 2 e célula 362 × 543. SW/NE/NW: 1491 × 1055, disposição 4 × 2 com limites proporcionais; não usar como atlas regular de 362 × 543.
2. GIF S recebido tem fundo/tratamento escuro e difere visualmente da folha frontal magenta; equivalência pixel a pixel não certificada. A cópia PNG em animacoes/ é idêntica à folha em referencias/.
3. GIF NE apresenta retângulos/variações de magenta; não são partes do personagem cortadas. Fundos das fontes são opacos e variáveis.
4. N v1 estática permanece como histórico superado. Usar exclusivamente N v2 como autoridade posterior.
5. Prompts literais dos Idles N/W/NE/NW não recuperados; referências recebidas sem prompts originais. Registros não foram preenchidos com reconstruções.
6. GIFs são prévias. Transparência, atlas, pivôs, uniformização de apresentação e comportamento temporal no motor pertencem a L5. Não há certificação de câmera isométrica exata.

## Encerramento da conferência

L3.1–L3.9 concluídas para arte estática e repouso nas oito direções. L3 geral segue em andamento pela locomoção, conforme roadmap original. Próxima produção depende da ação/direção escolhida pelo usuário. README, roadmap, state.ai e documentos de arte/movimento atualizados; histórico anterior preservado.
