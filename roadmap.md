# Roadmap Louis

Atualização: 11/11/2026 (recuperação de L3.6; publicação binária pendente).

| Etapa | Escopo | Estado |
|---|---|---|
| L0 | Preservar fontes, analisar arte e idle; criar documentação e estado | Concluída |
| L1 | Receber escolha da próxima ação/direção; planejar poses e confirmar adaptação de câmera pela referência produzida | Concluída: arte posterior estática v2 aprovada e congelada em 10/11/2026 |
| L2 | Produzir e validar a primeira folha nova e sua prévia animada, registrando prompt real | Folha Idle N v1 aprovada, congelada e publicada com prévia GIF; prompt real não recuperado (lacuna documental) |
| L3 | Completar gradualmente idle e locomoção nas oito direções | Em andamento: L3.1–L3.5 concluídas; 7/8 artes; 6/8 pares arte + Idle (S/N/E/W/SE/SW); Idle NE, arte + Idle NW e locomoção pendentes |
| L4 | Ataques e skills em oito direções, com antecipação/impacto/recuperação | Pendente, ações a definir |
| L5 | Exportar atlas, transparência, pivôs e metadados; validar em motor | Pendente, formato do jogo a definir |

A ordem posterior é uma proposta de organização, não autorização para gerar tudo. Uma ação/direção por geração, conforme contrato de movimento. Ações específicas, arma desembainhada, novas direções, quantidade final de frames e timing precisam de validação quando forem produzidos. Atualizar este arquivo em cada publicação.

L1: regra de fixação anterior e oclusão por direção documentada em docs/oclusao-equipamentos.md e JSON. V2 aprovada e congelada pelo usuário em 10/11/2026; não gerar frames sem instrução.

L2 — 10/11/2026: publicado `animacoes/louis-idle-n-v1.png`, sem alterar o original aprovado, com prévia GIF derivada (120 ms/quadro). Registro e metadados na mesma pasta. Aprovação visual não equivale à validação no motor. O prompt literal não foi recuperado e não foi reconstruído; preservar esta pendência documental nas retomadas.

L3 — 10/11/2026: arte estática [Leste v1](artes/louis-leste-parado-v1.md) aprovada e congelada, com PNG original, prompt literal e metadados. Usada como base do Idle E v1 aprovado e congelado; aguardar instrução para próxima ação/direção.

## Idle E v1 — aprovado e congelado em 10/11/2026

[Folha PNG](animacoes/louis-idle-e-v1.png), [prévia GIF](animacoes/louis-idle-e-v1.gif), [registro](animacoes/louis-idle-e-v1.md), [metadados](animacoes/louis-idle-e-v1.json) e [prompt literal](prompts/louis-idle-e-v1.txt) publicados. Oito quadros, grade 4 × 2, 1448 × 1086; GIF com 120 ms/quadro. Aprovação explícita: “aprovado! publique e atualize a documentação”. Preservar PNG e prompt sem sobrescrever; mudanças exigem nova versão e aprovação. Timing de prévia; integração e ancoragem exata no motor ainda pendentes. Próxima ação/direção a definir pelo usuário.

## Arte Oeste aprovada e congelada — 10/11/2026

[Louis Oeste parado v1](artes/louis-oeste-parado-v1.png): pose única olhando para a esquerda da tela (W), 1254 × 1254, RGB, fundo magenta opaco. Aprovada e congelada pelo usuário: “ficou boa! congele e publique. atualize os documentos do repositorio também.” PNG original e prompt literal preservados, sem recorte ou redimensionamento. [Registro](artes/louis-oeste-parado-v1.md), [metadados](artes/louis-oeste-parado-v1.json) e [prompt](prompts/louis-oeste-parado-v1.txt).

Lado esquerdo anatômico próximo: ombreira metálica única e adaga anterior esquerda visíveis, com sobreposição pelo braço. Bolsa anterior direita, faixa direita e tira da coxa direita ficam no lado distante, ocultas nesta pose; marca da bochecha direita não aparece. Não espelhar E para obter W. Esta arte é a autoridade estática para o Idle W v1, junto das referências frontal, posterior v2 e E. Alterações exigem nova versão e aprovação. A etapa estática não incluiu animação; o Idle W v1 foi publicado posteriormente, conforme registro abaixo. Validação em motor pendente.

## Idle Oeste (W) v1 — aprovado e congelado em 10/11/2026

- [Folha original PNG](animacoes/louis-idle-w-v1.png): 1448 × 1086, RGB opaco, fundo magenta, oito quadros em grade 4 × 2 (362 × 543 por célula).
- [GIF de validação aprovado](animacoes/louis-idle-w-v1.gif): 362 × 543, oito frames, 120 ms/quadro, ciclo de 960 ms. Arquivo recuperado da geração anterior e preservado sem regeneração.
- [Registro](animacoes/louis-idle-w-v1.md) e [metadados](animacoes/louis-idle-w-v1.json), com hashes dos dois originais.

A aprovação visual e o congelamento foram solicitados pelo usuário na conversa de origem. Preservar os arquivos; qualquer alteração exige nova versão e aprovação. A arte Oeste parada v1 continua sendo a autoridade estática W. O prompt literal do Idle W não foi recuperado nesta publicação; não reconstruir como se fosse o original. Validação em motor, transparência e atlas continuam pendentes em L5. Próxima ação/direção a definir pelo usuário.

## Conferência do conjunto cardinal — 10/11/2026

Inventário recursivo e registros conferidos: S (referências originais), N (costas v2 + Idle N v1), E (arte v1 + Idle v1) e W (arte v1 + Idle v1) possuem arte estática + folha Idle de oito quadros. São 4/4 cardeais e 4/8 direções do objetivo. GIFs existentes de N/E/W incorporados ao README; frente inicialmente exibida como folha original; GIF frontal publicado posteriormente, conforme registro abaixo. Diagonais NE/NW/SE/SW e locomoção seguem pendentes; L3 permanece em andamento e L5 não foi validada. Nenhum asset alterado nesta revisão.

## GIF frontal recebido — 10/11/2026

Publicado [Idle S v1 GIF](animacoes/louis-idle-s-v1.gif), enviado pelo usuário como `idle_front_8frames(1).gif`, sem alterar seus bytes. Dimensões 362 × 543 px, oito frames, 120 ms/quadro, ciclo de 960 ms. [Registro](animacoes/louis-idle-s-v1.md) e [metadados](animacoes/louis-idle-s-v1.json). Agora S/N/E/W possuem GIFs incorporados ao README. Folha frontal original preservada em referencias/. Timing medido no GIF recebido; integração em motor continua pendente.

## L3.1 — Arte Sudeste (SE) aprovada e congelada — 10/11/2026

[Arte SE v1](artes/louis-sudeste-parado-v1.png), [registro](artes/louis-sudeste-parado-v1.md), [metadados](artes/louis-sudeste-parado-v1.json) e [prompt literal](prompts/louis-sudeste-parado-v1.txt). Pose única em três quartos frente/direita, 1254 × 1254 px, RGB, fundo magenta opaco. Aprovação explícita: “arte aprovada. congele, documente e publique. atualize documentação e readme”. Original preservado sem edição, recorte ou redimensionamento; alterações exigem nova versão e aprovação.

Lado direito anatômico próximo, com ombro de couro, bolsa anterior direita, marca na bochecha, faixa e tira da coxa direitas; ombreira metálica única e adaga à esquerda anatômica, no lado distante, com projeção parcial e sobreposição. Usar esta arte como autoridade estática SE junto de Frente e Leste; costas v2 e Idle frontal são referências complementares. Superfícies intermediárias resultam de interpretação da rotação aprovada, sem definir um novo ângulo de câmera.

**L3.1 concluída.** Há 5/8 direções com arte estática e 4/8 com arte + Idle. Idle SE ainda não produzido; NE/NW/SW estáticos e as quatro animações diagonais continuam pendentes. Locomoção e integração em motor também pendentes. A próxima produção depende de instrução do usuário.

## L3.2 — Idle Sudeste (SE) aprovado e congelado — 10/11/2026

[Folha PNG](animacoes/louis-idle-se-v1.png), [GIF de validação aprovado](animacoes/louis-idle-se-v1.gif), [registro](animacoes/louis-idle-se-v1.md), [metadados e hashes](animacoes/louis-idle-se-v1.json) e [prompt literal](prompts/louis-idle-se-v1.txt).

Oito quadros em grade 4 × 2, folha 1448 × 1086 px, células 362 × 543 px; GIF de 120 ms/quadro, ciclo de 960 ms. Arte SE v1 congelada como autoridade de design; Idle frontal e Leste como referências de movimento. Aprovação explícita do usuário nesta conversa: “aprovado, publique no repositorio”. Preservar PNG e GIF aprovados sem alteração; mudanças exigem nova versão e aprovação. Fundo magenta opaco; timing de prévia. Ancoragem exata, transparência, atlas e validação no motor permanecem pendentes em L5.

**L3.2 concluída: 5/8 pares arte + Idle disponíveis (S/N/E/W/SE).** Faltam artes e Idles SW/NE/NW, além da locomoção nas oito direções. Aguardar instrução para a próxima produção.

## L3.3 — Arte Sudoeste (SW) aprovada e congelada — 10/11/2026

[Arte SW v1](artes/louis-sudoeste-parado-v1.png), [registro](artes/louis-sudoeste-parado-v1.md), [metadados e hash](artes/louis-sudoeste-parado-v1.json) e [prompt literal](prompts/louis-sudoeste-parado-v1.txt). Pose única em três quartos frente/esquerda, 1254 × 1254 px, RGB, fundo magenta opaco. Aprovação explícita do usuário: “aprovado! congele, publique usando github e atualize readme e documentação.” PNG original preservado integralmente, sem edição, recorte ou redimensionamento. Alterações exigem nova versão e aprovação.

Frente + Oeste são as autoridades principais; costas v2 e Idle frontal são referências complementares. Lado esquerdo anatômico próximo: ombreira prateada única e adaga anterior esquerda visíveis, com sobreposição pelo braço. Bolsa anterior direita no lado distante, com projeção parcial; faixa e tira da coxa direitas mantêm seus pontos de fixação. Sem espelhamento automático. As superfícies intermediárias são interpretações da rotação agora aprovada.

**L3.3 concluída: 6/8 artes estáticas e 5/8 pares arte + Idle (S/N/E/W/SE).** SW ainda não possui animação; NE/NW ainda precisam de arte + Idle. Próxima etapa proposta: **L3.4 — Idle SW + GIF de validação**, usando a arte SW aprovada e os Idles frontal/Oeste. Aguardar instrução para produzir. Locomoção e integração no motor permanecem pendentes.

## L3.4 — Idle Sudoeste (SW) aprovado e congelado — 10/11/2026

[Folha original PNG](animacoes/louis-idle-sw-v1.png), [GIF aprovado](animacoes/louis-idle-sw-v1.gif), [registro](animacoes/louis-idle-sw-v1.md), [metadados e hashes](animacoes/louis-idle-sw-v1.json) e [prompt literal](prompts/louis-idle-sw-v1.txt).

Aprovação explícita: “Aprovados! publique e atualize documentação + readme usando a conexão github”. PNG e GIF aprovados preservados sem alteração nesta publicação; mudanças exigem nova versão e aprovação. Arte SW v1 é a autoridade estática; Idle frontal e Oeste são referências de movimento. Assimetria e contrato de oclusão permanecem obrigatórios.

**Exceção de formato:** o prompt solicitou 1448 × 1086, mas a folha efetivamente gerada e aprovada mede **1491 × 1055 px**, oito quadros em disposição 4 × 2; os limites proporcionais arredondados produzem células de larguras 372/373 e alturas 527/528 px. Não tratar esta fonte como atlas regular de células 362 × 543. O GIF aprovado mede 362 × 543 px, oito frames, 120 ms/quadro e ciclo de 960 ms. Na composição anterior à aprovação, as células foram recortadas, o conteúdo recebeu um fator uniforme comum para altura máxima de 480 px e foi centralizado aproximadamente em x=183, com base y=496. Fundo magenta opaco. A folha original não foi redimensionada nesta publicação.

**L3.4 concluída: 6/8 pares arte + Idle (S/N/E/W/SE/SW).** Faltam NE e NW. Próxima etapa: **L3.5 — Arte estática NE**, conforme sequência de produção; aguardar instrução do usuário. Locomoção, transparência, atlas e validação em motor permanecem pendentes. Timing do GIF é de prévia.

## L3.5 — Arte Nordeste (NE) aprovada e congelada — 10/11/2026

[Arte NE v1](artes/louis-nordeste-parado-v1.png), [registro](artes/louis-nordeste-parado-v1.md), [metadados e hash](artes/louis-nordeste-parado-v1.json) e [prompt literal](prompts/louis-nordeste-parado-v1.txt). Pose única em três quartos costas/direita, 1254 × 1254 px, RGB, fundo magenta opaco. Aprovação explícita: “arte aprovada!congele e publique. atualize tbm as documentações + readme seguindo o nosso padrão.” PNG original preservado sem edição, recorte ou redimensionamento; alterações exigem nova versão e aprovação.

Costas v2 + Leste são as autoridades principais; arte frontal e Idle frontal são referências complementares. Lado direito anatômico próximo, ombro de couro; ombreira metálica única à esquerda anatômica, distante e parcialmente visível. Bolsa e adaga anteriores ocultas pelo corpo/casaco; faixa bordô lateral/posterior direita e tira da coxa preservadas. Correia posterior do ombro esquerdo ao quadril direito, sem fivela frontal nas costas. Superfícies intermediárias são interpretações da rotação agora aprovada, sem definir novo ângulo de câmera.

**L3.5 concluída: 7/8 artes estáticas e 6/8 pares arte + Idle (S/N/E/W/SE/SW).** Idle NE e arte + Idle NW pendentes. Próxima etapa proposta: **L3.6 — Idle NE + GIF de validação**, usando a arte NE aprovada e os Idles costas/Leste. Aguardar instrução para produzir. Locomoção, transparência, atlas e validação em motor permanecem pendentes.


## L3.6 — Idle Nordeste (NE): aprovado, originais recuperados; publicação binária pendente — 11/11/2026

A folha Idle NE e o GIF de validação foram recuperados dos artefatos da conversa de produção anterior e a aprovação explícita do usuário foi confirmada. **A conexão GitHub desta recuperação não permitiu transferir os bytes binários; os PNG/GIF NÃO estão publicados no repositório e L3.6 NÃO está concluída como publicação.** Não substituir por recriação nem anunciar o par como disponível no GitHub.

- Folha original `Louis em idle NE, vista traseira.png`: 1491 × 1055 px, RGB, 4 × 2 quadros, SHA-256 `41833a363dbf2d7b8d374f8b7ea8201b449899badb812079e180cd1ab6f2f95a`, 1.831.756 bytes. Destino previsto: `animacoes/louis-idle-ne-v1.png`.
- GIF original `louis-idle-ne-v1-validacao.gif`: 362 × 543 px, 8 quadros, 120 ms/quadro, 960 ms/ciclo, SHA-256 `fed66b13d2040550d393b72781d8797a9240664865c87acf816833f0ef10dceb`, 539.699 bytes. Destino previsto: `animacoes/louis-idle-ne-v1.gif`.
- Autoridade de design: `artes/louis-nordeste-parado-v1.png` (L3.5); referências de movimentação: Idle N e E. Assimetria e oclusão em `docs/oclusao-equipamentos.md`. Folha de tamanho excepcional: não presumir células regulares 362 × 543; preservar fonte sem redimensionar.
- Após transferência binária e verificação dos hashes, criar `animacoes/louis-idle-ne-v1.json`, `animacoes/louis-idle-ne-v1.md` e registrar prompt literal **somente se recuperado**. Atualizar inventário de **6/8 para 7/8 pares** apenas depois de confirmar os dois arquivos no GitHub. NW permanecerá pendente. Transparência, pivôs e teste em motor continuam em L5.
