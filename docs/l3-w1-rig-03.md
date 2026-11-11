# L3.W1 — Walk E piloto rig03
11/11/2026. **Nova execução apresentada para avaliação visual; não aprovada ou congelada.**

## Mudança de método
Os pilotos desenhados em folhas, blocos e pares não preservaram a sequência. As lições e prompts positivo/negativo estão na [retrospectiva](l3-w1-aprendizados-e-prompts.md). Nesta execução, image_gen integrado produziu arte de peças estáveis e um compositor de animação calculou16 instantes com o mesmo conjunto de membros. Não se trata de interpolar ou repetir oito poses da tentativa rejeitada.

Referências: arte E v1 e Idle E v1 aprovados, frente original e costas v2, regras de arte, movimento e oclusão existentes. O atlas é uma nova interpretação de preparação para animação; não substitui a arte congelada. O [prompt literal de geração do atlas](../prompts/louis-walk-e-rig-03-atlas.txt) foi preservado. O pacote entregue contém atlas original, peças, script, folhas, GIFs e JSON de cada quadro.

## Arte e preparação
Fonte RGBA transparente de1254×1254. Disposição aproximada3×3, não uma grade exata: o corpo ultrapassa o limite proporcional da primeira célula. Separação por componentes alfa e caixas medidas, não por recorte cego da grade. Nove peças: cabeça/tronco, dois braços superiores, dois antebraços/mãos, duas coxas e duas canelas/botas. Cada peça recebe uma única escala de preparação; essa escala não muda durante os16 quadros. O tornozelo usa sobreposição fixa entre canela e pé para permitir rolagem independente. Fonte original preservada.

## Contrato executado
- Uma coxa, uma canela e um pé por lado; tira apenas na coxa direita. Ordem distante→próximo fixa nos cruzamentos.
- Contato esquerdo no01; direito no09. Dupla sustentação nesses dois instantes. Restantes alternam um apoio e um membro livre.
- Apoio recua8,5px/quadro em relação ao quadril, percorrendo68px por passo. Pé livre avança uma única vez, com curva suave e arco baixo de até21px de afastamento da sola.
- Coxa88px e canela76px: comprimentos matemáticos constantes. Inversa de duas articulações resolve joelho para frente, com pé articulado separadamente.
- Rotação discreta do pé de cerca+4° no contato até−7° na saída. Sola de apoio alinhada emy=496; não elevar o corpo inteiro para fingir contato.
- Braços em contrafase com amplitude de17°, cotovelos relaxados; cabeça e tronco preservados; oscilação corporal de2px e lateral de1,2px. Tecido abaixo do cinto com deformação de até1,8px e atraso de um quadro.
- Formato362×543 por quadro, folha1448×2172 em4×4.80ms/quadro,1280ms/ciclo; versão lenta160ms/quadro.01 não é repetido no16.

## Verificações executadas
| Verificação | Resultado |
|---|---|
| Quadros com conteúdo distinto |16/16 |
| Decodificação PNG/GIF e timing | Completa; GIF16×80ms |
| Menor número de apoios por quadro |1; dois nos contatos01/09 |
| Maior erro da sola de apoio contra o chão no render |0px |
| Maior erro numérico nos comprimentos dos ossos |4,3×10^-14px, arredondamento de ponto flutuante |
| Avanço do pé livre nas duas metades | Monotônico em relação ao quadril |
| Cabeça redesenhada/pulsando entre quadros | Não: mesma peça e escala |
| Margens | Conteúdo dentro do canvas; topo18–22, base exclusiva496–497 |
| Ordem de profundidade | Esquerda distante e direita próxima persistentes |

O JSON registra hip/knee/ankle, estado de cada perna, rotação, afastamento da sola e medidas por quadro. A folha/GIF de conferência sobrepõe esqueleto e chão, permitindo comparar01–16 e16→01. Revisão visual interna dos cruzamentos e contatos realizada; aprovação do usuário continua pendente.

## Limites
Trata-se de **restrições cinemáticas**, não simulação de forças, equilíbrio dinâmico ou tecido físico. O pé de apoio recua em relação à raiz; sua rolagem muda o ponto da sola que toca o chão. Não foi certificado deslizamento zero no mundo ou em motor. Um passo68px a cada640ms sugere106,25px/s nessa escala, sujeito à calibração de motor/câmera em L5.

A composição em peças tem aparência diferente de uma animação totalmente redesenhada e pode requerer polimento nos encontros de joelho/tornozelo/ombro. A arte das peças, o ritmo e o acabamento precisam de avaliação visual. As verificações acima comprovam somente seus critérios específicos, não perfeição artística. Nenhum Walk oficial foi congelado; W e demais direções aguardam avaliação do piloto.
