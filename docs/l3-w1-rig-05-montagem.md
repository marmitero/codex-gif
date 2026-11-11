# L3.W1 — Rig05: correção da montagem e do vínculo de proporções
11/11/2026. Piloto para avaliação visual; sem congelamento.

## Diagnóstico
O usuário continuou percebendo braços e pernas pequenos em relação ao corpo e indicou possível erro de montagem. **Não houve nova geração de imagens nesta revisão.** Cabeça/tronco e os dois atlas de origem do rig04 foram reaproveitados sem alteração, com SHA-256 conferido. O ajuste ocorreu no compositor: geometria de repouso, pivôs, alcance e mapeamento entre a pintura das peças e as articulações.

A auditoria04 acertou ao corrigir faces internas e volumes de algumas peças, mas não demonstrava que o encaixe no corpo estava correto. A altura da caixa da peça, o comprimento do osso e a parte escondida sob o corpo são medidas diferentes. O rig ainda usava quadril emy=313 e coxa88 como parâmetros herdados; isso não foi recalculado com os marcos visíveis. O resultado também deixava a faixa da coxa alta em relação à referência.

## Referências e método
Autoridades: arte estática E v1 e Idle E v1 aprovados. Comparação de apresentação na mesma célula362×543, chão e pose neutra, sem redimensionar o personagem inteiro para fazer as silhuetas coincidirem. O Idle01 serve como fixture de comparação; as outras poses conservam a família de escala.

Marcos visíveis: bordas da faixa da coxa, posição do joelho/boot cuff, tornozelo/sola e extremidade dos dedos. Pontos ocultos, como o centro do quadril, são parâmetros inferidos de montagem e não medidas anatômicas diretamente observáveis. Foram usados para manter os marcos pintados próximos da referência, sem vender uma precisão3D inexistente.

Foram separados três controles:
1. Escala de apresentação do corpo: núcleo156×330 preservado byte a byte.
2. Geometria física do rig: comprimento entre pivôs e posição do quadril, sem depender da caixa alfa da pintura.
3. Vínculo da peça ao osso: margens escondidas, posição da faixa e do joelho na pintura, largura projetada e alcance até os dedos.

## Ajustes implementados
| Parâmetro | Rig04 | Rig05 |
|---|---|---|
| Quadril do rig, repouso |y=313 |y=299, inferido na calibração |
| Coxa entre articulações |88px |102px |
| Canela entre articulações |76px |76px |
| Braço superior próximo, pintura preparada |42×69 |47×76 |
| Braço superior distante, pintura preparada |42×80 |47×88 |
| Antebraço/mão próximo |37×78 |40×84 |
| Antebraço/mão distante |36×78 |39×84 |
| Coxa próxima, arquivo preparado |45×104 |52×112, incluindo margem transparente do pivô |
| Coxa distante, arquivo preparado |44×104 |51×112, incluindo margem transparente do pivô |
| Canelas/botas |79×107 |79×107, reaproveitadas |

Os ombros continuam no mesmo lugar e os ossos superiores dos braços continuam57px. As mangas receberam mais volume, com pivôs ajustados para conservar63px entre o ombro e o fim da manga. O alcance distal da mão aumentou; não se empurrou o braço inteiro para fora do corpo.

A coxa ganhou um pivô acima do início dos pixels pintados. Assim, o trecho escondido participa da alavanca e do comprimento do membro. O quadril subiu14px e o comprimento da coxa cresceu14px, mantendo o joelho próximo de sua faixa de referência e o chão fixo. Isso não exige aumentar a altura total do personagem.

### Calibração da pintura da coxa
Na peça em repouso, as bordas da faixa foram localizadas por inspeção e contraste de cor, nas linhas35/46. A montagem agora mapeia os marcos verticais:
- origem pintada0 → distância13 do pivô;
- borda35 → distância54;
- borda46 → distância66;
- encaixe de joelho95 → distância102;
- fim104 → distância111.

É um remapeamento fixo da malha de repouso, igual nas duas pernas. A coxa distante mantém a costura medial e continua sem faixa. O algoritmo não recentraliza a peça por quadro.

**Mudança de método explícita:** esta revisão usa transformações2D fixas de preparação, inclusive fatores X/Y diferentes e um remapeamento por marcos na coxa. A normalização uniforme isolada usada antes foi insuficiente. Essas transformações são documentadas e constantes durante a animação; sua aparência precisa de avaliação visual. Não houve redesenho/inpainting nem novo prompt de imagem.

## Medidas da comparação neutra
| Marco de apresentação | Referência Idle E01 | Rig04 | Rig05 |
|---|---|---|---|
| Centro da região brilhante da faixa |y=359,5 |y=345,5 |y=357,5 |
| Erro da faixa |— |14px acima |2px acima |
| Última linha de pele dos dedos próximos |y=341 |y=338 |y=343 |
| Erro do alcance da mão |— |3px curto |2px além |

A faixa usa uma máscara de cor em região conhecida; os dedos do rig são isolados na camada da mão para não confundir a faixa com pele. São fixtures de apresentação2D, não um detector anatômico universal. As regiões, limiares e resultados estão em JSON e no validador reproduzível. Não se conclui proporção perfeita apenas por esses dois indicadores.

A comparação mostra referência, rig04 e rig05 lado a lado, todos em pose neutra. As botas não foram aumentadas indiscriminadamente: sua largura já estava próxima da referência; a correção principal foi no vínculo das pernas e no alcance/volume dos braços.

## Movimento e superfícies preservados
16 instantes, dois passos,80ms/quadro e1280ms/ciclo. Mesmas fases, estados de apoio, percurso horizontal dos tornozelos e afastamento da sola em relação ao rig04. A cinemática vertical do joelho muda por causa do quadril/comprimento recalibrados. Braços em contrafase, tecido com atraso discreto e fechamento16→01 mantidos como base.

As faces mediais do rig04 foram preservadas: palma no membro distante, bota interna sem fivela externa, coxa distante sem tira. Não houve espelhamento ou repetição do membro externo. A visibilidade segue a oclusão natural do corpo; o braço distante pode ficar quase todo escondido.

Verificações:16 quadros distintos; ao menos um apoio por quadro; erro da sola de apoio0px no render; comprimentos constantes, erro numérico máximo7,2×10^-14px; núcleo e atlas originais idênticos aos do rig04. Folha1448×2172, células362×543, prévias normal e lenta e PNGs individuais. A folha de conferência expõe os pivôs e as cadeias articulares para inspeção.

## Aprendizados para as próximas montagens
Positivo: calibrar a pose de repouso na mesma escala do corpo; vincular pixels a marcos e articulações; manter margens escondidas no cálculo; comparar alcance da mão, faixa, joelho e sola antes do ciclo; auditar medidas e aparência separadamente.

Negativo: não gerar novas peças automaticamente quando a falha é de montagem; não tratar a altura da caixa alfa como comprimento anatômico; não usar só largura de peças ou constância dos ossos como prova de proporção; não aumentar tudo indiscriminadamente; não compensar encaixe ruim movendo membros para ficarem visíveis; não aplicar escalas diferentes a cada quadro.

O pacote inclui fontes reutilizadas, compositor, calibração, validadores, baseline04, referência de comparação, folha/GIFs,16 PNGs e JSONs. Artes/Idles oficiais preservados. Rig05 segue sujeito à avaliação visual; não é simulação de forças nem certificação de deslizamento zero em motor.
