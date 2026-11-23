# Ética e impactos da IA na triagem de pull requests

**Estudante:** Brayan Aragão Pletsch  
**RGM:** 38473585  
**Curso/Turma:** Engenharia de Software - N1 (noturno)  
**Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos  
**Professora:** Kadidja Valéria  
**Aula:** 16/11/2026, Ética e implicações em IA (A1, 0,5 pt)

Esta análise é sobre o sistema especialista que fiz na aula 13, a [triagem de pull requests](../../08_AprendizadoSupervisionado/README.md) ([notebook no Colab](https://colab.research.google.com/drive/1fWa30sqzyK-5dhodaoRDjOn5by51pCIu?usp=sharing)).

## 1. Leitura e vídeo

### Artigo

LACERDA JÚNIOR, Francisco Pires de. Da proibição à governança: uso ético da inteligência artificial generativa na educação superior: uma revisão integrativa (2023–2026). *Revista Foco*, v. 19, n. 8, e12330, p. 1-18, 2026. DOI: 10.54751/revistafoco.v19n8-017.

A questão de integridade que eu separei é a de conseguir explicar o que foi entregue. Na seção 4.2 (p. 10), o autor diz que perguntar só se houve IA resolve pouco, e que é preciso identificar o que foi delegado e se essa delegação preservou a competência que está sendo avaliada. Ele chega a três requisitos mínimos: autoria humana responsável, rastreabilidade suficiente do uso e possibilidade de explicar as decisões apresentadas. Na p. 6 ele diz ainda que declarar a ajuda da IA não torna aceitável um uso inadequado, mas que, sem a declaração, ninguém consegue avaliar como o trabalho foi feito.

No meu caso isso pesa, porque usei bastante IA no trabalho da aula 13 (está na seção 4). A competência avaliada era montar um sistema especialista com um modelo treinado e mostrar como os fatos acionam as regras. Então, além de declarar, eu preciso conseguir defender cada escolha, como o limite de 400 linhas da D1 ou o motivo de a R5 existir. O artigo também diz (p. 10 e 11) que detectores automáticos de texto gerado por IA são instáveis e podem errar mais com alguns grupos, e sugere olhar o processo, com versões intermediárias e explicação das escolhas. O histórico de commits do repositório mostra como o trabalho foi mudando.

### Vídeo

INSTITUTO DE ESTUDOS AVANÇADOS DA USP. *O Estado da Arte em Ética na Inteligência Artificial*. São Paulo: IEA-USP, 9 jun. 2026. 1 vídeo (2h01). Disponível em: <https://www.iea.usp.br/midiateca/video/videos-2026/o-estado-da-arte-em-etica-na-inteligencia-artificial/>. A mesma gravação está no [YouTube, já no início do trecho](https://www.youtube.com/watch?v=x35_NJfXrpE&t=1312s).

Trecho: de 21:52 a 23:30, na fala do Steven Gouveia, que organizou o livro lançado no evento (*The Palgrave Handbook on the Ethics of Artificial Intelligence*) e resume os capítulos da seção sobre IA e virtudes. Sobre o capítulo que ele escreveu, diz que a explicabilidade sozinha não fecha as lacunas de responsabilidade em sistemas opacos, e que o caráter da organização dá uma base mais sólida para a prestação de contas. Logo depois, resumindo outro capítulo, diz que depender demais das ferramentas de IA pode corroer o entendimento básico de quem as usa, e que a IA deveria entrar como auxílio crítico, e não como substituto.

Ideia para o debate: o meu sistema mostra a regra e o rastro de cada recomendação. Isso explica de onde a recomendação veio. Quem responde quando um PR marcado como "revisão normal" quebra a produção é outra pergunta, e o sistema não tem resposta para ela.

## 2. Análise ética do projeto

O projeto ajuda um time de desenvolvimento a decidir quanto cuidado cada pull request precisa na revisão de código. Quem usa é a pessoa que revisa os PRs. Quem pode ser afetado é o autor do PR, que pode ter o trabalho travado ou receber pedidos a mais, e quem usa o software, se um PR com defeito passar. A IA entra em um ponto só: uma árvore de decisão olha as linhas alteradas, os arquivos alterados e se o PR tem teste, e prevê o risco como alto ou baixo. O resto são regras que eu escrevi. A D1 (mais de 400 linhas é PR grande) e a R0 (perguntar se é área crítica quando ninguém sabe) não dependem do modelo. As regras R1 a R6 juntam o risco previsto com os fatos que o time informa. O texto de cada recomendação foi decisão minha, e o modelo só escolhe se o PR segue pelas regras de risco alto ou pelas de risco baixo.

| Aspecto | Situação no projeto | Quem pode ser afetado | O que eu faço ou faria |
|:--|:--|:--|:--|
| Privacidade e dados | O dataset só tem números de cada PR (linhas, arquivos, se tem teste) e o rótulo. Deixei o autor de fora, mas com dados reais isso não basta: o número do PR leva direto ao autor no GitHub. | O autor do PR, que poderia ser identificado e comparado com os colegas. | Usar o número do PR só para montar o rótulo (procurar reverts e hotfixes) e apagar essa coluna depois. Os três números e o rótulo bastam para a finalidade, como pedem os princípios da finalidade e da necessidade da LGPD (art. 6º, I e III). |
| Viés e equidade | Linhas de teste contam como linhas alteradas. Um PR de 290 linhas com teste sai com risco baixo (8% de risco alto na folha). Se o autor escrever mais 40 linhas de teste, o PR vai para 330 linhas e passa a risco alto. | Quem escreve mais teste, e quem abre PR com arquivo gerado (lockfile, migração automática), que aumenta as linhas sem mudar a lógica. | Contar só as linhas fora de arquivos de teste e de arquivos gerados. Acrescentar ao notebook um teste, no mesmo formato dos testes das regras, que confere que somar linhas de teste a um PR nunca aumenta o risco previsto. |
| Transparência | A saída mostra o risco previsto, a porcentagem de risco alto na folha, a regra, o rastro e o aviso "Sugestão para quem revisa. A decisão continua sendo do revisor." Só que quem vê isso é o revisor. O autor recebe apenas o pedido. | O autor, que recebe "divida o PR" sem saber de onde veio o pedido. | Publicar a recomendação como comentário no próprio PR, marcada como sugestão automática da triagem, com a regra e o rastro. |
| Supervisão e responsabilidade | Quem decide é o revisor, mas o sistema não registra quando ele discorda. Um PR que atualiza uma biblioteca e mexe em 900 linhas pode não ter como ser dividido, e a R2 pede a divisão mesmo assim. | O autor, que pode ficar parado esperando uma divisão que não faz sentido. | Um campo "não segui porque..." em cada recomendação. Uma vez por mês o time lê esses registros e ajusta as regras, por exemplo o limite de 400 linhas da D1. |
| Impacto social | Os revisores gastam tempo onde o risco é maior, e PRs pequenos entram mais rápido. Se a recomendação for tratada como definitiva, os erros do modelo vão para a produção: no teste, 9 PRs de risco alto saíram como baixo, todos pequenos, e 2 deles receberam "revisão normal" (considerando que não eram de área crítica). | Quem usa o software, que recebe o bug. | Mudar o texto da R6, que hoje diz "Pode fazer merge com uma aprovação" e soa como autorização. A regra passaria a indicar só o nível de revisão, e o merge fica com quem revisa. |

## 3. Dilema e reflexão

### Dilema

O dilema que escolhi é parecido com a questão do debate sobre o Orientador UDF e a coordenação. O histórico do sistema mostra quais PRs caíram em risco alto ou receberam pedido de divisão. Se esse histórico for agrupado por autor, o líder técnico vê quem mais aparece em risco alto. Ele deveria ter acesso a isso?

Uma saída é mandar o relatório por autor para o líder. Ele vê quem está com dificuldade e pode oferecer mentoria cedo. Em compensação, o relatório vira avaliação de desempenho mesmo que ninguém tenha planejado isso. Quem pega as tarefas difíceis, como refatorações grandes e código legado, aparece mais vezes. E as pessoas aprendem a picar PRs só para ficar abaixo do corte de 311 linhas, ou deixam de fazer a refatoração que o código precisava.

A outra saída é guardar só os números de cada PR, sem autor, e mostrar ao líder o resultado por módulo do sistema, por exemplo "metade dos PRs do módulo de pagamentos caiu em risco alto este mês". O time descobre onde faltam testes sem apontar para ninguém. Perde-se a chance de ver quem precisa de ajuda, mas isso já aparece na revisão, quando alguém lê o código da pessoa. Eu fico com a segunda saída.

### Ideia do vídeo que sustenta a análise

No trecho de 21:52 a 23:30, o Steven Gouveia diz que a explicabilidade sozinha não fecha a lacuna de responsabilidade e que o caráter da organização pesa mais. No relatório por autor, o rastro de cada recomendação estaria lá, explicado, e mesmo assim a responsabilidade escorregaria para o autor do PR, como se o risco alto fosse culpa dele. Só que as regras foram escritas pelo time e o merge foi aprovado por um revisor. Na segunda saída, a responsabilidade fica com quem tomou essas decisões. A outra ideia do trecho, a da dependência da ferramenta, descreve o risco que mais me preocupa no projeto: o revisor que vê "risco baixo" várias vezes seguidas pode parar de ler PR pequeno com atenção, e o modelo erra justamente nos PRs pequenos.

### Reflexão individual

Depois da aula, eu manteria a decisão de deixar o autor fora dos dados e passaria a apagar também o número do PR depois de montar o rótulo, porque, escrevendo esta análise, percebi que o número leva ao autor. Mudaria a contagem de linhas. Eu não tinha notado que um PR com mais teste pode virar risco alto, e isso vai contra a minha própria R5, que pede teste. O argumento que mais pesou foi o da dependência da ferramenta, do vídeo. Eu contava com o rastro e com o aviso de "sugestão" para proteger o revisor de confiar demais, mas um aviso que aparece igual em toda saída tende a ser ignorado depois de algumas semanas, e por isso eu também tiraria a palavra "merge" do texto da R6. Para saber se as mudanças funcionam, eu faria duas coisas. No código, um teste que pega os PRs do dataset, soma linhas de teste a cada um e confere que o risco previsto nunca sobe. No uso real, durante alguns meses, compararia quantos PRs marcados como risco baixo precisaram de revert antes e depois das mudanças, e quanto tempo os revisores passam em PRs pequenos. Se esse tempo cair para quase nada, é sinal de que o time está confiando demais na triagem.

## 4. Declaração de uso de sistemas de IA

### IA incorporada ao projeto

O projeto utiliza uma árvore de decisão (`DecisionTreeClassifier` do scikit-learn, profundidade 2) junto com um sistema especialista de 8 regras (D1 e R0 a R6) para recomendar como revisar um pull request. O sistema recebe as linhas alteradas, os arquivos alterados, se o PR inclui teste e se ele mexe em área crítica, e gera o risco previsto, a porcentagem de risco alto na folha da árvore, a regra aplicada, a recomendação e o rastro da inferência. Verifiquei o funcionamento com a separação em treino e teste (72% de acurácia no teste, com 7 dos 16 PRs de risco alto encontrados), validação cruzada no treino, matriz de confusão, três PRs novos, a troca só da informação de área crítica e testes das regras com casos positivos, negativos e de informação ausente, além de passar as 24 combinações de fatos pelo motor. As limitações identificadas são os dados simulados, o modelo que reaprendeu o corte que eu mesmo coloquei no gerador, os PRs pequenos sem teste que passam como risco baixo, a contagem de linhas que inclui os testes e o motor que para na primeira regra. Pedem revisão com mais cuidado os PRs pequenos sem teste e os PRs pequenos em área crítica, em que a R4 ganha da R5 e o pedido de teste some. A revisão cabe a quem revisa o PR, e as regras são mantidas pelo time.

### IA utilizada na elaboração do trabalho

Utilizei o Claude (Anthropic, modelo Opus 5.5) no trabalho da aula 13 e nesta análise. A ideia de fazer a triagem de pull requests veio de uma sugestão dele, e ele escreveu o script que gera o dataset, o código do notebook, os primeiros rascunhos dos textos do notebook, do arquivo que explica o trabalho no repositório e desta análise, e tirou as capturas de tela da execução no Colab. Também usei o Claude para localizar o trecho do vídeo pela legenda automática do YouTube. Aproveitei o código e os textos depois de rodar o notebook inteiro no Colab, conferir se os números do texto batiam com as saídas, revisar as regras R0 a R6 e o motor até conseguir explicar cada uma, assistir ao trecho do vídeo citado e ajustar os textos ao meu jeito de escrever. Assumo a responsabilidade pelas escolhas, verificações e conteúdo da entrega.

## Referências

BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). Brasília, DF: Presidência da República, 2018. Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm>.

INSTITUTO DE ESTUDOS AVANÇADOS DA USP. *O Estado da Arte em Ética na Inteligência Artificial*. São Paulo: IEA-USP, 9 jun. 2026. 1 vídeo (2h01). Disponível em: <https://www.iea.usp.br/midiateca/video/videos-2026/o-estado-da-arte-em-etica-na-inteligencia-artificial/>.

LACERDA JÚNIOR, Francisco Pires de. Da proibição à governança: uso ético da inteligência artificial generativa na educação superior: uma revisão integrativa (2023–2026). *Revista Foco*, v. 19, n. 8, e12330, p. 1-18, 2026. DOI: 10.54751/revistafoco.v19n8-017.
