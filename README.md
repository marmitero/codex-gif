# Louis · Arte e animação

Referências e produção de sprites para MMO RPG 2D isométrico, com identidade visual congelada e objetivo de oito direções.

**4 de 4 direções cardeais com arte + Idle disponíveis** · **5 de 8 artes estáticas · 5 de 8 pares arte + Idle**
Conferência do inventário e dos registros em **10/11/2026**, considerando as referências originais como a direção frontal (S).

## Inventário por direção

| Direção de tela | Arte estática oficial | Folha Idle · 8 quadros | Registro / situação |
|---|---|---|---|
| **S · Frente** | [Arte frontal congelada](referencias/arte%20congelada%20Louis.png) | [Idle frontal original](referencias/Idle%20front%20Louis.png) | Referências recebidas e preservadas; [arte](Arte%20Louis.md) e [movimento](Padr%C3%A3o%20de%20movimenta%C3%A7%C3%A3o%20Louis.md) |
| **N · Costas** | [Costas parada v2](artes/louis-costas-parado-v2.png) | [Idle N v1](animacoes/louis-idle-n-v1.png) | Aprovados e congelados · [arte](artes/louis-costas-parado-v2.md) · [Idle](animacoes/louis-idle-n-v1.md) |
| **E · Leste / direita** | [Leste parado v1](artes/louis-leste-parado-v1.png) | [Idle E v1](animacoes/louis-idle-e-v1.png) | Aprovados e congelados · [arte](artes/louis-leste-parado-v1.md) · [Idle](animacoes/louis-idle-e-v1.md) |
| **W · Oeste / esquerda** | [Oeste parado v1](artes/louis-oeste-parado-v1.png) | [Idle W v1](animacoes/louis-idle-w-v1.png) | Aprovados e congelados · [arte](artes/louis-oeste-parado-v1.md) · [Idle](animacoes/louis-idle-w-v1.md) |
| **SE · Sudeste / frente-direita** | [Sudeste parado v1](artes/louis-sudeste-parado-v1.png) | [Idle SE v1](animacoes/louis-idle-se-v1.png) | Arte e Idle aprovados e congelados · [L3.1](artes/louis-sudeste-parado-v1.md) · [L3.2](animacoes/louis-idle-se-v1.md) |

“Completo” nesta conferência significa **um par de arte estática + folha Idle por direção cardinal**. **SE** possui arte e Idle aprovados e congelados (L3.1/L3.2). **NE, NW e SW** ainda não possuem arte estática aprovada. Faltam os pares arte + Idle de NE/NW/SW. Oito quadros de animação não significam oito direções.

## Galeria de Idle

As quatro direções cardeais e SE possuem GIFs publicados e são exibidas abaixo. O GIF frontal foi enviado pelo usuário em 10/11/2026 e preservado sem alteração; [registro e procedência](animacoes/louis-idle-s-v1.md).

<table>
<tr><th>Frente · S — GIF</th><th>Costas · N — GIF</th></tr>
<tr>
<td align="center"><a href="animacoes/louis-idle-s-v1.gif"><img src="animacoes/louis-idle-s-v1.gif" alt="Louis em Idle de frente" width="240"></a></td>
<td align="center"><a href="animacoes/louis-idle-n-v1.gif"><img src="animacoes/louis-idle-n-v1.gif" alt="Louis em Idle de costas" width="240"></a></td>
</tr>
<tr><th>Leste · E — GIF</th><th>Oeste · W — GIF</th></tr>
<tr>
<td align="center"><a href="animacoes/louis-idle-e-v1.gif"><img src="animacoes/louis-idle-e-v1.gif" alt="Louis em Idle olhando para a direita" width="240"></a></td>
<td align="center"><a href="animacoes/louis-idle-w-v1.gif"><img src="animacoes/louis-idle-w-v1.gif" alt="Louis em Idle olhando para a esquerda" width="240"></a></td>
</tr>
</table>

<p align="center"><a href="animacoes/louis-idle-se-v1.gif"><img src="animacoes/louis-idle-se-v1.gif" alt="Louis em Idle Sudeste SE aprovado" width="240"></a><br>Sudeste · SE — L3.2 aprovada e congelada</p>

[Baixar GIF S](animacoes/louis-idle-s-v1.gif) · [Baixar GIF N](animacoes/louis-idle-n-v1.gif) · [Baixar GIF E](animacoes/louis-idle-e-v1.gif) · [Baixar GIF W](animacoes/louis-idle-w-v1.gif)

## Galeria de artes congeladas

| Frente · S | Costas · N (v2) |
|:---:|:---:|
| <img src="referencias/arte%20congelada%20Louis.png" alt="Arte frontal congelada" width="260"> | <img src="artes/louis-costas-parado-v2.png" alt="Arte posterior v2 congelada" width="260"> |
| **Leste · E** | **Oeste · W** |
| <img src="artes/louis-leste-parado-v1.png" alt="Arte Leste congelada" width="260"> | <img src="artes/louis-oeste-parado-v1.png" alt="Arte Oeste congelada" width="260"> |

<p align="center"><a href="artes/louis-sudeste-parado-v1.png"><img src="artes/louis-sudeste-parado-v1.png" alt="Louis Sudeste SE — arte estática congelada L3.1" width="300"></a><br>Sudeste · SE — L3.1 aprovada e congelada</p>

## Especificações e uso

| Material | Especificação documentada |
|---|---|
| Artes estáticas oficiais | 1254 × 1254 px, pose única |
| Folhas Idle S / N / E / W / SE | 1448 × 1086 px, grade 4 × 2, oito quadros |
| Célula de animação | 362 × 543 px; leitura por linhas |
| GIFs S / N / E / W / SE | 120 ms/quadro, ciclo de 960 ms; prévias |
| Fundo | Magenta opaco com variações; fontes RGB ou RGBA com alfa opaco |
| Integração | Transparência, atlas, pivôs e validação em motor pendentes (L5) |

Aprovação visual e congelamento não certificam ancoragem exata nem integração no jogo. O timing dos GIFs é de prévia; o PNG frontal não fornece timing original. Preservar os originais: alterações exigem nova versão e aprovação.

**Assimetria obrigatória:** não espelhar E para obter W. Ombreira metálica e adaga pertencem ao lado esquerdo anatômico; bolsa, faixa e tira da coxa ao direito. Bolsa e adaga são anteriores e ficam ocultas na vista posterior neutra. Usar sempre a **arte posterior v2**; v1 é histórico superado. Consultar o [contrato de oclusão](docs/oclusao-equipamentos.md) e seu [JSON](docs/oclusao-equipamentos.json).

## Documentação e inventário

| Caminho | Conteúdo |
|---|---|
| [Arte Louis.md](Arte%20Louis.md) | Identidade, materiais, lateralidade, paleta e fidelidade |
| [Padrão de movimentação Louis.md](Padr%C3%A3o%20de%20movimenta%C3%A7%C3%A3o%20Louis.md) | Grade, oito quadros, ancoragem proposta e contrato de produção |
| [referencias/](referencias/) | Arte frontal e Idle frontal originais |
| [artes/](artes/) | Artes N v1 histórica / N v2 oficial / E v1 / W v1 / SE v1 e registros |
| [animacoes/](animacoes/) | Idle N / E / W / SE: PNG, GIF, registro Markdown e metadados JSON; GIF frontal S, registro e metadados (folha S em referencias/) |
| [prompts/](prompts/) | Prompts literais recuperados de N estático v1/v2, E estático/Idle e W / SE estáticos; Idle SE |
| [docs/](docs/) | Regra de oclusão em Markdown e contrato JSON |
| [analise/medicoes.json](analise/medicoes.json) | Dimensões, hashes e caixas das referências originais |
| [analise/medir.py](analise/medir.py) | Reprodução das medidas com Python, Pillow e NumPy |
| [roadmap.md](roadmap.md) | Etapas concluídas e pendentes |
| [state.ai](state.ai) | Estado e decisões para retomada |

**Procedência:** prompts literais dos Idles N e W não foram recuperados; os das referências recebidas não foram fornecidos. Essas lacunas não devem ser preenchidas com reconstruções apresentadas como originais. Metadados dos Idles: [S](animacoes/louis-idle-s-v1.json), [N](animacoes/louis-idle-n-v1.json), [E](animacoes/louis-idle-e-v1.json), [W](animacoes/louis-idle-w-v1.json), [SE](animacoes/louis-idle-se-v1.json).

## Próximas etapas

- **L3 em andamento:** L3.1 e L3.2 concluídas (arte + Idle SE); faltam artes NE/NW/SW, os três Idles diagonais e a locomoção nas oito direções.
- **L4 pendente:** ataques e skills, com ações a definir.
- **L5 pendente:** transparência, atlas, pivôs, metadados de integração e teste em motor.

A próxima ação/direção depende da instrução do usuário. Idle SE v1 aprovado, congelado e publicado em L3.2; [registro](animacoes/louis-idle-se-v1.md).
