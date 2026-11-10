# Arte Louis

Referência visual congelada — versão 1, 10/11/2026.

## Autoridade e uso

A fonte principal é [arte congelada Louis.png](referencias/arte%20congelada%20Louis.png). A folha [Idle front Louis.png](referencias/Idle%20front%20Louis.png) define a apresentação animada e deve ser consultada em conjunto com [Padrão de movimentação Louis.md](Padr%C3%A3o%20de%20movimenta%C3%A7%C3%A3o%20Louis.md). Os arquivos originais estão preservados sem alteração. Este documento descreve o que é visível; partes ocultas não constituem design aprovado.

## Identidade, silhueta e proporções

Louis é um jovem aventureiro humano de fantasia medieval, sem capacete, com aparência chibi de RPG e tratamento anime. Cabeça grande, olhos expressivos, tronco compacto, pernas relativamente curtas e botas largas. A altura visual equivale aproximadamente a três cabeças, dependendo de incluir o volume do cabelo. Postura frontal ereta, pés separados, braços relaxados junto ao corpo e mãos parcialmente fechadas. Expressão confiante e amistosa, sorriso pequeno; não é uma expressão agressiva.

A silhueta deve preservar cabelo muito volumoso e irregular, lenço largo, ombros assimétricos, bolsa lateral, tiras pendentes e botas robustas. Não afinar o personagem nem converter para proporções adultas realistas.

## Estilo de renderização

Pixel art ilustrativa detalhada: contornos escuros em degraus, massas de sombra bem marcadas, pequenos agrupamentos de pixels e brilho pontual em metal. A imagem apresenta variações finas de cor; não é comprovadamente um sprite de baixa resolução ampliado por fator inteiro nem uma paleta indexada estrita. Não inventar uma resolução lógica original. Reproduzir a aparência observada: bordas pixeladas, textura controlada e detalhes legíveis; evitar pintura lisa, 3D, vetorização e suavização excessiva.

Luz principal aparente superior/frontal, com reflexos claros no topo da ombreira e nas biqueiras, sombras sob cabelo, queixo, lenço, mangas e entre as pernas. Não há sombra projetada no chão nem cenário. O preto de contorno possui tons quentes muito escuros, não apenas preto uniforme.

## Inventário visual e lateralidade

Direita/esquerda anatômicas são sempre as de Louis. Na vista frontal, a direita anatômica aparece à esquerda da imagem.

| Região | Características congeladas |
|---|---|
| Cabelo | Castanho quase preto; mechas grossas pontudas, franja central longa entre os olhos, tufos para os lados e mechas curvas ascendentes no topo; reflexos cinza/castanho quentes. Sem barba, chapéu ou capacete. |
| Rosto | Pele clara quente/pêssego, olhos grandes avermelhados/castanho-avermelhados, pupilas e cílios escuros, sobrancelhas grossas inclinadas, nariz mínimo, sorriso discreto. Marca diagonal clara/rosada na bochecha direita anatômica, visível à esquerda da imagem; preservar sua aparência sem afirmar origem narrativa. |
| Pescoço | Lenço vermelho escuro/bordô envolvendo o pescoço, dobras sobrepostas, centro frontal triangular e sombras profundas. |
| Ombro direito | Cobertura de couro/tecido marrom em camadas, sem placa metálica equivalente à do outro lado. |
| Ombro esquerdo | Uma ombreira de metal cinza/prata com brilho claro, rebite circular próximo ao pescoço e borda inferior escura. Não duplicar. |
| Tronco | Casaco/colete marrom escuro aberto, lapelas e bordas bege/marrons, camisa creme com fechamento central e pequenos botões escuros. |
| Mangas | Mangas claras dobradas abaixo do cotovelo; antebraços parcialmente expostos. |
| Correia | Correia de couro diagonal: do ombro esquerdo anatômico para o quadril direito; fivela aproximadamente quadrada em losango no peito. |
| Cintura | Cinto largo marrom, fivela metálica retangular/quadrada central, passadores e pequenas peças de couro. |
| Quadril direito | Bolsa marrom retangular com aba, fecho e costuras; faixa de tecido bordô pendendo atrás/lateralmente, com ponta irregular. |
| Quadril esquerdo | Arma curta embainhada com partes metálicas visíveis e bainha marrom. Forma de adaga/espada curta; comprimento total e desenho oculto da lâmina não são confirmados. |
| Mãos | Luvas marrons sem dedos, punhos largos e aplicações metálicas cinza; dedos claros visíveis. |
| Pernas | Calças escuras largas com dobras; tira de couro na coxa direita anatômica; abas do casaco pendentes, mais longas à esquerda anatômica. |
| Botas | Couro marrom de cano médio, tiras, fivelas metálicas claras e biqueiras reforçadas cinza com brilho. |

## Medidas da fonte

| Propriedade | Valor |
|---|---|
| Arquivo | PNG RGBA, 1254 × 1254 px |
| Alfa | 255 em todos os pixels: imagem totalmente opaca |
| Caixa aproximada do personagem | x=396..854, y=11..1228; 459 × 1218 px |
| Margens aproximadas | esquerda 396, direita 399, topo 11, inferior 25 px |
| Fundo predominante | próximo de #FB03F9; há variações, não é #FF00FF uniforme |

A caixa foi obtida excluindo pixels com R>220, G<50, B>220. É uma medição aproximada do conteúdo, não um recorte aprovado. Coordenadas iniciam em zero e limites finais exclusivos constam no JSON técnico.

## Paleta de referência

Famílias visuais obrigatórias: cabelo carvão/castanho, couro marrom quente, creme nas mangas/camisa, bordô no lenço/faixa, pele pêssego, olhos vermelhos e metais prata envelhecida. Exemplos representativos extraídos por quantização do primeiro original: #030002 (contornos), #1F1715 (sombras), #3C2E29 e #4F403B (tons escuros), #43302A e #7D513B (couros), #A87D63 e #ECC099 (tons quentes/pele). São amostras aproximadas de agrupamentos, não uma tabela exata por material; a imagem é a autoridade para comparação de cores e metal. Não impor uma paleta reduzida que elimine os reflexos.

## Regras das próximas gerações

1. Usar sempre ambas as imagens originais como referência visual, além destes documentos. Texto sozinho não garante identidade.
2. Preservar rosto, corte de cabelo, volumes, cores, roupas, materiais e lateralidade de todos os acessórios.
3. Não espelhar automaticamente direções: ombreira, bolsa, arma, faixa, marca facial e correia são assimétricas.
4. Manter fundo magenta opaco e espaço suficiente para cabelo, pés, tecido e arma em todos os quadros.
5. Não acrescentar cenário, texto, números, molduras, efeitos luminosos ou equipamentos sem instrução.
6. Para costas e diagonais, derivar apenas o necessário da roupa existente e registrar o que for interpretação; a vista frontal não confirma o desenho das costas.
7. O destino é MMO RPG 2D isométrico com oito direções. As fontes atuais mostram frente quase ortogonal; não comprovam um ângulo isométrico específico. Validar a adaptação de câmera na primeira direção nova, preservando a identidade.

## Lista de validação visual

Comparar lado a lado: rosto/cabelo; proporção cabeça/corpo; olhos e marca; lenço; ombreira única; correia e fivela; bolsa, arma e faixa em seus lados; luvas e botas; contraste, contorno e densidade de detalhe. Rejeitar mudança de estética, membros extras, acessórios trocados, arma aparecendo/desaparecendo ou alterações de escala entre quadros.
