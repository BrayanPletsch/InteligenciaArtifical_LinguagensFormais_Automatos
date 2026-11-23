# Atividades práticas da Aula 1

Brayan Aragão Pletsch | RGM 38473585 | Engenharia de Software - N1

Respostas da seção "12. Atividades Práticas" do `Notas_de_Aula.md`.

## Atividade 1: prefixos e sufixos

Palavra: `ab`

Prefixos são os pedaços que começam no início da palavra. Vou tirando símbolos do fim até não sobrar nenhum: `ab`, `a` e, por último, a palavra vazia.

$$
\text{Prefixos}(ab) = \{\varepsilon, a, ab\}
$$

Sufixos são os pedaços que terminam no fim. Agora tiro símbolos do começo: `ab`, `b` e a palavra vazia.

$$
\text{Sufixos}(ab) = \{\varepsilon, b, ab\}
$$

`ε` e a própria palavra `ab` aparecem nos dois conjuntos. `b` não é prefixo, porque `ab` começa com `a`, e `a` não é sufixo, porque `ab` termina com `b`. Uma palavra de tamanho $n$ tem $n + 1$ prefixos e $n + 1$ sufixos; aqui $n = 2$, então são 3 de cada.

## Atividade 2: gramática

$G = (\{S\}, \{a\}, \{S \rightarrow aS \mid \varepsilon\}, S)$

Três palavras geradas, com a derivação:

1. $\varepsilon$: $S \Rightarrow \varepsilon$
2. $a$: $S \Rightarrow aS \Rightarrow a\varepsilon = a$
3. $aa$: $S \Rightarrow aS \Rightarrow aaS \Rightarrow aa\varepsilon = aa$

Cada aplicação de $S \rightarrow aS$ acrescenta um `a`, e $S \rightarrow \varepsilon$ encerra a derivação sem acrescentar nada. A gramática gera qualquer quantidade de `a`, inclusive nenhuma:

$$
L(G) = \{a^n \mid n \geq 0\} = \{\varepsilon, a, aa, aaa, \ldots\}
$$

Nas derivações usei $\Rightarrow$, que indica a aplicação de uma regra. As notas de aula escrevem os passos com $\rightarrow$, mas a tabela de resumo dos exercícios comentados reserva $\rightarrow$ para a produção e $\Rightarrow$ para a derivação.
