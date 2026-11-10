# Regra obrigatória: posição e oclusão dos equipamentos

Decisão do usuário em 2026-11-10. Vale para toda nova direção, pose e quadro.

## Sistema de referência

Coordenadas locais do personagem: +X = direita anatômica, +Y = frente do corpo, +Z = cabeça. As posições pertencem ao corpo; não à tela. Girar câmera/personagem muda a projeção e a visibilidade, nunca o ponto de fixação do item. Não espelhar automaticamente.

- Bolsa: quadril direito, posição anterolateral (+X,+Y).
- Adaga embainhada: quadril esquerdo, posição anterolateral (-X,+Y).
- Faixa bordô: lateral/posterior do quadril direito; não herda a ocultação da bolsa.
- Ombreira: ombro esquerdo. Correia, cinto e demais peças seguem seus próprios volumes.

## Contrato por direção

| Vista | Bolsa e adaga em repouso |
|---|---|
| S, frente | Visíveis conforme referência frontal congelada |
| SE / SW | Visibilidade parcial calculada pela silhueta e profundidade; lado distante pode ficar oculto |
| E / W | Perfil/espessura coerente com a fixação anterior; ocultar por corpo ou braço quando necessário |
| NE / NW | Predominantemente ocultas pelo corpo; apenas trecho que realmente ultrapasse a silhueta pode aparecer |
| N, costas | Praticamente invisíveis. Na pose neutra v2, totalmente ocultas pelo corpo/casaco |

Não transportar os itens para as costas para torná-los reconhecíveis. Não mostrar aba frontal da bolsa, cabo, guarda ou bainha através do corpo. Item oculto continua existindo no inventário visual. Em ataques, a adaga pode sair da bainha somente quando a ação exigir; avaliar a nova posição por quadro.

## Implementação técnica e revisão

Em um pipeline com geometria, projetar posições locais após a rotação e resolver superfícies por profundidade. Em composição 2D, usar máscaras de oclusão: `item_visivel = mascara_item AND NOT mascara_oclusores_mais_proximos`. Separar trechos quando uma peça passa por trás e pela frente; uma ordem global única de camadas não resolve todos os casos. Se a arte for gerada já achatada, esse contrato é uma restrição de prompt e uma revisão visual obrigatória, não um z-buffer automático.

Para cada entrega: conferir fixação anatômica, orientação da câmera, superfície vista, silhueta, profundidade e continuidade entre quadros. Rejeitar reposicionamento para manter item visível, transparência do corpo ou acessórios saltando de lado. Não impor percentual numérico de visibilidade sem geometria de referência.

Contrato legível por ferramentas: `oclusao-equipamentos.json`. Ele registra regras; não constitui validador automático de pixels.

## Cláusula obrigatória de prompt

“Preservar a fixação tridimensional dos equipamentos ao corpo. Bolsa no quadril anterior direito e adaga embainhada no quadril anterior esquerdo. Resolver a oclusão conforme câmera e pose: na vista posterior neutra, corpo e casaco ocultam ambas; não desenhá-las sobre as costas. Nas diagonais e perfis mostrar somente superfícies realmente expostas. A faixa bordô posterior/lateral direita é independente e pode continuar visível.”

## Referência posterior oficial

A [arte posterior v2](../artes/louis-costas-parado-v2.png) foi aprovada e congelada pelo usuário em 10/11/2026. É a autoridade visual da oclusão na pose N neutra. Preservar esta referência nas próximas gerações; v1 é apenas histórico superado.
