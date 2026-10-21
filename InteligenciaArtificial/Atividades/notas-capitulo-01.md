# Notas — Capítulo 1: Introdução

Brayan Aragão Pletsch, RGM 38473585, Engenharia de Software - N1

RUSSELL, Stuart J.; NORVIG, Peter. Inteligência Artificial: Uma Abordagem Moderna. 4. ed. Rio de Janeiro: GEN LTC, 2022. E-book. p. 1. ISBN 9788595159495. Acesso: 05 out. 2026. Disponível em: Minha Biblioteca

## 1. Conceitos principais

- Inteligência artificial como área multidisciplinar, voltada para sistemas que percebem o ambiente, raciocinam, aprendem e agem.
- As quatro visões da IA. Elas saem do cruzamento de duas perguntas: o foco está no pensamento ou no comportamento? A referência é o ser humano ou a racionalidade? Daí vêm pensar como humano (abordagem cognitiva), agir como humano (teste de Turing), pensar racionalmente (leis do pensamento, lógica) e agir racionalmente (agente racional).
- Agente: tudo que percebe o ambiente por sensores e modifica esse ambiente por atuadores.
- Agente racional: escolhe a ação que maximiza o desempenho esperado com a informação que tem. Para isso pesa o que percebe, o que já sabe, quais ações estão disponíveis e que consequência espera de cada uma.
- Áreas que deram base à IA: filosofia, matemática, neurociência, psicologia, computação, teoria de controle, linguística e economia.
- Linha histórica: computação moderna e Alan Turing entre 1940 e 1950, a Conferência de Dartmouth em 1956 (quando o nome "Artificial Intelligence" ganha destaque), os primeiros avanços de 1950 a 1970, os invernos da IA e depois o renascimento da área.
- IA especializada e IA geral.
- Benefícios e riscos do uso de IA.

## 2. Conceitos que considerei mais importantes

- Agir racionalmente. É a visão que o livro adota e foi a que mais fez sentido para mim. As outras três dependem de imitar o ser humano ou de seguir a lógica à risca. Já o agente racional pode ser avaliado pelo resultado: definido o objetivo, dá para comparar uma ação com outra. Isso lembra muito um critério de aceitação em software.
- O ciclo percebe → decide → age → observa novamente. Um programa comum normalmente recebe uma entrada, devolve uma saída e termina. O agente continua no ciclo e usa o resultado da última ação para decidir a próxima.
- Inteligência em uma tarefa é diferente de inteligência geral. Um sistema que vence um campeão de xadrez não sabe dirigir nem traduzir. Vale lembrar disso quando aparece notícia dizendo que uma IA "pensa".
- IA não precisa de corpo físico. Chatbot, mecanismo de busca, sistema de recomendação e sistema de previsão também são IA. Antes da leitura eu associava IA quase direto a robô.

## 3. O que compreendi

O capítulo parte de uma pergunta que parece simples: o que significa uma máquina ser inteligente? A resposta muda conforme o ponto de vista. Se a referência é o ser humano, a IA pode tentar reproduzir como a gente pensa, e aí precisa entender percepção, memória, aprendizagem, resolução de problemas e tomada de decisão. Ou pode tentar reproduzir como a gente se comporta, que é a ideia do teste de Turing. Se a referência é a racionalidade, a IA pode seguir as regras da lógica, como no silogismo de Sócrates, ou escolher a melhor ação possível com o que sabe.

Russell e Norvig dão ênfase a essa última. Pelo que entendi, raciocinar certo pela lógica é uma forma de agir bem, mas em muitas situações não existe uma dedução pronta e mesmo assim o agente precisa fazer alguma coisa. O carro autônomo é um bom caso: ele percebe, decide, age e observa de novo o tempo todo. A palavra "esperado" na definição também pesa. O agente não sabe com certeza o que vai acontecer depois da ação, por isso a matemática da IA inclui probabilidade (incerteza e inferência) junto com a lógica (representação e raciocínio).

Na parte histórica, a IA aparece como resultado de várias áreas. Perguntas antigas da filosofia, como "o que é conhecimento?" e "como devemos tomar decisões?", viraram problemas que um computador pode tentar resolver. Entre 1950 e 1970 houve muito entusiasmo com programas que demonstravam teoremas, jogavam e manipulavam símbolos. Só que as promessas passaram do que a tecnologia conseguia entregar, e vieram os invernos da IA, com menos financiamento, menos projetos e expectativas menores. O renascimento não veio de uma descoberta só. Foi a soma de mais dados, mais processamento, algoritmos melhores e deep learning.

Por último, o capítulo mostra o que as máquinas já fazem hoje (reconhecer imagens e fala, traduzir, gerar conteúdo, jogar jogos complexos, auxiliar diagnósticos e programar) e os riscos que vêm junto: viés e discriminação, privacidade, segurança, desinformação, impacto no trabalho e uso indevido. Entendi que a pergunta que os autores deixam é como construir uma IA que seja útil e segura ao mesmo tempo.

## 4. Exemplos apresentados pelos autores

- Silogismo de Sócrates: "todos os seres humanos são mortais", "Sócrates é humano", logo "Sócrates é mortal". Serve para mostrar a abordagem das leis do pensamento, em que a conclusão sai das premissas só pela aplicação de uma regra.
- Teste de Turing, proposto por Alan Turing em 1950 no artigo "Computing Machinery and Intelligence": uma máquina consegue conversar de um jeito que não dê para distinguir de um ser humano? Para isso ela precisaria de linguagem, conhecimento, raciocínio e aprendizagem.
- Carro autônomo como exemplo de agente racional, sempre no ciclo percebe, decide, age e observa novamente.
- Robô aspirador: percebe obstáculos, posição, sujeira e bateria; decide para onde ir e se continua ou volta; se move, desvia, aspira e retorna. Achei o exemplo bom porque separa bem o que é sensor e o que é atuador.
- IA no dia a dia: teclado do celular, recomendação de músicas, filmes e produtos, rotas e mapas, filtro de spam, sistemas de busca, assistentes e chatbots.
- Perguntas para provocar: uma IA que vence um campeão de xadrez é inteligente? Uma IA que escreve um texto compreende o que escreveu? Um robô que dirige sozinho entende o mundo como uma pessoa?
- Aplicativo de transporte escolhendo uma rota, com quatro opções: sempre a mais curta, a mais rápida naquele momento, considerar trânsito, distância, histórico e objetivo do usuário, ou escolher ao acaso para explorar. Eu escolheria a terceira. A mais curta ignora o trânsito e a mais rápida agora ignora o histórico e o que o usuário quer (talvez ele prefira evitar pedágio, por exemplo). A aleatória faz sentido para o sistema aprender, mas não para quem precisa chegar.
- Benefícios por área: apoio à análise de exames na saúde, personalização do ensino na educação, análise de grandes volumes de dados na ciência, automação e otimização na indústria e tecnologias assistivas na acessibilidade.

## 5. Relações com conhecimentos anteriores

- Turing de novo. Na parte de autômatos estudamos a Máquina de Turing como modelo do que pode ser computado e vimos que existem limites computacionais. No capítulo 1 o mesmo Turing aparece com uma pergunta de outro tipo: se o comportamento de uma máquina numa conversa pode ser confundido com o de uma pessoa. A Máquina de Turing trata do que um computador consegue calcular. O teste trata de como julgar se o resultado parece inteligente.
- Lógica da Aula 1. Os operadores que vimos (¬, ∧, ∨, →) aparecem no silogismo. Dá para escrever "se x é humano, então x é mortal" como humano(x) → mortal(x). Com humano(Sócrates), chega-se a mortal(Sócrates). A abordagem de pensar racionalmente parte desse tipo de inferência.
- Derivação em gramáticas. Na aula de gramáticas formais a gente partia do símbolo inicial e aplicava regras de produção até chegar numa palavra só com terminais. A inferência lógica funciona de um jeito parecido: premissas mais regras geram conclusões, passo a passo, sem precisar "entender" o conteúdo. Isso me ajudou a ver por que os primeiros programas de IA focavam em manipular símbolos e demonstrar teoremas.
- Autômato finito e o ciclo do agente. O AFD lê um símbolo e muda de estado; o agente recebe uma percepção e escolhe uma ação. Dá para esboçar o robô aspirador como autômato, com estados ASPIRANDO, DESVIANDO e VOLTANDO e entradas como "sujeira", "obstáculo" e "bateria baixa". Para um robô bem simples funciona. Mas o AFD só aceita ou rejeita uma cadeia e, no mesmo estado, reage sempre igual à mesma entrada. Ele não tem medida de desempenho nem lida com incerteza, que são justamente o que o capítulo coloca no centro do agente racional.
- Expressões regulares e filtro de spam. No tutorial de regex validamos o formato de um e-mail escrevendo o padrão na mão. O capítulo cita filtro de spam como IA do dia a dia, e fiquei pensando em quanto um filtro baseado em regex se parece com isso (anotei como dúvida).
- Linguística e linguagens formais. A linguística está entre as áreas que deram base à IA. Na aula inaugural a disciplina começou por alfabetos, palavras, linguagens e gramáticas de Chomsky. Chatbot e tradução lidam com língua natural, que é bem mais ambígua do que as linguagens formais que estudamos, mas nos dois casos a ideia é descrever a língua por meio de regras.
- Engenharia de Software. A medida de desempenho do agente racional lembra requisito: se o objetivo estiver mal definido, o sistema pode cumprir a meta e mesmo assim não atender o usuário. O desafio da rota é parecido com uma discussão de prioridade entre requisitos (tempo, distância, preferência do usuário).

## 6. Dúvidas

- Onde fica a fronteira entre um programa comum e IA? Um filtro de spam feito só com expressões regulares que eu mesmo escrevi conta como IA? Pela definição de agente parece que sim, porque ele percebe a mensagem e age movendo para a pasta de spam. Mas imagino que o filtro citado no capítulo seja do tipo que aprende com dados.
- Se toda IA roda em um computador, ela fica presa aos mesmos limites que vimos com a Máquina de Turing? Ou seja, existe problema que nenhuma IA vai resolver, não importa quantos dados ou quanto processamento ela tenha?
- O teste de Turing avalia só a conversa. Um chatbot que passa no teste está "agindo como humano", mas o capítulo deixa aberto se ele compreende o que escreve. O teste mede inteligência ou só capacidade de imitar? Ele ainda é usado como critério hoje?
- Escolher uma rota ao acaso para explorar pode ser considerado racional? Para o usuário daquela corrida parece ruim, mas para o sistema pode valer a pena. Nesse caso a racionalidade é medida pelo objetivo de quem: do usuário ou da empresa?
- Quem define a medida de desempenho de um agente? Se ela for definida errada, o agente continua sendo racional?
- Na discussão sobre os primeiros avanços aparece a pergunta "que capacidades faltavam?". Não consegui responder só com o capítulo. Faltava processamento, dados, ou era um problema da própria abordagem simbólica?

## 7. Pontos que gostaria de aprofundar

- Ler o artigo "Computing Machinery and Intelligence" para ver como o próprio Turing descreve o teste.
- Os invernos da IA: quais promessas não se cumpriram e o que foi cortado.
- Como o agente calcula o "desempenho esperado" quando há incerteza. Pela parte de matemática, isso passa por probabilidade e inferência.
- Até onde um agente pode ser modelado por autômato finito e quando ele precisa de mais memória ou de outro modelo. Acho que isso conversa com o próximo capítulo, sobre agentes inteligentes.
- Viés e discriminação em sistemas de recomendação, que aparecem no capítulo tanto como exemplo de IA do dia a dia quanto na lista de riscos.

## 8. Reflexão final

Antes da leitura eu tinha uma ideia de IA bem ligada a robô e a chatbot. O capítulo me mostrou que existem pelo menos quatro formas de definir a área e que o livro escolhe a do agente racional, que é a mais prática para quem vai construir sistemas. Também ficou claro que a IA teve altos e baixos e que o que existe hoje é forte em tarefas específicas, enquanto a IA geral ainda é objetivo de pesquisa.

O que mais me interessou foi perceber que a parte de linguagens formais e autômatos que vimos no começo do semestre tem ligação direta com IA: lógica, regras, derivação, estados e o próprio Turing. Fiquei com vontade de entender melhor onde o modelo de autômato deixa de ser suficiente para descrever um agente. A pergunta com que a aula fechou também ficou na cabeça. Em vez de perguntar se a máquina pensa, faz mais sentido perguntar como ela percebe, decide, aprende e age.
