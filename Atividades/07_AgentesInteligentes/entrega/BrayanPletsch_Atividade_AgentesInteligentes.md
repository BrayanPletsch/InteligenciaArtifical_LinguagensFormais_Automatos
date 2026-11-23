# Atividade sobre agentes inteligentes

Aula 19/10/2026 | Professora Kadidja Valéria | Inteligência artificial

**Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos

**Estudante:** Brayan Aragão Pletsch (RGM 38473585) | **Turma:** Engenharia de Software - N1

Realize os exercícios 2.3, 2.4 e 2.5 do Capítulo 2 sobre agentes inteligentes. Analise a racionalidade, descreva ambientes de tarefa por meio do modelo PEAS e explique os conceitos com suas próprias palavras. Utilize o capítulo disponibilizado e justifique suas respostas.

**Modalidade sugerida:** individual com consulta. **Tempo estimado:** 2h30. **Prazo:** conforme orientação da professora.

## Preparação
Leia os tópicos sobre racionalidade, ambientes e estrutura dos agentes, especialmente a Seção 2.3.2.

## Exercício 2.3
Para cada afirmação, indique V ou F, justifique e forneça exemplo ou contraexemplo. Explicite as hipóteses utilizadas.

Em todos os itens uso a definição da Seção 2.2.1: um agente é racional quando, para cada sequência de percepções, escolhe a ação que se espera maximizar a medida de desempenho, dado o que percebeu até ali e o conhecimento prévio que tem.

### a. Um agente que detecta apenas informações parciais sobre o estado não pode ser perfeitamente racional.

- Julgamento: **F**
- Justificativa: Hipótese: "perfeitamente racional" no sentido do capítulo, que não exige onisciência. A própria definição de racionalidade é condicionada à sequência de percepções recebida, então ela já admite que o agente não sabe tudo sobre o estado. O que se cobra é que ele use bem a informação que tem e, quando compensar, faça ações para obter mais informação (a coleta de informações da Seção 2.2.2). A observabilidade parcial pode baixar o desempenho máximo que dá para atingir, mas o agente racional é comparado com o melhor que se consegue fazer com aquelas percepções.
- Exemplo ou contraexemplo: O aspirador da Figura 2.3 só percebe o quadrado em que está e se ali há sujeira. Ele não sabe se o outro quadrado está sujo. Mesmo assim, com as hipóteses da Seção 2.2.1 (1 ponto por quadrado limpo a cada passo, 1.000 passos, geografia conhecida, sem custo de movimento), o capítulo afirma que esse agente é racional.

### b. Existem ambientes de tarefa nos quais nenhum agente reativo puro pode comportar-se racionalmente.

- Julgamento: **V**
- Justificativa: Hipótese: "reativo puro" é o agente reativo simples da Seção 2.4.2, que decide só pela percepção atual e não guarda estado. Para a afirmação ser verdadeira basta um ambiente em que a mesma percepção apareça em duas situações que pedem ações diferentes, e em que só o histórico permita separar essas situações. Aí qualquer regra percepção → ação erra em pelo menos uma delas, e um agente com memória faz melhor.
- Exemplo ou contraexemplo: Mundo do aspirador com A e B, sensor de posição e de sujeira local, sujeira inicial desconhecida, ações Esquerda, Direita, Aspirar e NoOp, e medida com +1 por quadrado limpo por passo e -1 por movimento (é o caso do Exercício 2.10). A percepção [A, Limpo] aparece quando B ainda está sujo (o certo é ir para a Direita) e quando o próprio agente já limpou B (o certo é parar). Se a regra for Direita, depois de tudo limpo o agente fica indo e voltando e perde 1 ponto por passo até o fim. Se a regra for NoOp, quando começa em A limpo com B sujo ele nunca limpa B. Sortear entre as duas também desperdiça pontos em parte das vezes. Um agente que guarda "já vi B limpo" acerta nos dois casos, então tem desempenho esperado maior que qualquer reativo puro.

### c. Existe um ambiente de tarefa em que todo agente é racional.

- Julgamento: **V**
- Justificativa: "Existe" pede só um caso. Se todas as ações disponíveis levam ao mesmo desempenho esperado, qualquer escolha maximiza esse valor e qualquer agente é racional. O caso mais trivial é um ambiente com uma única ação possível. Hipótese: o conjunto de ações é o que o ambiente permite, e a medida é a que o projetista definiu.
- Exemplo ou contraexemplo: Par ou ímpar contra um adversário que sorteia um número de 0 a 5 com probabilidade igual, com medida "vitórias esperadas". Como o adversário tem três números pares e três ímpares, a soma sai par em 50% dos casos para qualquer número que o agente mostre e para qualquer lado que ele escolha. Todo agente tem a mesma chance de vencer, logo todos são racionais nesse ambiente.

### d. A entrada para o programa de agente é a mesma que a entrada para a função de agente.

- Julgamento: **F**
- Justificativa: Hipótese: a estrutura adotada na Seção 2.4.1, em que o programa recebe a percepção atual dos sensores e devolve uma ação. A função de agente é a descrição matemática e recebe a sequência completa de percepções. O programa recebe só a percepção do instante, porque é a única coisa que o ambiente entrega naquele momento. Se a ação depender do passado, o programa precisa guardar o histórico (ou um resumo dele) por conta própria.
- Exemplo ou contraexemplo: O AGENTE-DIRIGIDO-POR-TABELA da Figura 2.7 recebe uma percepção por chamada. É ele que anexa essa percepção à variável estática `percepções` e só então consulta a tabela, que é indexada pela sequência inteira. A entrada do programa é uma percepção; a entrada da função é a sequência.

### e. Toda função de agente é implementável por uma combinação de programa/máquina.

- Julgamento: **F**
- Justificativa: A função de agente é um objeto matemático, e nada impede definir uma que nenhum programa consiga calcular. Considero dois casos. Primeiro, com uma máquina idealizada (memória ilimitada), ainda existem funções não computáveis. Segundo, com uma arquitetura física, a memória é finita, e algumas funções exigem distinguir infinitos históricos diferentes.
- Exemplo ou contraexemplo: (1) Um agente cujas percepções são códigos-fonte de programas e que deve responder "termina" ou "não termina" corretamente para cada um. Implementar essa função seria resolver o problema da parada, que é indecidível. (2) Um agente que recebe percepções 0 ou 1 e, a cada passo, deve dizer se até agora recebeu a mesma quantidade de 0s e de 1s. Isso exige um contador sem limite. Uma máquina com n bits tem no máximo 2^n configurações, então depois de sequências longas o bastante ela confunde históricos que pedem respostas diferentes. É a mesma razão pela qual um autômato finito não reconhece esse tipo de linguagem.

### f. Suponha que um agente selecione sua ação uniformemente ao acaso do conjunto de ações possíveis. Existe um ambiente de tarefa determinista em que esse agente é racional.

- Julgamento: **V**
- Justificativa: Hipótese: ambiente determinístico no sentido do capítulo (estado atual + ação determinam o próximo estado). O capítulo diz que em ambientes de agente único a aleatoriedade em geral não é racional. "Em geral" deixa espaço para exceções: se todas as ações produzem o mesmo desempenho, sortear é tão bom quanto qualquer escolha.
- Exemplo ou contraexemplo: Mundo do aspirador com A e B em que os dois quadrados começam limpos, quadrados limpos continuam limpos e não há custo de movimento. É determinístico, e qualquer ação (Esquerda, Direita ou Aspirar) rende os mesmos 2 pontos por passo. O agente que sorteia atinge o máximo e é racional. Se houvesse sujeira inicial, o mesmo agente deixaria de ser racional, porque demoraria em média mais passos para limpar do que o agente da Figura 2.8.

### g. É possível para um dado agente ser perfeitamente racional em dois ambientes de tarefa distintos.

- Julgamento: **V**
- Justificativa: A racionalidade é sempre relativa a um ambiente de tarefa (medida, ambiente, atuadores e sensores). Nada impede que a mesma política seja a melhor em dois ambientes que diferem em algum desses elementos. Hipótese: considero ambientes distintos aqueles que mudam pelo menos um componente do PEAS ou da distribuição de estados iniciais.
- Exemplo ou contraexemplo: O aspirador reativo da Figura 2.8 é racional no ambiente da Seção 2.2.1 (1.000 passos). Também é racional se o tempo de vida for de 10.000 passos ou se a sujeira inicial seguir outra distribuição (por exemplo, B quase sempre começa sujo). O motivo é que, sem custo de movimento, ele aspira quando o quadrado está sujo e vai ao outro quadrado quando não está, o que limpa tudo no menor número de passos em qualquer configuração. Já com custo por movimento, o mesmo agente deixa de ser racional, como a própria Seção 2.2.1 comenta.

### h. Todo agente é racional em um ambiente não observável.

- Julgamento: **F**
- Justificativa: Hipótese: "não observável" no sentido do capítulo, o agente não tem sensores, mas pode ter conhecimento prévio do ambiente e das próprias ações. Sem percepções, o histórico não ajuda a decidir, mas as ações continuam tendo efeitos diferentes sobre o desempenho. O capítulo comenta que, mesmo sem sensores, os objetivos podem ser alcançáveis, em alguns casos com certeza. Então existem agentes melhores e piores, e os piores não são racionais.
- Exemplo ou contraexemplo: Aspirador sem sensores no mundo A/B, com geografia conhecida e posição e sujeira iniciais desconhecidas. A sequência Direita, Aspirar, Esquerda, Aspirar deixa os dois quadrados limpos qualquer que seja o estado inicial, porque um movimento para fora do mundo deixa o agente onde está. Um agente que só executa Esquerda para sempre nunca limpa nada. No mesmo ambiente não observável ele tem desempenho esperado bem menor que o agente da sequência acima, então não é racional, e um contraexemplo basta para derrubar o "todo".

### i. Um agente jogador de pôquer perfeitamente racional nunca perde.

- Julgamento: **F**
- Justificativa: Hipóteses: medida de desempenho em fichas ganhas, cartas dos adversários ocultas e baralho embaralhado ao acaso, adversários que também podem jogar bem. Racionalidade maximiza o desempenho esperado, e não o resultado real, que exigiria onisciência (Seção 2.2.2). O pôquer é parcialmente observável e estocástico (Figura 2.6), então uma decisão correta pode ter um resultado ruim, como o slide "Racionalidade e resultado" aponta.
- Exemplo ou contraexemplo: No Texas Hold'em, apostar tudo com um par de ases contra um par de reis antes do flop vence perto de 80% das vezes. A jogada é a certa, mas em cerca de uma a cada cinco vezes o adversário melhora o jogo nas cartas comunitárias (quase sempre com um terceiro rei) e o agente perde a mão. Numa noite curta, ele pode até terminar com menos fichas do que começou.

## Exercício 2.4
Para cada caso, delimite o agente, preencha o PEAS e justifique todas as classificações. Considere Titã como cenário hipotético do exercício.

Observação sobre previsibilidade: sigo a convenção da Seção 2.3.2, que deixa de fora da definição de estocástico a incerteza que vem apenas das ações de outros agentes. Por isso, nos casos com adversários, separo a incerteza física (que torna o ambiente estocástico) da incerteza estratégica (que aparece como multiagente e observabilidade parcial).

### Caso 1 — Jogar futebol.

- Agente analisado: Um jogador de linha (meio-campista) de um dos times. Não estou tratando o time inteiro como um agente só.
- Objetivo e hipóteses: Ajudar o time a vencer uma partida oficial de 90 minutos dentro das regras. O jogador controla apenas o próprio corpo; companheiros, adversários e árbitro são outros participantes do ambiente.
- P — Medida de desempenho: Resultado da partida e saldo de gols; contribuições individuais como passes certos, desarmes, finalizações e assistências; penalidade por faltas, cartões e gols sofridos por erro próprio.
- E — Ambiente: Campo, bola, traves, 10 companheiros, 11 adversários, árbitro e assistentes, gramado, clima.
- A — Atuadores: Pernas e pés (correr, passar, chutar, driblar), cabeça (cabecear), tronco e braços (proteger a bola, equilíbrio), voz e gestos para pedir a bola ou orientar colegas.
- S — Sensores: Visão, audição (chamados dos colegas e apito), propriocepção e equilíbrio, tato no contato com a bola e com outros jogadores.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | O jogador não vê quem está nas costas dele e não sabe o que os outros pretendem fazer. Muitas vezes precisa lembrar onde estava um adversário que saiu do campo de visão. |
| Número de agentes | Multiagente, cooperativo e competitivo | Os companheiros buscam a mesma medida que ele (cooperação). Os adversários maximizam uma medida que reduz a do agente, que é o critério do capítulo para competição. |
| Previsibilidade | Estocástico | Mesmo sem contar as decisões dos outros, o efeito das próprias ações é incerto: o chute pode sair torto, a bola quica de forma irregular no gramado, o vento desvia cruzamentos. As escolhas dos adversários somam ainda uma incerteza estratégica. |
| Dependência entre decisões | Sequencial | Um passe errado vira contra-ataque, o cansaço se acumula durante o jogo e um cartão amarelo muda como o jogador pode disputar bolas depois. |
| Mudança durante a decisão | Dinâmico | Bola e jogadores continuam se movendo enquanto ele decide. Se demorar para passar, a linha de passe fecha. |
| Natureza dos elementos | Combinação, predominantemente contínuo | Posições, velocidades, força do chute e tempo variam continuamente. Placar, cartões e o tipo de jogada (passe, chute, drible) são discretos. |
| Conhecimento do funcionamento | Conhecido | Um jogador treinado conhece as regras e como a bola reage aos toques. Não saber a tática do adversário é questão de observabilidade, não do funcionamento do ambiente. |

### Caso 2 — Explorar os oceanos subterrâneos de Titã.

- Agente analisado: Um veículo submarino autônomo que opera dentro do oceano sob a crosta de gelo de Titã.
- Objetivo e hipóteses: Cenário hipotético. Suponho que existe um oceano líquido sob o gelo, que o robô já atravessou a crosta e está na água, e que ele se comunica com a Terra por meio de uma sonda na superfície. O sinal leva mais de uma hora para chegar à Terra, então as decisões do dia a dia são do próprio robô. Também suponho que não há nenhuma forma de vida que se comporte como agente.
- P — Medida de desempenho: Volume mapeado; quantidade e qualidade das medições e amostras (química, temperatura, possíveis sinais de vida); dados efetivamente transmitidos; energia gasta; integridade do robô, já que perdê-lo encerra a missão.
- E — Ambiente: Oceano frio, escuro e sob alta pressão, correntes, teto de gelo e fundo com formato desconhecido, sonda de retransmissão na superfície.
- A — Atuadores: Propulsores e lemes, sistema de lastro para controlar a profundidade, braço coletor de amostras, iluminação, transmissor para a sonda.
- S — Sensores: Sonar, câmeras com iluminação, sensores de pressão, temperatura e composição química, unidade inercial (acelerômetros e giroscópios), medidor de bateria.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Sonar e câmera alcançam pouca distância no escuro. Não há GPS, então a posição é estimada pela unidade inercial e o erro cresce com o tempo. |
| Número de agentes | Agente único | Pela hipótese, não há outro agente no oceano, e a equipe na Terra fica fora do ciclo de decisão por causa do atraso. Se o robô encontrasse algo que reagisse a ele, essa classificação teria de ser revista. |
| Previsibilidade | Estocástico | Correntes desviam o robô, peças podem falhar e o efeito dos propulsores depende de propriedades do líquido que ninguém mediu ainda. |
| Dependência entre decisões | Sequencial | A energia gasta em uma região não volta, os compartimentos de amostra são limitados e a posição atual define o que dá para alcançar depois. |
| Mudança durante a decisão | Dinâmico | As correntes continuam arrastando o robô enquanto ele processa os dados, e o próprio robô segue em movimento, como o táxi do capítulo. |
| Natureza dos elementos | Combinação, predominantemente contínuo | Posição, profundidade, temperatura, empuxo e tempo são contínuos. Modo de operação (explorar, coletar, retornar) e a decisão de coletar ou não são discretos. |
| Conhecimento do funcionamento | Desconhecido | Ninguém explorou esse oceano. O robô precisa aprender, por exemplo, quanto os propulsores realmente o deslocam e como as correntes se comportam. Isso é diferente de observabilidade: mesmo enxergando tudo ao redor, ele não saberia de antemão o efeito das ações. |

### Caso 3 — Comprar livros usados de IA na Internet.

- Agente analisado: Um programa de compras (softbot) que age em nome de um estudante.
- Objetivo e hipóteses: O usuário informa os títulos e edições que quer, um orçamento máximo e um prazo. A compra é feita em marketplaces de livros usados com preço fixo (sem leilão), e o pagamento já está autorizado até o valor do orçamento.
- P — Medida de desempenho: Receber a edição certa em estado aceitável; custo total (livro + frete) baixo e dentro do orçamento; entrega no prazo; poucos pedidos cancelados ou devolvidos; nenhuma compra com vendedor fraudulento.
- E — Ambiente: Sites e marketplaces, anúncios, vendedores, outros compradores, sistema de pagamento, transportadora ou Correios, o próprio usuário.
- A — Atuadores: Fazer buscas, aplicar filtros, abrir anúncios, mandar perguntas aos vendedores, adicionar ao carrinho, preencher endereço e pagar, avisar o usuário.
- S — Sensores: Páginas HTML ou APIs dos sites (preço, frete, fotos, descrição do estado, reputação do vendedor, estoque), e-mails de confirmação e de rastreamento, respostas dos vendedores.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | O estado real do livro (grifos, páginas soltas, edição trocada) só aparece na entrega, e a foto do anúncio pode ser genérica. O agente também não sabe se outro comprador está prestes a fechar o mesmo exemplar. |
| Número de agentes | Multiagente, competição leve | Outros compradores disputam o mesmo exemplar. Os vendedores têm objetivos próprios (vender mais caro), mas a relação é em parte cooperativa, porque os dois lados querem que a venda aconteça. |
| Previsibilidade | Estocástico | Descontando as decisões de outros agentes, ainda há incerteza no resultado das ações: o pagamento pode falhar, o site pode cair e a entrega pode atrasar ou extraviar. |
| Dependência entre decisões | Sequencial | Comprar um livro consome orçamento que faria falta para o próximo, e um pedido pago não se desfaz sem custo. |
| Mudança durante a decisão | Dinâmico | Um anúncio pode ser vendido ou mudar de preço enquanto o agente ainda compara outras lojas. Se eu supusesse o catálogo congelado durante a busca, seria estático. |
| Natureza dos elementos | Discreto | Anúncios, páginas, cliques e pedidos são discretos, e os preços variam em centavos. O prazo de entrega é contado em dias. |
| Conhecimento do funcionamento | Conhecido | Para os sites que o agente já sabe usar, o efeito de buscar, adicionar ao carrinho e pagar é conhecido. Um site novo, com outro layout, exigiria que ele aprendesse a operá-lo. |

### Caso 4 — Jogar uma partida de tênis.

- Agente analisado: Um tenista humano em uma partida de simples contra outro tenista.
- Objetivo e hipóteses: Vencer a partida dentro das regras oficiais, em quadra aberta, com árbitro. Uso sensores reais, como no slide "Classificação de uma partida de tênis".
- P — Medida de desempenho: Vitória na partida; sets, games e pontos ganhos; poucos erros não forçados e duplas faltas.
- E — Ambiente: Quadra, rede, linhas, bola, adversário, árbitro e juízes de linha, vento e sol.
- A — Atuadores: Braço, punho e raquete (saque, golpes de fundo, voleio, efeito na bola) e pernas (deslocamento e posicionamento).
- S — Sensores: Visão (bola, adversário, linhas), audição (som da bola na raquete do adversário, marcação do juiz) e propriocepção.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | O efeito e a velocidade exata da bola só podem ser estimados, e o adversário esconde para onde vai sacar ou bater. |
| Número de agentes | Multiagente competitivo | O ponto que um jogador ganha o outro perde, então a medida de um diminui a do outro. |
| Previsibilidade | Estocástico | Vento, quique na quadra e imprecisão do próprio golpe fazem o mesmo movimento gerar trajetórias diferentes. A escolha do adversário entra como incerteza estratégica. |
| Dependência entre decisões | Sequencial | Uma bola curta deixa o adversário atacar no golpe seguinte, e o placar e o cansaço se acumulam ao longo dos sets. |
| Mudança durante a decisão | Dinâmico | A bola e o adversário se movem enquanto o jogador decide o golpe. |
| Natureza dos elementos | Combinação, predominantemente contínuo | Posição, velocidade, ângulo da raquete e tempo são contínuos. Placar e o tipo de golpe escolhido são discretos. |
| Conhecimento do funcionamento | Conhecido | O jogador conhece as regras e como a bola reage à raquete e à quadra. |

### Caso 5 — Praticar tênis contra uma parede.

- Agente analisado: O mesmo tenista, treinando sozinho contra um paredão.
- Objetivo e hipóteses: Treinar consistência e precisão. A parede é plana e não há mais ninguém na área. Ela não é um agente, porque não maximiza nenhuma medida que dependa do tenista; apenas devolve a bola pela física, como as "ondas do mar" citadas no capítulo.
- P — Medida de desempenho: Número de rebatidas seguidas sem a bola quicar duas vezes, quantidade de acertos em uma marca na parede, regularidade ao longo do treino.
- E — Ambiente: Parede, piso da área de treino, bola, vento.
- A — Atuadores: Braço, punho e raquete; pernas para se deslocar.
- S — Sensores: Visão, audição (som do impacto na parede) e propriocepção.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Os sensores são os mesmos do Caso 4, então o efeito e a velocidade exata da bola continuam sendo estimativas. Fica mais perto do completamente observável, porque não existe intenção escondida de um adversário. |
| Número de agentes | Agente único | Só o tenista toma decisões. A parede faz parte do ambiente. |
| Previsibilidade | Estocástico | A parede responde sempre da mesma forma, então a incerteza vem quase toda da variação do próprio golpe e de quiques irregulares. Com golpes perfeitamente precisos o ambiente seria quase determinístico. |
| Dependência entre decisões | Sequencial | A rebatida atual define onde e com que velocidade a bola volta, e a medida conta a sequência de rebatidas. |
| Mudança durante a decisão | Dinâmico | A bola continua vindo enquanto o jogador se prepara. |
| Natureza dos elementos | Combinação, predominantemente contínuo | Posições, velocidades e tempo são contínuos. A contagem de rebatidas é discreta. |
| Conhecimento do funcionamento | Conhecido | O jogador sabe como a bola volta da parede e como o golpe afeta a trajetória. |

### Caso 6 — Realizar um salto de altura.

- Agente analisado: Um atleta de salto em altura usando a técnica Fosbury.
- Objetivo e hipóteses: Recorto uma tentativa, da corrida de aproximação até a queda no colchão, com o sarrafo já na altura escolhida. Os outros competidores não interferem na execução. A escolha de quais alturas tentar fica fora desse recorte.
- P — Medida de desempenho: Passar sem derrubar o sarrafo (tentativa válida), altura conseguida, ausência de lesão e, na competição, menos tentativas falhas.
- E — Ambiente: Pista de aproximação, postes e sarrafo, colchão de queda, vento, juízes.
- A — Atuadores: Pernas (corrida e impulsão), tronco, quadril e braços (rotação e arqueamento sobre o sarrafo).
- S — Sensores: Visão (marca de saída e sarrafo), propriocepção, equilíbrio, tato do pé no chão e audição para o sinal do juiz.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | No Fosbury o atleta passa de costas para o sarrafo e não vê se o quadril ou as pernas vão encostar nele. O vento também não é medido com precisão por ele. |
| Número de agentes | Agente único | Pelas hipóteses, ninguém atua durante o salto. Os juízes só validam o resultado. |
| Previsibilidade | Estocástico | O mesmo plano de corrida gera passadas um pouco diferentes, a impulsão varia e o vento interfere, então o resultado do salto não fica determinado pelo estado e pela ação planejada. |
| Dependência entre decisões | Sequencial | Corrida, impulsão, passagem e queda são encadeadas: uma passada errada compromete a impulsão. Entre tentativas também há dependência, porque três falhas seguidas eliminam o atleta. |
| Mudança durante a decisão | Dinâmico | Sarrafo e colchão ficam parados, mas o corpo do atleta segue em movimento pela inércia e pela gravidade enquanto ele ajusta o salto. O capítulo conta o movimento do próprio táxi como mudança do ambiente, e aqui é a mesma situação. Antes de iniciar a corrida, com tempo limite para começar a tentativa, o caso seria semidinâmico. |
| Natureza dos elementos | Combinação, predominantemente contínuo | Velocidade, ângulo de impulsão, altura e tempo são contínuos. O resultado (válido ou nulo) é discreto. |
| Conhecimento do funcionamento | Conhecido | O atleta conhece as regras da prova e a técnica do salto. |

### Caso 7 — Participar de um leilão de um item, realizando lances.

- Agente analisado: Um programa que dá lances em nome de um usuário em um leilão online.
- Objetivo e hipóteses: Assumi um leilão aberto e ascendente de um único item, em que todos veem o preço atual, o lance mínimo é o preço atual mais um incremento fixo e o encerramento tem horário marcado. O usuário define um teto, o valor máximo que aceita pagar. Também suponho que a plataforma não falha. Se fosse um leilão fechado, com um único lance em envelope, o caso ficaria episódico e estático até o prazo.
- P — Medida de desempenho: Arrematar o item pagando o menor preço possível, nunca acima do teto. Perder só é aceitável quando o preço passou do teto.
- E — Ambiente: Plataforma do leilão, item e sua descrição, vendedor, outros licitantes (pessoas e outros programas), relógio de encerramento.
- A — Atuadores: Enviar lance com um valor, deixar de dar lances, efetuar o pagamento ao vencer, avisar o usuário.
- S — Sensores: Preço atual, histórico de lances, tempo restante, descrição e fotos do item, mensagens da plataforma (lance aceito, lance superado, leilão encerrado).

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | O agente vê preço, histórico e tempo, mas não sabe o teto dos concorrentes nem o estado real do item. É parecido com o táxi, que não sabe o que os outros motoristas estão pensando. |
| Número de agentes | Multiagente competitivo | Cada licitante quer pagar menos, e o lance de um tira a vitória do outro. O vendedor também é um agente, interessado em preço alto. |
| Previsibilidade | Determinístico (estratégico) | Pelas regras, o próximo estado fica determinado pelo estado atual e pelos lances dados. A incerteza vem só das escolhas dos outros licitantes, que o capítulo deixa fora da definição, como em um jogo. Na prática essa incerteza estratégica pesa bastante e aparece na observabilidade parcial. |
| Dependência entre decisões | Sequencial | Cada lance sobe o preço e muda o que o agente e os outros farão em seguida. |
| Mudança durante a decisão | Dinâmico | Outros licitantes podem dar lances enquanto o agente decide, e o relógio corre. Perto do encerramento, demorar significa perder. |
| Natureza dos elementos | Combinação, predominantemente discreto | Valores em múltiplos do incremento, lances como eventos e o conjunto de ações são discretos. O tempo é contínuo, mas o que importa dele é basicamente o horário de encerramento. |
| Conhecimento do funcionamento | Conhecido | As regras da plataforma (incremento, encerramento, quem vence) são publicadas. As estratégias dos outros ficam por conta da observabilidade. |

### Opções para classificação
- **Observabilidade:** Completamente observável, parcialmente observável ou não observável.
- **Número de agentes:** Agente único ou multiagente; indique cooperação ou competição quando pertinente.
- **Previsibilidade:** Determinístico ou estocástico; considere a influência estratégica de outros agentes.
- **Dependência entre decisões:** Episódico ou sequencial.
- **Mudança durante a decisão:** Estático, dinâmico ou semidinâmico.
- **Natureza dos elementos:** Discretos, contínuos ou combinação; considere estados, tempo, percepções e ações.
- **Conhecimento do funcionamento:** Conhecido ou desconhecido para o agente.

### Comparação final
1. O que muda entre jogar tênis contra outra pessoa e praticar contra uma parede?
2. Por que comprar livros usados pode exigir decisões com informações incompletas?
3. Como outros agentes influenciam futebol e leilões?

Respostas:

1. A mudança principal é o número de agentes. Contra uma pessoa o ambiente é multiagente competitivo: o adversário esconde para onde vai jogar e tenta explorar padrões do agente. Por isso, variar o lado do saque pode ser racional, já que o capítulo observa que em ambientes competitivos parcialmente observáveis o comportamento aleatório evita a armadilha de ser previsível. Contra a parede, a devolução depende só da física e do próprio golpe, e variar sem motivo não traz vantagem. A medida de desempenho também muda: na partida o agente mira onde o adversário não alcança; no treino ele quer que a bola volte de um jeito que dê para continuar rebatendo. Nas minhas classificações, as outras propriedades ficaram iguais nos dois casos (parcialmente observável, estocástico, sequencial, dinâmico, contínuo e conhecido), mas contra a parede a incerteza é bem menor.
2. Porque o agente nunca encosta no livro. Tudo o que ele sabe vem de fotos, de uma descrição subjetiva como "bom estado" e da reputação do vendedor, que é uma média de compras passadas. O estoque pode mudar durante a busca e o prazo de entrega é uma estimativa. Ele precisa pagar antes de ver o exemplar. Um agente racional, nesse caso, coleta informação quando vale a pena (perguntar ao vendedor sobre grifos, ler avaliações) e pesa preço contra risco, o que combina com um agente baseado em utilidade.
3. No futebol, companheiros e adversários mudam o estado o tempo todo: abrem e fecham linhas de passe, marcam, antecipam jogadas. O jogador precisa prever o movimento dos outros, cooperar com o próprio time, inclusive se comunicando, e competir com o time adversário. No leilão, os outros licitantes definem o preço que o agente vai pagar e se ele vence. Cada lance é uma resposta ao anterior, e o agente precisa estimar o teto dos concorrentes, que ele não observa.

## Exercício 2.5
Defina cada termo com suas palavras em duas a quatro linhas e apresente um exemplo.

### Agente

- Definição: Qualquer coisa que percebe o ambiente por sensores e age sobre ele por atuadores. O capítulo trata essa ideia como uma ferramenta para analisar sistemas, e não como um rótulo que separa o mundo em agentes e não agentes.
- Exemplo: Um bot de moderação em um servidor do Discord, que lê as mensagens (percepções) e apaga as ofensivas ou silencia o usuário (ações).

### Função de agente

- Definição: Descrição matemática do comportamento: para cada sequência possível de percepções, diz qual ação o agente executa. Ela descreve o agente "por fora", sem dizer como ele é implementado, e para a maioria dos agentes a tabela correspondente seria infinita.
- Exemplo: A tabela parcial da Figura 2.3: [A, Limpo] → Direita; [B, Sujo] → Aspirar; [A, Limpo], [A, Sujo] → Aspirar.

### Programa de agente

- Definição: A implementação concreta da função de agente, executada em uma arquitetura física (agente = arquitetura + programa). Recebe a percepção atual e devolve uma ação; o que precisar do passado, ele mesmo guarda.
- Exemplo: Uma função Python `agir(posicao, situacao)` que retorna `"Aspirar"` se a situação for suja e, senão, `"Direita"` em A e `"Esquerda"` em B, rodando no microcontrolador do aspirador. É o programa da Figura 2.8.

### Racionalidade

- Definição: Escolher a ação que se espera maximizar a medida de desempenho, levando em conta as percepções até o momento, o conhecimento prévio e as ações disponíveis. Ela é avaliada com a informação que o agente tinha na hora, então um resultado ruim não torna a escolha irracional.
- Exemplo: Um aplicativo de navegação que escolhe a rota com menor tempo esperado pelo trânsito atual agiu racionalmente, mesmo que um acidente imprevisto trave essa rota dez minutos depois.

### Autonomia

- Definição: Quanto o comportamento do agente depende das próprias percepções e do que ele aprendeu, em vez de depender só do conhecimento que o projetista colocou. Um agente pode começar com algum conhecimento inicial e ganhar autonomia com a experiência.
- Exemplo: Um filtro de spam que começa com regras básicas e passa a classificar de acordo com as mensagens que o usuário marca como spam. A vespa Sphex do capítulo é o caso contrário: repete o plano inato mesmo quando ele falha.

### Agente reativo

- Definição: Agente que escolhe a ação apenas pela percepção atual, com regras condição-ação do tipo "se ... então ...", sem guardar nada do histórico. Funciona bem quando a percepção atual basta para decidir, ou seja, em ambientes completamente observáveis.
- Exemplo: Um irrigador de jardim que liga a água quando o sensor de umidade indica solo seco e desliga quando indica solo úmido.

### Agente baseado em modelo

- Definição: Agente que mantém um estado interno atualizado a cada percepção, usando um modelo de como o mundo evolui e de como as próprias ações o afetam. Assim ele acompanha partes do mundo que não está vendo agora, com um "melhor palpite" sobre o estado atual.
- Exemplo: Um robô aspirador que guarda um mapa dos cômodos já limpos e sua posição estimada pelas rodas, e volta para a base quando o mapa indica que terminou.

### Agente baseado em objetivos

- Definição: Agente que, além de saber como o mundo está, tem uma descrição das situações que deseja alcançar e escolhe ações pensando no futuro, com busca ou planejamento. Para mudar o comportamento, basta trocar o objetivo, sem reescrever regras.
- Exemplo: Um robô de armazém que recebe a tarefa "levar a caixa X até a doca 3" e planeja o caminho entre as prateleiras. Se a doca mudar para a 5, ele replaneja com o novo objetivo.

### Agente baseado em utilidade

- Definição: Agente que usa uma função utilidade para medir o quanto cada estado é desejável e escolhe a ação com maior utilidade esperada. Ele consegue comparar caminhos que atingem o mesmo objetivo e equilibrar objetivos conflitantes ou incertos.
- Exemplo: Um aplicativo de rotas que pesa tempo de viagem, gasto com pedágio e risco de congestionamento para escolher entre três caminhos que chegam ao mesmo destino.

### Agente com aprendizagem

- Definição: Agente que melhora com a experiência. O elemento de desempenho escolhe as ações, o crítico compara o resultado com um padrão fixo, o elemento de aprendizado ajusta os outros componentes e o gerador de problemas sugere ações exploratórias.
- Exemplo: O robô de Titã do Caso 2: o crítico compara o deslocamento planejado com o medido pela unidade inercial, o elemento de aprendizado corrige o modelo de resposta dos propulsores e o gerador de problemas manda testar manobras em profundidades ainda não visitadas.

## Síntese com autômatos
Escolha um caso do item 2.4. Apresente três estados internos, três percepções, três ações e duas regras no formato estado atual + percepção → próximo estado e ação. Explique como estados internos representam informação passada e cite uma limitação da simplificação.

Resposta:

Escolhi o Caso 7, o programa que dá lances em um leilão aberto. Modelei o agente como um controlador finito em que cada transição lê uma percepção, muda o estado interno e emite uma ação.

Estados internos:

- LIDERANDO: o último lance válido é do agente.
- FORA: em algum momento o próximo lance possível passou do teto, e o agente parou de dar lances.
- ARREMATOU: o leilão terminou com o agente na frente.

Percepções (já interpretadas, como faz o INTERPRETAR-ENTRADA da Figura 2.10, que compara o preço com o teto):

- p1: outro participante deu um lance, e preço + incremento ainda cabe no teto.
- p2: outro participante deu um lance, e preço + incremento passa do teto.
- p3: leilão encerrado.

Ações:

- a1: dar lance de preço atual + incremento.
- a2: não fazer nada.
- a3: pagar o item.

Estado inicial: LIDERANDO, depois que o agente entra com o lance mínimo (suponho que esse lance é aceito).

| Estado atual | p1 | p2 | p3 |
|---|---|---|---|
| LIDERANDO | LIDERANDO, a1 | FORA, a2 | ARREMATOU, a3 |
| FORA | não ocorre (o preço só sobe) | FORA, a2 | FORA, a2 |
| ARREMATOU | não ocorre | não ocorre | ARREMATOU, a2 |

Regras destacadas:

- R1: LIDERANDO + p2 → FORA e a2 (não fazer nada). Cobrir esse lance passaria do teto, então o agente sai da disputa.
- R2: LIDERANDO + p3 → ARREMATOU e a3 (pagar o item). O leilão acabou com o agente na frente.

Como o estado guarda informação passada: o agente não armazena a lista de lances que recebeu. O estado é um resumo do que importa nesse histórico. Estar em FORA significa "em algum momento cobrir o lance de alguém passaria do meu teto"; estar em LIDERANDO significa "até agora, cobri todos os lances". Isso aparece com clareza na percepção p3: ela é a mesma nos dois casos, mas em LIDERANDO leva a pagar e em FORA leva a não fazer nada. Um agente reativo simples, que só olha a percepção atual, não teria como distinguir essas duas situações. É o que o slide "Agentes e autômatos" descreve: o estado interno resume o histórico e a transição o atualiza a partir da percepção.

Limitação da simplificação: o modelo supõe que o lance do agente é aceito na hora e não representa o tempo. Na plataforma real, dois lances podem chegar quase juntos e o do agente ser recusado, o que exigiria um estado a mais (esperando confirmação). Sem o relógio, o agente também não consegue usar estratégias que dependem do tempo restante, como segurar o lance até os últimos segundos para não subir o preço cedo. Outro ponto é que o preço e o teto são números sem limite fixo e não cabem em um conjunto finito de estados; por isso deixei a comparação dentro da interpretação da percepção.

## Entrega e avaliação
Confira: identificação; nove análises no item 2.3; sete casos completos no item 2.4; dez conceitos no item 2.5; síntese; referências.
Nome sugerido: `NomeSobrenome_Atividade_AgentesInteligentes`. Prazo e envio conforme orientação da professora.

| Critério | Atividade avaliativa (1,0 ponto) A2 |
|---|---:|
| Item 2.3 — correção e argumentação | 30% |
| Item 2.4 — PEAS e classificação justificada | 40% |
| Item 2.5 — precisão conceitual e exemplos | 20% |
| Síntese, organização e referências | 10% |

## Referências
Material-base: Capítulo 2 — Agentes inteligentes, disponibilizado para a aula de 19/10/2026.
Referências adicionais:

- RUSSELL, Stuart; NORVIG, Peter. Agentes inteligentes. In: RUSSELL, Stuart; NORVIG, Peter. *Inteligência Artificial*. Tradução da 3. ed. Rio de Janeiro: Elsevier, 2013. Cap. 2. Texto disponibilizado pela professora para a aula de 19/10/2026.
- OLIVEIRA, Kadidja Valéria Reginaldo de. *Agentes Inteligentes: Capítulo 2*. Slides da aula de 19/10/2026. Inteligência Artificial, Linguagens Formais e Autômatos. Brasília: UDF, 2026.
- OLIVEIRA, Kadidja Valéria Reginaldo de. *Instruções gerais da atividade: agentes inteligentes*. Aula de 19/10/2026. Brasília: UDF, 2026.
