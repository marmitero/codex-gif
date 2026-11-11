# L3.W1 — Aprendizados, prompts e nova execução
Data: 11/11/2026. Estado: tentativas anteriores rejeitadas; sem Walk aprovado. Esta retrospectiva complementa o [planejamento](l3-w-planejamento-walk-cycle.md).

## O que funcionou e os limites
| Acerto observado | Como conservar |
|---|---|
| Referências aprovadas preservam paleta, cabelo, rosto e identidade geral | Usar arte/Idle E, frente e costas v2 como autoridades, nunca uma tentativa rejeitada como novo design |
| Identificação direita próxima/esquerda distante tornou as trocas legíveis | Uma única tira na coxa direita; marcar joelho e tornozelo de cada lado do início ao fim |
| Separar poses tornou erros locais mais fáceis de encontrar | Revisar por quadro e também por pares adjacentes, incluindo fronteiras e fechamento |
| GIF normal/lento, fonte preservada, grade medida e metadados permitem auditoria | Conservar os dois timings e os recortes reais |
| Dezesseis imagens distintas e ausência de cortes | São verificações de arquivo, não prova de fluidez, física ou sucesso artístico |

## O que não funcionou
| Falha | Evidência nas tentativas | Mudança obrigatória |
|---|---|---|
| Perna troca de identidade | Tira migra/duplica; perna que deveria avançar volta a ficar atrás | Lados anatômicos persistentes; exatamente duas pernas; profundidade próxima/distante constante |
| Passo incompleto ou repetido | Pé fica atrás por muitos desenhos e salta à frente; intermediários quase repetidos | Pé livre percorre atrás → sob quadril → frente uma vez por passo |
| Saltos/apoio incerto | Algumas poses anteriores mostravam ambos os pés elevados | Apoio obrigatório; dupla sustentação nos contatos; nenhum voo |
| Recuo irregular de apoio | Pé para ou muda abruptamente entre quadros/blocos | Trajetória de apoio contínua e aproximadamente linear em relação à raiz |
| Variações entre blocos | Cabeça, tronco, pernas, bota/cano e estilo mudam | Mesmas referências e escala; verificar volumes e coordenadas, sem normalização por caixa de cada pose |
| Correção local destrói outro detalhe | Remover tira distante também eliminou cano/cuff de bota em algumas gerações | Correção precisa manter bota, sola, fivela e demais volumes |
| Guia/prompt não obedecido | Houve imagens bonitas que contrariavam as trajetórias solicitadas | Comparar resultado aos pontos, não tratar pedido textual como resultado comprovado |
| Avaliação técnica usada como substituto da animação | Contagem/hash/margens passaram, caminhada não | Validar anatomia, contato, arcos, velocidade e fechamento separadamente |
| Muitas regenerações com instruções longas não resolveram o ciclo | Persistiu inconsistência na revisão 02 | Reduzir a quantidade de poses por geração e tornar as restrições verificáveis |

## Prompt positivo reutilizável
“Louis em caminhada relaxada para a direita, perfil E constante. Exatamente duas pernas e dois braços com identidade anatômica persistente. Direita próxima com uma única tira na coxa; esquerda distante sem tira. Cada membro conserva comprimentos e volumes. Dois passos alternados em 16 instantes distintos: contato esquerdo no01, passagem direita no05, contato direito no09, passagem esquerda no13. Pelo menos um pé em apoio; contato inclui dupla sustentação. Apoio progride calcanhar/planta/ponta e recua continuamente em relação à raiz; pé livre descreve arco baixo, avançando uma única vez por passo. Flexão suave de joelho/tornozelo, centro de massa sobre o apoio, tronco quase vertical, braços contrários às pernas, pequena contrarrotação e tecido com atraso discreto. Mesma câmera, escala, paleta, rosto, roupa e equipamentos em todos os quadros; oclusão anatômica consistente. Transições contínuas, inclusive16→01.”

## Prompt negativo reutilizável
“Evitar salto, voo, hopping, corrida, inclinação de sprint, passada exagerada ou joelho alto. Evitar pernas/braços/pés/mãos extras, membros fundidos, perna trocando de lado, tira duplicada ou migrando. Evitar oito poses repetidas para preencher16, ping-pong, repetição de ação dentro do mesmo passo, pose01 duplicada no16, pé livre voltando para trás antes de completar avanço. Evitar apoio parado artificialmente na tela no ciclo no lugar, teletransporte, aceleração brusca, pés atravessando chão/corpo, interpenetração e deslizamento não compensado. Evitar mudança de câmera, cabeça pulsando, membros esticando, bota/cuff sumindo, redesenho de roupas, fivela ou equipamento saltando de lado, cintilação de textura. Não ocultar defeitos reduzindo velocidade ou recentralizando cada quadro pela silhueta.”

## Física: o que pode ser validado
O guia pode impor comprimentos articulares constantes, chão, trajetórias e alternância de apoio. A imagem achatada precisa ser conferida contra ele; mencionar física no prompt não executa uma simulação nem garante forças/contatos. Em prévia no lugar, o apoio recua para compensar a velocidade futura de mundo. Ausência de deslizamento em motor só pode ser validada na integração. Sem promessa de perfeição.

## Execução seguinte
Nova tentativa: pares de dois instantes com guia temporal comum, reduzindo a carga de poses de cada geração. Montagem preserva fontes, usa uma escala comum e registra operações. Verificação:16 quadros, lados persistentes, posição de cada pé, continuidade de cada par e de todas as fronteiras, volumes e equipamentos. Rejeitar qualquer falha que permaneça; não congelar uma animação por ter16 arquivos.

As tentativas 01 e02 foram rejeitadas pelo usuário. As artes e os Idles aprovados continuam congelados. O resultado da nova tentativa será registrado separadamente; esta publicação documental não aprova nenhum Walk.

## Resultado da execução seguinte: pares rejeitados e mudança para rig

Os oito pares foram gerados, mas o par01/02 antecipou o contato da perna direita e outros pares repetiram estados ou contrariaram as identidades do guia. Portanto, reduzir de quatro para duas poses por imagem também não foi suficiente. Não usar essas fontes como ciclo aprovado.

A nova produção mudou para **peças fixas + articulações e trajetórias calculadas**. O gerador de imagens produziu um atlas transparente de nove peças; um compositor de animação utiliza sempre as mesmas peças, com joelho e tornozelo articulados, lados fixos, braço oposto à perna, apoio e arco livre. Cabeça e tronco não são redesenhados por quadro. Pequena deformação abaixo do cinto acrescenta atraso ao tecido. As artes/Idles congelados não foram alterados.

Aprendizado positivo adicional: fixar identidade e volume em componentes persistentes; calcular a sequência antes de exportar; usar articulação independente do pé para não obrigar a bota a acompanhar a rotação inteira da canela. Aprendizado negativo adicional: não confundir um prompt de física com uma simulação; não usar um conjunto de poses independentes rejeitadas como animação; não aceitar a validação numérica do apoio sem conferir a aparência da articulação e da sola.

O [relatório do piloto rig03](l3-w1-rig-03.md) registra medições, verificações e limites. O novo piloto tem16 quadros e foi apresentado para avaliação visual; não está aprovado ou congelado.
