# L3.W1 — Rig04: auditoria de proporções e superfícies dos membros
Data: 11/11/2026. Estado: piloto produzido para avaliação visual; não congelado.

## Feedback e o que preservar
O usuário avaliou o rig03: “a movimentação em si ficou boa”, mas apontou membros desproporcionais e pediu verificar a face interna dos membros distantes. Isso é feedback positivo sobre o movimento, não aprovação final da arte. Preservamos16 instantes,80ms/quadro, fase dos dois passos, arco baixo, comprimentos articulares, apoio e movimento dos braços. Cabeça e tronco do rig03 foram mantidos byte a byte.

## O que falhou e causa identificada
A preparação anterior ajustava sobretudo a altura total de cada peça. Não verificava suficientemente largura, proporção interna bota/calça, alcance até os dedos e posição dos encaixes. Assim, peças de altura aceitável ainda produziam luvas/botas pequenas e excesso de tecido no joelho. Além disso, as peças distantes repetiam o dorso metálico da luva e a fivela externa da bota: posição atrás do corpo não corrige a superfície desenhada.

## Auditoria e calibração implementada
Autoridade: arte E v1 e Idle E v1 aprovados. Referência de apresentação: célula362×543 do Idle, principalmente quadro01 e conjunto das demais poses. Marcos de ombro/cotovelo/punho/dedos/joelho/tornozelo foram estimados visualmente na referência; pontos ocultos, como quadril, continuam propostas do rig. Não são reconstrução anatômica automática.

Procedimento obrigatório:
1. Manter cabeça/tronco fixos e chão/escala comuns; comparar o personagem em pose neutra antes do Walk.
2. Medir tanto comprimento quanto largura e sua relação com o núcleo corporal. Não normalizar peças apenas pela altura.
3. Medir a distância entre encaixe e fim da manga/mão, descontando a margem escondida de articulação. Caixas de pixels maiores não significam ossos maiores.
4. Usar escala uniforme por peça, calibrada uma vez. Sem esticar largura isoladamente, sem escala variável por quadro e sem recentralizar cada pose por sua silhueta.
5. Se a silhueta não atender, gerar nova arte; depois conferir as faces visíveis e os cruzamentos.
6. Reexecutar os controles de apoio e sequência após mudar as peças.

### Medições das peças preparadas
Dimensões de pixels antes da rotação; não são caixas variáveis das poses.

| Peça | Rig03 | Rig04 | Correção |
|---|---|---|---|
| Cabeça/tronco |156×330 |156×330 | Mesmo arquivo, hash conferido |
| Braço superior direito próximo |36×69 |42×69 | Volume da manga aproximado da referência |
| Braço superior esquerdo distante |35×69 |42×80 | Largura pareada e margem de encaixe escondida calibrada |
| Antebraço/luva direito |31×68 |37×78 | Alcance e tamanho da mão aumentados |
| Antebraço/luva esquerdo |30×68 |36×78 | Alcance aumentado e palma redesenhada |
| Coxa direita |55×104 |45×104 | Redução do excesso de volume |
| Coxa esquerda |52×104 |44×104 | Volume pareado; face interna sem tira |
| Canela/bota direita completa |61×107 |79×107 | Bota maior, cano/cuff e cap de joelho redistribuídos |
| Canela/bota esquerda completa |61×107 |79×107 | Mesmo porte; face medial sem fivela externa |

O braço distante tem80px de caixa porque inclui mais cap de encaixe escondido sob o tronco. Pivô emy=17, contra6 no próximo: em ambos, o intervalo ombro→fim da manga é63px. O osso superior continua57px nos dois lados; não alongamos o braço distante. A auditoria das peças alinha os pivôs para mostrar isso. O alcance distal até os dedos passou de cerca119 para129px em pose neutra (57+72), próximo dos127px estimados na referência. Esses números são calibração de apresentação, não novos limites canônicos de anatomia.

As estimativas de referência indicaram botas de cerca75–80px de largura e luvas na faixa aproximada35–42px, considerando pose e silhueta. Os alvos iniciais não foram tratados como medidas infalíveis: as larguras finais acima são as efetivamente produzidas. Uma primeira geração deixou o braço distante estreito e as coxas largas; foram refinados antes da montagem final.

## Superfícies interna e externa
Nesta câmera E e no movimento sem torção axial do rig:
- Direita próxima: manga externa, dorso da luva com placa metálica, coxa com uma tira, lado externo da bota com fivela.
- Esquerda distante: face medial da manga/cotovelo, palma da luva com pregas e polpas dos dedos, coxa com costura interna sem tira, face medial da bota com cuff liso e sem fivela externa. Biqueira metálica permanece porque não pertence apenas à face externa.
- As peças distantes foram geradas especificamente; não são cópias ou espelhamentos das externas. Não foram encolhidas artificialmente por profundidade.
- A maior parte do braço distante fica corretamente oculta: a auditoria de composição encontrou0–98 pixels visíveis por quadro, conforme limiar de alfa. Não deslocamos o membro para exibir a nova palma.
- Em outras vistas ou com pronação/supinação/torção, recalcular a superfície exposta; não impor “mostrar a palma” universalmente.

Também foi ajustada a separação de canela e pé: a porção da canela não deve carregar a parte superior da biqueira quando gira. O novo recorte de preparação usa sobreposição de7px na região do tornozelo, com o mesmo ponto lógico do tornozelo, reduzindo contornos duplicados na articulação.

## Prompt positivo atualizado
“Preservar a sequência e o rig de movimento que funcionaram. Usar a referência E para comprimento, largura, posição do cuff, mão e bota em relação à cabeça/tronco. Partes persistentes com escala uniforme fixa; encaixes e alcances medidos; volumes pareados entre lados. Mostrar a superfície medial correta dos membros distantes na câmera E: palma/parte interna da luva e face interna da bota, sem detalhes externos que ficam voltados para longe. Manter oclusão natural e articulações contínuas. Validar em pose neutra e depois em todos os16 quadros.”

## Prompt negativo atualizado
“Não corrigir proporção normalizando apenas altura. Não criar mãos ou botas pequenas, coxas infladas, dois caps de joelho, membros distantes fisicamente menores, manga alongada por encaixe mal posicionado ou biqueira duplicada pela canela. Não esticar peças horizontalmente nem mudar escala por quadro. Não copiar o dorso/placa da luva para a palma, nem a fivela externa para a face medial da bota. Não espelhar o pé para fazê-lo apontar para a esquerda. Não revelar membros ocultos à força. Não alterar câmera, corpo, cadência ou alternância para corrigir a arte.”

Prompts literais das duas gerações em [atlas de membros](../prompts/louis-walk-e-rig-04-membros.txt) e [refino](../prompts/louis-walk-e-rig-04-refino.txt). Os prompts são restrições de geração; as medidas finais vêm da auditoria, não do texto solicitado.

## Verificações do novo ciclo
16 quadros distintos; PNG/GIF decodificados integralmente; GIF362×543,80ms/quadro, ciclo1280ms; folha1448×2172. Comprimentos coxa88/canela76 constantes; erro numérico máximo5,7×10^-14px. Ao menos um apoio por quadro, dupla sustentação nos contatos; erro da sola de apoio contra o chão0px no render. Fases, estados de apoio, afastamento da sola e coordenadas horizontais do tornozelo comparados ao rig03: iguais. Altura/rotação da articulação são recalibradas para a nova silhueta da bota; não se afirma equivalência pixel a pixel entre as duas artes.

O pacote inclui comparação neutra referência/rig03/rig04, auditoria de faces com pivôs alinhados, conferência dos16 quadros, GIF normal/lento, PNGs individuais, fontes, JSON e compositor reproduzível. O núcleo corporal preservado foi conferido por SHA-256.

## Limites e estado
Movimento preservado como base bem recebida pelo usuário; proporções e novas peças continuam sujeitas à avaliação visual. Estes controles são cinemáticos e de apresentação2D, não simulação de forças ou garantia de deslizamento zero em motor. A regra de superfície é relativa à câmera e à pose. Artes/Idles congelados não foram sobrescritos; não congelar rig04 antes da aprovação explícita.
