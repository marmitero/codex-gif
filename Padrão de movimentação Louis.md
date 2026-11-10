# Padrão de movimentação Louis

Versão 1 — 10/11/2026. Referência: [Idle front Louis.png](referencias/Idle%20front%20Louis.png). Usar junto de [Arte Louis.md](Arte%20Louis.md).

## O que a folha demonstra

Oito poses frontais de repouso, em quatro colunas e duas linhas. Louis permanece com ambos os pés apoiados e separados; não existe deslocamento de caminhada, rotação significativa, ataque ou troca de apoio. Variações suaves na altura da cabeça/ombros, volume do tronco, braços e tecidos sugerem respiração e acomodação corporal. Cabelo, lenço e faixa acompanham com variações pequenas, sem vento forte. Rosto permanece reconhecível e olhos abertos; a fonte não demonstra uma piscada completa.

A leitura temporal proposta é esquerda→direita na primeira linha, depois esquerda→direita na segunda, voltando ao início. A imagem não contém números, metadados temporais ou prova de uma sequência original: essa ordem é uma convenção de produção adotada aqui.

## Composição e medidas

PNG RGBA de 1448 × 1086 px, totalmente opaco. Grade regular de 4 × 2 células, cada uma com 362 × 543 px, sem gutter adicional. Não há linhas desenhadas. Os espaços vazios pertencem às células e devem ser preservados. O personagem ocupa aproximadamente 176–179 px de largura e 477–489 px de altura. Centro horizontal do conteúdo próximo de x=183 local, ligeiramente à direita do centro matemático da célula (181).

Caixas aproximadas locais por exclusão do magenta (x e y começam em zero; limite máximo exclusivo):

| Quadro | Origem da célula | Caixa local x0,y0,x1,y1 | Altura | Margens E/D/T/B |
|---|---|---|---|---|
| 1 | 0,0 | 94,19,272,497 | 478 | 94/90/19/46 |
| 2 | 362,0 | 94,12,273,497 | 485 | 94/89/12/46 |
| 3 | 724,0 | 95,8,274,497 | 489 | 95/88/8/46 |
| 4 | 1086,0 | 95,14,273,497 | 483 | 95/89/14/46 |
| 5 | 0,543 | 94,17,272,497 | 480 | 94/90/17/46 |
| 6 | 362,543 | 94,20,271,497 | 477 | 94/91/20/46 |
| 7 | 724,543 | 95,19,271,497 | 478 | 95/91/19/46 |
| 8 | 1086,543 | 95,20,272,497 | 477 | 95/90/20/46 |

A base do conteúdo permanece em y=496 local, com limite exclusivo 497. O topo varia 12 px no conjunto; isso não mede isoladamente o deslocamento da cabeça, pois cabelo e silhueta também mudam. Não interpretar a diferença de altura como escala animada deliberada. O pico superior ocorre no quadro 3; os quadros 6–8 são mais baixos. Não presumir pares idênticos ou interpolação matemática.

O fundo predominante fica próximo de #FA0BF9, com variações. Não remover somente #FF00FF por igualdade exata. Os originais continuam intactos; uma futura versão transparente exigirá máscara cuidadosa para preservar olhos, lenço e faixa e evitar halo magenta.

## Movimento, ritmo e limites da inferência

A intenção aparente é um idle discreto e contínuo: expansão/elevação suave, retorno e acomodação. Pés ancorados, sem deslizar. A animação real ainda não foi validada em GIF ou motor nesta etapa. Um PNG estático não fornece FPS, duração, easing, ordem garantida ou qualidade do fechamento 8→1.

Recomendação inicial para teste futuro, não dado extraído: 100–150 ms por quadro (aproximadamente 6,7–10 FPS), ciclo de 0,8–1,2 s. Ajustar depois de visualizar o loop, sobretudo 8→1 e 5→6. Não congelar esse timing para corrida, ataque ou skills: cada ação exige ritmo próprio e marcação de antecipação, ação e recuperação.

## Contrato para próximas folhas

- Uma ação em uma direção por geração: por exemplo, Walk S e Walk SW são entregas distintas. Esta é a interpretação operacional de cada padrão possuir geração própria; não produzir as oito direções todas juntas sem nova instrução.
- Para ações de oito quadros, manter canvas 1448 × 1086, grade 4 × 2 e células 362 × 543, ordem de leitura acima e fundo magenta opaco semelhante à referência.
- Manter a escala visual do idle, base dos pés em y=496 e eixo de apoio próximo de x=183 quando a ação for no lugar. Pivô de integração proposto: (183,496), a validar com recortes e motor. Não recortar cada frame pelo conteúdo variável.
- Espaço horizontal livre atual é aproximadamente 90 px por lado; a folga superior mínima é apenas 8 px. Ataques, saltos ou armas elevadas podem ultrapassar a célula. Não cortar nem encolher o personagem para caber: se necessário, planejar canvas/células maiores uniformes antes de gerar e documentar a exceção.
- Oito quadros são o padrão demonstrado para idle, não garantia de que toda skill caberá em oito poses. Planejar qualquer exceção antes da produção.
- Manter cada quadro independente, sem sobreposição de células, títulos, rótulos, grades ou molduras. Movimento secundário deve preservar volume e quantidade dos acessórios.
- Para deslocamento, preferir animação no lugar e movimento controlado pelo motor; isso é recomendação de integração, não uma característica comprovada das ações ainda inexistentes.

## Oito direções e assimetria

Convenção de tela proposta: S=frente/baixo; SW=baixo-esquerda; W=esquerda; NW=cima-esquerda; N=costas/cima; NE=cima-direita; E=direita; SE=baixo-direita. Os nomes designam a tela, não coordenadas do mapa isométrico. Apenas Idle S tem referência recebida. A arte estática N (costas), v2, foi aprovada e congelada em 10/11/2026; a folha [Idle N v1](animacoes/louis-idle-n-v1.png) foi aprovada e congelada em 10/11/2026, com [registro e prévia](animacoes/louis-idle-n-v1.md). A arte estática E v1 também foi aprovada e congelada em 10/11/2026: [referência lateral](artes/louis-leste-parado-v1.png) e [registro](artes/louis-leste-parado-v1.md). [Idle E v1](animacoes/louis-idle-e-v1.png) aprovado e congelado em 10/11/2026, com [registro e GIF](animacoes/louis-idle-e-v1.md). As cinco direções restantes continuam sem arte aprovada. Preservar lateralidade anatômica em todas; não usar espelhamento simples para completar o conjunto. Não confundir oito quadros de uma ação com oito direções.

## Validação por entrega futura

Conferir fidelidade à arte, número e ordem dos quadros, grade, dimensões e fundo; detectar clipping, duplicações involuntárias e variação de escala. Verificar pés/pivô, trajetória de mãos/arma, integridade de rosto e equipamento e transição último→primeiro. Gerar prévia animada quando autorizada a produção; ataques não precisam fechar como um ciclo de caminhada. Registrar prompt efetivamente usado, referências, parâmetros disponíveis, alterações, timing e aprovação no repositório. O prompt original das imagens recebidas não foi fornecido e não deve ser reconstruído como fato.

## Regra posterior obrigatória — 10/11/2026

Aplicar [posição e oclusão dos equipamentos](docs/oclusao-equipamentos.md) em todas as gerações. Bolsa e adaga ficam na região anterior da cintura, preservando os lados anatômicos. Na vista de costas neutra ficam ocultas pelo corpo/casaco; nunca transferi-las para as costas. A v1 posterior errou essa profundidade; usar a [v2 corrigida e congelada](artes/louis-costas-parado-v2.png) como referência posterior oficial.
