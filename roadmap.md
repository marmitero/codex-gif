# Roadmap Louis

Atualização: 11/11/2026 (L3.9 — conferência final concluída).

| Etapa | Escopo | Estado |
|---|---|---|
| L0 | Preservar fontes, analisar arte e idle; criar documentação e estado | Concluída |
| L1 | Receber escolha da próxima ação/direção; planejar poses e confirmar adaptação de câmera pela referência produzida | Concluída: arte posterior estática v2 aprovada e congelada em 10/11/2026 |
| L2 | Produzir e validar a primeira folha nova e sua prévia animada, registrando prompt real | Folha Idle N v1 aprovada, congelada e publicada com prévia GIF; prompt real não recuperado (lacuna documental) |
| L3 | Completar gradualmente idle e locomoção nas oito direções | Em andamento: L3.1–L3.9 concluídas; 8/8 artes e 8/8 pares arte + Idle (S/N/E/W/SE/SW/NE/NW); locomoção pendente |
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

> Os registros datados abaixo preservam o estado de cada publicação; o estado atual consta em L3.9 e no inventário.

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

## L3.6 — Idle Nordeste (NE) publicado e congelado — 11/11/2026

[Folha PNG](animacoes/louis-idle-ne-v1.png), [GIF aprovado](animacoes/louis-idle-ne-v1.gif), [registro](animacoes/louis-idle-ne-v1.md) e [metadados e hashes](animacoes/louis-idle-ne-v1.json) disponíveis. Binários enviados pelo usuário em `823a187` (“etapa manual”); hashes conferidos contra os originais recuperados. Folha RGB 1491 × 1055 px, oito quadros em disposição 4 × 2, com exceção de formato; GIF 362 × 543 px, oito frames de 120 ms, ciclo de 960 ms. Nenhum binário modificado nesta revisão. Prompt literal não recuperado; não inventar.

**Estado atual: 7/8 artes e 7/8 pares arte + Idle (S/N/E/W/SE/SW/NE).** Faltam arte e Idle NW. Próxima etapa proposta: **L3.7 — arte estática NW**, depois L3.8 — Idle NW + GIF, mediante instrução. Locomoção continua pendente em L3; transparência, atlas, pivôs e validação no motor em L5.

## Auditoria de integridade — 11/11/2026

[Relatório](docs/auditoria-integridade-2026-11-11.md) e [medições](analise/integridade.json). O commit manual restaurou o **PNG Oeste (W)**, que agora decodifica integralmente e corresponde ao hash previamente documentado. O PNG SW não mudou nesse commit e abre completo. Fontes preservadas; lacunas conhecidas e limites da revisão registrados no relatório.

## Organização das galerias — 11/11/2026

Regra de publicação: seguir o padrão obrigatório das galerias no README. Tabelas centralizadas de duas colunas; pares S/N, E/W, SE/SW, NE/NW; artes a 260 px e GIFs a 240 px, com proporção preservada e link para o original. Substituir a célula pendente ao publicar uma direção; não acrescentar prévias soltas ou duplicadas ao final do arquivo.

## L3.7 — Arte Noroeste (NW) aprovada e congelada — 11/11/2026

[Arte NW v1](artes/louis-noroeste-parado-v1.png), [registro](artes/louis-noroeste-parado-v1.md), [metadados e hash](artes/louis-noroeste-parado-v1.json) e [prompt literal](prompts/louis-noroeste-parado-v1.txt). Pose única em três quartos costas/esquerda, 1254 × 1254 px, RGB, fundo magenta opaco. Aprovação explícita: “arte aprovada! congele e publique. atualize também as documentações e readme.” PNG original preservado sem edição, recorte ou redimensionamento; alterações exigem nova versão e aprovação.

Costas v2 + Oeste são as autoridades principais; arte frontal e Idle frontal complementam identidade, proporções e renderização. Ombreira prateada única no lado esquerdo anatômico próximo; couro no ombro direito distante. Correia posterior do ombro esquerdo ao quadril direito, sem fivela frontal nas costas. Bolsa anterior direita e adaga anterior esquerda ocultas pelo corpo/casaco/braços; faixa bordô e tira da coxa mantidas à direita anatômica, com visibilidade independente. Superfícies intermediárias são interpretações da rotação agora aprovada. Não espelhar NE.

**Estado atual: 8/8 artes estáticas aprovadas e 7/8 pares arte + Idle.** Falta o Idle NW. Próxima etapa: **L3.8 — Idle NW + GIF de validação**, usando a arte NW aprovada e os Idles costas/Oeste, mediante instrução. Locomoção nas oito direções continua pendente em L3; transparência, atlas, pivôs e validação no motor em L5.

## L3.8 — Idle Noroeste (NW) aprovado e congelado — 11/11/2026

[Folha PNG](animacoes/louis-idle-nw-v1.png), [GIF aprovado](animacoes/louis-idle-nw-v1.gif), [registro](animacoes/louis-idle-nw-v1.md) e [metadados e hashes](animacoes/louis-idle-nw-v1.json) publicados. Binários enviados pelo usuário no commit `589e5d8` (“etapa manual 2”); registro e JSON completados em `8bf8bbe`. PNG e GIF preservados integralmente.

Folha RGB de **1491 × 1055 px**, oito quadros em disposição **4 × 2**, leitura por linhas. Exceção de formato: não é atlas regular de células 362 × 543. GIF de **362 × 543 px**, oito frames de **120 ms**, ciclo de **960 ms**, loop infinito. Decodificação integral e hashes registrados no JSON. Prompt literal não recuperado; não reconstruir como original.

Autoridade estática: arte NW v1; movimento: Idle N e Idle W. Respeitar assimetria e contrato de oclusão, sem espelhar NE. Ombreira prateada à esquerda anatômica próxima; bolsa e adaga anteriores predominantemente ocultas pelo corpo/casaco/braços; faixa e tira da coxa permanecem à direita anatômica.

**Estado atual: 8/8 artes estáticas e 8/8 pares arte + Idle (S/N/E/W/SE/SW/NE/NW).** O repouso nas oito direções está completo. **L3 permanece em andamento pela locomoção**; próxima ação/direção a definir mediante instrução do usuário. Transparência, atlas, pivôs e validação em motor permanecem pendentes em L5.

## L3.9 — Conferência final das oito direções — 11/11/2026

**Conferência concluída: 8/8 artes oficiais, 8/8 folhas Idle e 8/8 GIFs com registros disponíveis.** [Relatório final](docs/l3-9-conferencia-oito-direcoes.md) e [medições e hashes](analise/integridade-l3-9.json). Todos os 26 arquivos de imagem do repositório decodificam; 64 quadros GIF verificados; nenhuma divergência nos hashes registrados ou link local quebrado. Fontes aprovadas preservadas sem alteração.

SW/NE/NW conservam a exceção de formato 1491 × 1055; GIF S conserva o tratamento diferente da folha; fundo NE apresenta variações. Prompts literais dos Idles N/W/NE/NW continuam não recuperados. Conferência de repouso concluída; L3 geral continua em andamento pela locomoção. Transparência, atlas, pivôs e teste em motor permanecem em L5.
