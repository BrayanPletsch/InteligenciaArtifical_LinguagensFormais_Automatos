# Lista 1: Linguagens Formais e Autômatos

Brayan Aragão Pletsch | RGM 38473585 | Engenharia de Software - N1

Exercícios para o estudante do material "Exercícios Comentados, Aulas 01 e 02" (aula de 24/08), incluindo o desafio final.

## Exercício 1

$\Sigma = \{a, b, c\}$

1. O alfabeto tem 3 símbolos.
2. Os símbolos são $a$, $b$ e $c$.
3. Sim, $a \in \Sigma$.
4. Não, $d \notin \Sigma$.
5. `cab`. Qualquer sequência finita só com $a$, $b$ e $c$ serviria, como `abc` ou `bbca`.

## Exercício 2

$\Sigma = \{0, 1\}$

| Sequência | Válida? | Justificativa |
| --------- | ------- | ------------- |
| `0101`    | Sim     | Só usa `0` e `1`. |
| `00110`   | Sim     | Só usa `0` e `1`. |
| `012`     | Não     | O `2` não está em $\Sigma$. |
| `111`     | Sim     | Repetir o mesmo símbolo é permitido. |
| `10a`     | Não     | O `a` não está em $\Sigma$. |

Basta um símbolo de fora do alfabeto para a sequência deixar de ser palavra sobre $\Sigma$.

## Exercício 3

$\Sigma = \{0, 1\}$

1. $0 \in \Sigma$: verdadeiro, `0` é um dos dois símbolos.
2. $1 \in \Sigma$: verdadeiro, pelo mesmo motivo.
3. $01 \in \Sigma$: falso. `01` tem dois símbolos, então é uma palavra. $\Sigma$ só contém símbolos soltos.
4. $01 \in \Sigma^*$: verdadeiro. $\Sigma^*$ reúne todas as palavras formadas com `0` e `1`, e `01` é uma delas.
5. $2 \in \Sigma$: falso, `2` não faz parte do alfabeto.
6. $101 \in \Sigma^*$: verdadeiro, os três símbolos de `101` pertencem a $\Sigma$.

A diferença entre os itens 3 e 4 é o que o exercício quer mostrar: a mesma sequência `01` não pertence a $\Sigma$, mas pertence a $\Sigma^*$.

## Exercício 4

$L = \{0, 01, 011, 0111\}$

| Palavra | Pertence a $L$? | Justificativa |
| ------- | --------------- | ------------- |
| `0`     | Sim | Primeiro elemento de $L$. |
| `01`    | Sim | Está listada em $L$. |
| `0111`  | Sim | Último elemento de $L$. |
| `10`    | Não | Usa os mesmos símbolos de `01`, mas a ordem é outra, e `10` não aparece no conjunto. |
| `111`   | Não | Não está listada. Todas as palavras de $L$ começam com `0`. |
| `011`   | Sim | Está listada em $L$. |

Como $L$ é finita e foi dada por extensão, a pertinência se decide olhando a lista. Ser formada com símbolos do alfabeto não basta.

## Exercício 5

$L = \{b^n \mid n \geq 1\}$

1. As cinco primeiras palavras, para $n = 1, \ldots, 5$: `b`, `bb`, `bbb`, `bbbb`, `bbbbb`.
2. $b^n$ é o símbolo `b` escrito $n$ vezes seguidas. Não é potência numérica: $b^3$ é a palavra `bbb`.
3. Sim. `bbbbbb` tem seis `b`, então é $b^6$, e $6 \geq 1$.
4. Não. A palavra vazia corresponderia a $b^0$, e a condição exige $n \geq 1$.

## Exercício 6

$L = \emptyset$ é a linguagem que não tem palavra nenhuma. $L = \{\varepsilon\}$ tem exatamente uma palavra, a palavra vazia. As duas parecem "vazias", mas uma é um conjunto sem elementos e a outra é um conjunto com um elemento, que por acaso tem tamanho zero.

1. $L = \{\varepsilon\}$ possui uma palavra.
2. $L = \emptyset$ não possui nenhuma palavra.
3. $|\varepsilon| = 0$.

## Exercício 7

$G = (\{S, A\}, \{0, 1\}, P, S)$ com $P = \{S \rightarrow 0A,\ A \rightarrow 1\}$

1. Variáveis: $V = \{S, A\}$
2. Terminais: $T = \{0, 1\}$
3. Produções: $P = \{S \rightarrow 0A,\ A \rightarrow 1\}$
4. Símbolo inicial: $S$
5. A única palavra gerada é `01`:

$$
S \Rightarrow 0A \Rightarrow 01
$$

Nenhuma regra é recursiva, então não existe outra derivação possível e $L(G) = \{01\}$.

## Exercício 8

Regra $S \rightarrow 0S$, começando em $S$:

1. Uma vez: $S \Rightarrow 0S$
2. Duas vezes: $S \Rightarrow 0S \Rightarrow 00S$
3. Três vezes: $S \Rightarrow 0S \Rightarrow 00S \Rightarrow 000S$
4. Sequência completa:

$$
S \Rightarrow 0S \Rightarrow 00S \Rightarrow 000S
$$

A forma $000S$ ainda tem o não terminal $S$, então não é uma palavra da linguagem. Com essa regra sozinha a derivação nunca termina, porque não há produção que troque $S$ por terminais.

## Exercício 9

$G: S \rightarrow aS \mid b$, gerar `aaab`:

1. Começo em $S$.
2. $S \rightarrow aS$ produz o primeiro `a`: $S \Rightarrow aS$
3. $S \rightarrow aS$ de novo: $aS \Rightarrow aaS$
4. Mais uma vez: $aaS \Rightarrow aaaS$
5. $S \rightarrow b$ fecha a palavra: $aaaS \Rightarrow aaab$

$$
S \Rightarrow aS \Rightarrow aaS \Rightarrow aaaS \Rightarrow aaab
$$

## Exercício 10

$G: S \rightarrow 0S \mid 1$

| Palavra | Gerada? | Derivação ou justificativa |
| ------- | ------- | -------------------------- |
| `1`     | Sim | $S \Rightarrow 1$ |
| `01`    | Sim | $S \Rightarrow 0S \Rightarrow 01$ |
| `001`   | Sim | $S \Rightarrow 0S \Rightarrow 00S \Rightarrow 001$ |
| `0001`  | Sim | $S \Rightarrow 0S \Rightarrow 00S \Rightarrow 000S \Rightarrow 0001$ |
| `101`   | Não | O `1` só aparece pela regra $S \rightarrow 1$, que elimina o $S$. Depois dele não sobra variável para gerar mais nada. |
| `1001`  | Não | Mesmo motivo: a palavra continua depois do primeiro `1`, e isso a gramática não permite. |

As palavras geradas são zero ou mais `0` seguidos de um único `1` no final, ou seja, $L(G) = \{0^n1 \mid n \geq 0\}$.

## Desafio final

$G: S \rightarrow aS \mid b$

1. `b`: sim, $S \Rightarrow b$.
2. `ab`: sim, $S \Rightarrow aS \Rightarrow ab$.
3. `aab`: sim, $S \Rightarrow aS \Rightarrow aaS \Rightarrow aab$.
4. `aaab`: sim, $S \Rightarrow aS \Rightarrow aaS \Rightarrow aaaS \Rightarrow aaab$.
5. `aba`: não. O `b` só entra pela regra $S \rightarrow b$, que encerra a derivação, então nenhuma palavra gerada tem símbolo depois do `b`.
6. Derivação de `aaaab`:

$$
S \Rightarrow aS \Rightarrow aaS \Rightarrow aaaS \Rightarrow aaaaS \Rightarrow aaaab
$$

7. Cada uso de $S \rightarrow aS$ coloca um `a` à esquerda do $S$, e a única saída é trocar o $S$ por `b`. Por isso as palavras são uma quantidade qualquer de `a` (inclusive nenhuma) seguida de exatamente um `b`:

$$
L(G) = \{a^nb \mid n \geq 0\}
$$

É a mesma linguagem que aparece no slide de gramáticas regulares da Aula 03.

## Sobre $\rightarrow$ e $\Rightarrow$

Nas respostas usei $\rightarrow$ para a regra de produção ("$S$ produz $aS$") e $\Rightarrow$ para um passo de derivação, quando uma regra é aplicada a uma forma sentencial ("$S$ deriva $aS$"), seguindo a tabela de resumo do material.
