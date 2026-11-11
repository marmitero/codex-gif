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

A intenção aparente é um idle discreto e contínuo: expansão/elevação suave, retorno e acomodação. Pés ancorados, sem deslizar. Na análise inicial da folha não havia prévia GIF. O GIF frontal enviado pelo usuário foi publicado posteriormente (ver registro abaixo); validação em motor permanece pendente. Um PNG estático não fornece FPS, duração, easing, ordem garantida ou qualidade do fechamento 8→1.

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

Convenção de tela proposta: S=frente/baixo; SW=baixo-esquerda; W=esquerda; NW=cima-esquerda; N=costas/cima; NE=cima-direita; E=direita; SE=baixo-direita. Os nomes designam a tela, não coordenadas do mapa isométrico. Apenas Idle S tem referência recebida. A arte estática N (costas), v2, foi aprovada e congelada em 10/11/2026; a folha [Idle N v1](animacoes/louis-idle-n-v1.png) foi aprovada e congelada em 10/11/2026, com [registro e prévia](animacoes/louis-idle-n-v1.md). A arte estática E v1 também foi aprovada e congelada em 10/11/2026: [referência lateral](artes/louis-leste-parado-v1.png) e [registro](artes/louis-leste-parado-v1.md). [Idle E v1](animacoes/louis-idle-e-v1.png) aprovado e congelado em 10/11/2026, com [registro e GIF](animacoes/louis-idle-e-v1.md). A arte estática W v1 foi aprovada e congelada em 10/11/2026; SE passou a ter arte aprovada em L3.1 (ver registro abaixo); NE/NW/SW continuam sem arte aprovada. [Idle W v1](animacoes/louis-idle-w-v1.png) aprovado, congelado e publicado com [GIF](animacoes/louis-idle-w-v1.gif) e [registro](animacoes/louis-idle-w-v1.md). Assim, S/N/E/W possuem arte + Idle; faltam as quatro diagonais. Preservar lateralidade anatômica em todas; não usar espelhamento simples para completar o conjunto. Não confundir oito quadros de uma ação com oito direções.

## Validação por entrega futura

Conferir fidelidade à arte, número e ordem dos quadros, grade, dimensões e fundo; detectar clipping, duplicações involuntárias e variação de escala. Verificar pés/pivô, trajetória de mãos/arma, integridade de rosto e equipamento e transição último→primeiro. Gerar prévia animada quando autorizada a produção; ataques não precisam fechar como um ciclo de caminhada. Registrar prompt efetivamente usado, referências, parâmetros disponíveis, alterações, timing e aprovação no repositório. O prompt original das imagens recebidas não foi fornecido e não deve ser reconstruído como fato.

## Regra posterior obrigatória — 10/11/2026

Aplicar [posição e oclusão dos equipamentos](docs/oclusao-equipamentos.md) em todas as gerações. Bolsa e adaga ficam na região anterior da cintura, preservando os lados anatômicos. Na vista de costas neutra ficam ocultas pelo corpo/casaco; nunca transferi-las para as costas. A v1 posterior errou essa profundidade; usar a [v2 corrigida e congelada](artes/louis-costas-parado-v2.png) como referência posterior oficial.

## Arte Oeste aprovada e congelada — 10/11/2026

[Louis Oeste parado v1](artes/louis-oeste-parado-v1.png): pose única olhando para a esquerda da tela (W), 1254 × 1254, RGB, fundo magenta opaco. Aprovada e congelada pelo usuário: “ficou boa! congele e publique. atualize os documentos do repositorio também.” PNG original e prompt literal preservados, sem recorte ou redimensionamento. [Registro](artes/louis-oeste-parado-v1.md), [metadados](artes/louis-oeste-parado-v1.json) e [prompt](prompts/louis-oeste-parado-v1.txt).

Lado esquerdo anatômico próximo: ombreira metálica única e adaga anterior esquerda visíveis, com sobreposição pelo braço. Bolsa anterior direita, faixa direita e tira da coxa direita ficam no lado distante, ocultas nesta pose; marca da bochecha direita não aparece. Não espelhar E para obter W. Esta arte é a autoridade estática para Idle W v1, junto das referências frontal, posterior v2 e E. Alterações exigem nova versão e aprovação. A etapa estática não produziu animação; o Idle W v1 foi publicado posteriormente. Validação em motor pendente; aguardar instrução para próxima produção.

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
