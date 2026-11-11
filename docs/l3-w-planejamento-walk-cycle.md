# L3.W — Planejamento do Walk Cycle de Louis

Data: 11/11/2026. Base documental: L3.9, commit a0dfacaddf0cb1c6f271b03888e540bcb0dc45b1.
Estado atualizado em11/11/2026:0/8 Walks aprovados; piloto E rig03 produzido para avaliação visual. Tentativas anteriores rejeitadas. Consultar [aprendizados e prompts](l3-w1-aprendizados-e-prompts.md) e [execução rig03](l3-w1-rig-03.md). Requisito do usuário: caminhar suave, 16 frames por direção (oito por passo), dimensões e identidade preservadas. Run fica para uma fase futura.

## Autoridades e preparação

Ler [arte](../Arte%20Louis.md), [movimento](../Padr%C3%A3o%20de%20movimenta%C3%A7%C3%A3o%20Louis.md), [oclusão](oclusao-equipamentos.md) e [conferência L3.9](l3-9-conferencia-oito-direcoes.md). Antes de cada geração, abrir visualmente arte frontal + folha frontal originais, costas v2, arte estática e Idle da direção escolhida; consultar também as vistas vizinhas. Os links exatos estão no inventário L3.9. O Idle fornece escala e design, não poses de caminhada.

Preservar proporções chibi, cabeça/corpo, comprimentos dos membros, volumes, paleta, câmera e acabamento pixelado. Não criar nova arte estática para substituir referências aprovadas. Não espelhar direções. Originais e exceções SW/NE/NW permanecem intactos.

## Contrato de movimento

Um ciclo completo tem dois passos alternados e 16 desenhos temporais distintos. Frames 1–8 cobrem o primeiro passo; 9–16, o segundo. O contato seguinte seria o frame 17, equivalente ao 1, e não é exportado. Não duplicar o 1 no 16; não produzir oito poses repetidas, ping-pong, morph ou mera translação de recortes.

Caminhada relaxada, passada moderada, tronco próximo da vertical, flexão suave dos joelhos e transferência de peso legível. Sempre pelo menos um pé em apoio; incluir dupla sustentação nos contatos. Sem fase aérea, arrancada, inclinação de sprint ou balanço exagerado. Fluidez depende de trajetórias e espaçamento coerentes, não só de quantidade de frames.

| Frame | Função | Corpo e apoios |
|---|---|---|
| 01 | Contato A | Pé esquerdo anatômico à frente; direito atrás; braço direito à frente |
| 02 | Transferência A | Receber peso; início da flexão; pé traseiro prepara saída |
| 03 | Down A | Compressão suave sobre a perna esquerda; pé direito libera |
| 04 | Saída A | Perna direita avança; apoio esquerdo contínuo |
| 05 | Passing A | Perna direita passa pela esquerda; joelho flexionado; equilíbrio sobre apoio |
| 06 | Elevação A | Corpo sobe discretamente; pé livre progride em arco |
| 07 | Up A | Calcanhar de apoio eleva; pé direito prepara contato |
| 08 | Aproximação B | Descida controlada; desacelerar balanço sem pausa |
| 09 | Contato B | Pé direito à frente; esquerdo atrás; braço esquerdo à frente |
| 10 | Transferência B | Receber peso no lado direito |
| 11 | Down B | Compressão suave; pé esquerdo libera |
| 12 | Saída B | Perna esquerda avança; apoio direito contínuo |
| 13 | Passing B | Perna esquerda passa pela direita |
| 14 | Elevação B | Corpo sobe discretamente; pé livre progride |
| 15 | Up B | Preparar contato esquerdo |
| 16 | Aproximação A | Preparar retorno contínuo ao 01 |

A numeração é comum às oito direções e usa lados anatômicos. A metade B inverte a função dos membros, mas preserva acessórios assimétricos. Visibilidade dos pés depende da câmera; marcar apoios mesmo quando ocultos. O retorno 16→1 deve preservar posição, velocidade aparente e continuidade dos tecidos.

## Corpo inteiro e movimento secundário

- Pernas/pés: flexão de quadril, joelho e tornozelo; transferência calcanhar→planta→ponta quando legível nas botas; arco baixo do pé em balanço, sem arrastar nem atravessar o outro membro.
- Cintura/pelve: rotação pequena e deslocamento lateral sobre o apoio; subida/descida discretas. Torso contrarrotaciona suavemente. Não esticar/encolher o corpo para simular peso.
- Ombros/braços/mãos: braço oposto à perna dianteira, arcos contínuos; cotovelos relaxados, punhos e dedos conservam anatomia e luvas. Ombreira acompanha o ombro como peça rígida, sem derreter.
- Cabeça: estável e reconhecível, acompanhando o corpo sem balanço brusco; cabelo responde discretamente.
- Roupa: mangas, abas do casaco, lenço e faixa acompanham aceleração e reversão com atraso pequeno, inicialmente de até 1–2 frames a avaliar visualmente. Nada de vento forte ou deslocamento igual em todas as peças.
- Equipamentos: cinto/correia ligados ao torso e à pelve, bolsa e bainha com oscilação curta coerente com fixação e peso. Adaga permanece embainhada. Sem colisões com mãos, pernas ou casaco.

## Oclusão dinâmica por quadro

Aplicar integralmente o contrato existente: ombreira e adaga à esquerda anatômica; bolsa, faixa e tira da coxa à direita. Bolsa e adaga são anteriores. N usa costas v2; não deslocar itens para trás para torná-los visíveis. NE/NW mantêm predominante ocultação; só mostrar trechos realmente expostos pela pose. E/W precisam de máscaras e alternância de profundidade coerentes para braços/pernas e equipamentos; uma ordem global fixa não basta. S/SE/SW também exigem revisão das sobreposições.

Registrar por frame: pé de apoio, membro próximo/distante, braço à frente/atrás do tronco, itens ocultos e justificativa de mudanças de visibilidade. Não impor desaparecimento total de item em toda pose só porque ele está oculto no repouso; tampouco fazê-lo aparecer sem mudança geométrica plausível.

## Escala, canvas e organização

Formato planejado: célula **362 × 543 px**, grade **4 × 4**, folha **1448 × 2172 px**, 16 frames em leitura por linhas. Fundo magenta opaco, sem textos, grades ou molduras. Cada direção tem sua folha e sua prévia.

Preservar escala visual do Idle: referência frontal com altura aproximada de 477–489 px e largura de 176–179 px em repouso. Essas medidas não são uma caixa obrigatória para todas as poses/direções; largura projetada e altura aparente podem variar com articulação, nunca por redimensionamento independente dos frames. Comparar cabeça, tronco e segmentos rígidos por sobreposição à referência, usando transformação de escala única documentada quando a fonte estática é maior que a célula.

Âncora de referência proposta (183,496), ainda não validada em motor. Ela representa origem de chão/raiz, não obrigação de manter ambos os pés em y=496 durante toda a caminhada. Pé livre sobe; em diagonais, projeção de profundidade altera sua coordenada vertical. Não recentralizar automaticamente pela caixa variável de cada pose.

A margem superior do Idle chega a apenas 8 px: verificar envelope de movimento antes da folha final. Se houver clipping, ampliar todas as células uniformemente com padding e atualizar coordenadas/grade/metadados antes de produzir a versão final, mantendo a escala do personagem. Não encolher para caber. Se o gerador não fornecer a dimensão exata, preservar a fonte, documentar o formato real e montar uma folha derivada regular sem deformação ou normalização individual. Nunca declarar grade exata sem medir.

## Ritmo e integração futura

Proposta inicial de prévia: **80 ms/frame**, 16 frames, ciclo de **1280 ms** (12,5 frames/s; dois passos por ciclo). É decisão inicial do planejamento, não timing extraído do Idle nem aprovação final. Avaliar ritmo no piloto e ajustar após visualização, preservando 16 desenhos; mais frames não significam correr mais rápido. Não copiar automaticamente os 120 ms do Idle. GIF usa timing representável em centésimos de segundo.

Animação no lugar, origem estável, sem acumular deslocamento. O pé em apoio recua em relação à raiz para compensar o avanço futuro do personagem; não fixá-lo artificialmente na tela por toda a fase de apoio. Na prévia auxiliar com deslocamento/chão, verificar que o apoio permanece estável no mundo. Em L5, relacionar velocidade à distância de passada: velocidade = distância de ciclo / duração de ciclo, convertida às unidades do motor. Deslocamento diagonal deve preservar velocidade de mundo; câmera/isometria e motor continuam a definir. Não certificar ausência de deslizamento em jogo apenas pelo GIF no lugar.

## Roadmap executável

A nomenclatura L3.W continua a locomoção de L3 sem renumerar L4 (combate) ou L5 (integração). Cada direção é uma etapa com revisão interna de poses, ciclo completo, GIF e aprovação; não publicar como congelada antes da aprovação explícita.

| Etapa | Entrega | Referências principais | Estado |
|---|---|---|---|
| L3.W0 | Planejamento, contrato de 16 frames e roadmap | L3.9 + documentos existentes | Concluída nesta publicação documental |
| L3.W1 | Walk E piloto: 16 frames + GIF | Arte/Idle E + frente + costas v2 | Piloto rig03 produzido; avaliação visual pendente |
| L3.W2 | Walk W: 16 frames + GIF | Arte/Idle W + piloto aprovado | Pendente |
| L3.W3 | Walk S: 16 frames + GIF | Frente original + E/W aprovados | Pendente |
| L3.W4 | Walk N: 16 frames + GIF | Costas v2 + Idle N + E/W | Pendente |
| L3.W5 | Walk SE: 16 frames + GIF | Arte/Idle SE + Walk S/E | Pendente |
| L3.W6 | Walk SW: 16 frames + GIF | Arte/Idle SW + Walk S/W | Pendente |
| L3.W7 | Walk NE: 16 frames + GIF | Arte/Idle NE + Walk N/E | Pendente |
| L3.W8 | Walk NW: 16 frames + GIF | Arte/Idle NW + Walk N/W | Pendente |
| L3.W9 | Conferência das oito direções, 128 frames e oito loops | Todas as entregas aprovadas | Pendente |

E é o piloto porque o perfil expõe a mecânica das pernas e os arcos dos braços. W valida a assimetria sem espelhamento; cardeais aprovadas sustentam as diagonais. Antes de cada direção: abrir imagens, marcar contatos/down/passing/up, revisar escala/envelope e profundidade, completar intermediários e secundários, medir arquivos, revisar GIF normal e lento e apresentar para aprovação. Ao aprovar: congelar e publicar PNG/GIF/MD/JSON/prompt literal; atualizar README, roadmap e state.ai. Seguir uma direção por vez, como no contrato do repositório.

## Entregáveis e aceitação

Caminhos de cada direção: `animacoes/louis-walk-<direcao>-v1.png`, `.gif`, `.md` e `.json`; prompt efetivamente usado em `prompts/louis-walk-<direcao>-v1.txt`. Se houver fonte irregular ou arquivos de trabalho, registrar sua procedência e o vínculo com o derivado aprovado. Não inventar prompts ausentes.

JSON deve registrar ação/direção/versão/estado, referências, dimensões reais, grade e retângulos de recorte, ordem 1–16, duração por frame/ciclo, âncora proposta, fases/apoios anatômicos, observações de oclusão, hashes SHA-256 e operações feitas. Registro Markdown contém prompt/referências utilizados, medições, ressalvas e aprovação literal. Nenhum asset foi gerado nesta etapa de planejamento.

Checklist por direção:
- 16 quadros distintos, dois passos, sem duplicação da pose de fechamento; 8→9 e 16→1 sem salto.
- Escala, volumes e detalhes conservados; nenhuma deformação temporal de rosto, mãos, botas ou equipamento.
- Apoio e transferência de peso legíveis; sem fase aérea; passada suave, sem aparência de Run.
- Braços, mãos, ombros, cintura, pernas e roupa participam; secundários discretos e coerentes.
- Oclusão revisada em todos os frames; sem troca de lado, interpenetração ou item atravessando o corpo.
- Sem cortes, sobreposição de células, serrilhado/halo novo ou cintilação de textura; revisar no tamanho nativo e ampliado.
- PNG/GIF decodificados integralmente; dimensões, recortes, ordem, timing e hashes conferidos; aprovação visual separada de integração em motor.

L3.W9 compara fase anatômica, cadência, escala e transições de direção em montagem de revisão, incluindo Idle↔Walk. Não acrescenta frames de transição aos 16 sem novo planejamento. README terá galeria Walk separada em duas colunas: S/N, E/W, SE/SW, NE/NW; GIFs a 240 px, clicáveis e proporcionais; pendências sem links a arquivos inexistentes. Encerramento: oito Walks aprovados com registros completos; Run continua futuro; transparência, atlas e teste real em L5.

## Fundamentação consultada

- [Autodesk — Animating a Freeform Walk Cycle](https://download.autodesk.com/us/3dsmax/2011/help/files/WS1a9193826455f5ff-e569a012180ce589112eb.htm): dois passos e poses contact/down/passing/up; apoio dos pés. Aplicamos esses princípios ao sprite 2D, sem adotar a contagem/timing do tutorial.
- [Blender — walkcycle usando NLA](https://docs.blender.org/api/htmlI/x8053.html): compatibilizar ciclo e deslocamento para evitar pés deslizando. Referência histórica conceitual, sem exigir Blender no pipeline.

A grade 4×4, a ordem do piloto, as marcações dos 16 frames e 80 ms/frame são propostas específicas para Louis. A exigência de 16 frames e caminhar suave vem do usuário. Avaliação visual futura decide o refinamento; esta documentação não certifica animação ainda inexistente.
