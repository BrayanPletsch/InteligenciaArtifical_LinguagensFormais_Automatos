# Gramáticas formais: exercícios da Aula 03 e Lista 1

**Estudante:** Brayan Aragão Pletsch  
**RGM:** 38473585  
**Curso/Turma:** Engenharia de Software - N1 (noturno)  
**Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos  
**Professora:** Kadidja Valéria  
**Aula:** 03 (17/08/2026) e 24/08/2026, Gramáticas formais

## Arquivos

- Exercícios de fixação da Aula 03: [entrega/BrayanPletsch_Exercicios_Fixacao_Aula03.md](entrega/BrayanPletsch_Exercicios_Fixacao_Aula03.md)
- Lista 1: [entrega/BrayanPletsch_Lista1_LinguagensFormais.md](entrega/BrayanPletsch_Lista1_LinguagensFormais.md)
- Lista das atividades da unidade: [AtividadesUnidade2.md](../../Unidade2_GramaticasFormais/AtividadesUnidade2.md), da professora

## O que fiz

Os exercícios de fixação são os do último slide da Aula 03 (17/08). No Bloco 1 derivei `aaab` com S → aS | b e expliquei quando a derivação termina. No Bloco 2 gerei `aaabbb` com S → aSb | ε e mostrei que `aabbb` não sai dessa gramática, porque cada passo coloca um `a` e um `b` juntos e a linguagem é {aⁿbⁿ | n ≥ 0}. No Bloco 3 classifiquei S → aA, A → b como regular (Tipo 3). O slide escreve essa gramática como `S → aA | A → b`, e eu li o `|` como separador de duas regras; a explicação está no arquivo.

A Lista 1 (24/08) tem os dez exercícios do material "Exercícios Comentados, Aulas 01 e 02" e o desafio final. No desafio conferi quais palavras S → aS | b gera e cheguei a L(G) = {aⁿb | n ≥ 0}. No fim da lista explico a diferença entre → (regra de produção) e ⇒ (passo de derivação), que usei em todas as respostas.
