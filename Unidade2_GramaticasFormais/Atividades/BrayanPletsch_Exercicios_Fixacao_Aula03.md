# Exercícios práticos para fixação da Aula 03 (Gramáticas Formais)

Brayan Aragão Pletsch | RGM 38473585 | Engenharia de Software - N1

Exercícios do último slide da Aula 03 (17/08), imagem `Exercicio_GramaticasFormais_Aula3.png`.

## Bloco 1 (Derivação)

$G_1: S \rightarrow aS \mid b$

### A) Gere a palavra $aaab$

$$
S \Rightarrow aS \Rightarrow aaS \Rightarrow aaaS \Rightarrow aaab
$$

Apliquei $S \rightarrow aS$ três vezes, uma para cada `a`, e terminei com $S \rightarrow b$.

### B) Explique como você sabe que a derivação terminou

Terminou porque a forma $aaab$ só tem terminais. Enquanto o $S$ estava presente ainda dava para aplicar uma das duas regras. Quando usei $S \rightarrow b$, o $S$ foi substituído por um terminal e não sobrou nenhum lado esquerdo de produção para reescrever. É o critério da aula: a derivação acaba quando não existem mais variáveis.

## Bloco 2 (GLC)

$G_2: S \rightarrow aSb \mid \varepsilon$

### A) Gere a palavra $aaabbb$

$$
S \Rightarrow aSb \Rightarrow aaSbb \Rightarrow aaaSbbb \Rightarrow aaa\varepsilon bbb \Rightarrow aaabbb
$$

$S \rightarrow aSb$ foi aplicada três vezes, sempre no $S$ do meio, e depois $S \rightarrow \varepsilon$ apagou a variável. Como $\varepsilon$ não ocupa espaço, $aaa\varepsilon bbb$ é a palavra $aaabbb$.

### B) É possível gerar $aabbb$? Justifique

Não. A única regra que produz terminais é $S \rightarrow aSb$, e ela coloca um `a` e um `b` ao mesmo tempo. A outra regra, $S \rightarrow \varepsilon$, não acrescenta nada. Então toda palavra gerada tem a mesma quantidade de `a` e de `b`, com os `a` antes:

$$
L(G_2) = \{a^nb^n \mid n \geq 0\} = \{\varepsilon, ab, aabb, aaabbb, \ldots\}
$$

$aabbb$ tem 2 `a` e 3 `b`. Tentando derivar, depois de $S \Rightarrow aSb \Rightarrow aaSbb$ a única forma de fechar é $aabb$; mais um passo já dá $aaaSbbb$, com um `a` a mais. A contagem nunca bate.

## Bloco 3 (Classificação)

$S \rightarrow aA \mid A \rightarrow b$

Li o $\mid$ do slide como separador das duas regras, ou seja, $P = \{S \rightarrow aA,\ A \rightarrow b\}$.

Classificação: regular (Tipo 3).

As duas produções seguem o formato restrito das gramáticas regulares visto na aula: do lado direito há um terminal seguido de no máximo uma variável, sempre na ponta direita ($S \rightarrow aA$), ou só um terminal ($A \rightarrow b$). A palavra cresce para um lado só, como no exemplo $S \rightarrow aS \mid b$. Não há nada parecido com $aSb$, em que a variável fica no meio e a gramática precisa "lembrar" quantos `a` gerou para colocar a mesma quantidade de `b`.

Ela também é livre de contexto, porque todo lado esquerdo é um único não terminal e, pela Hierarquia de Chomsky, Tipo 3 $\subset$ Tipo 2. A classificação mais específica é regular. Essa gramática gera apenas a palavra `ab` ($S \Rightarrow aA \Rightarrow ab$), e uma linguagem regular pode ser reconhecida por um autômato finito.
