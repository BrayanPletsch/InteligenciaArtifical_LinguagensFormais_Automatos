# Atividades práticas da Aula 1: prefixos, sufixos e gramática

**Estudante:** Brayan Aragão Pletsch  
**RGM:** 38473585  
**Curso/Turma:** Engenharia de Software - N1 (noturno)  
**Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos  
**Professora:** Kadidja Valéria  
**Aula:** 1 (10/08/2026), Linguagens formais e gramáticas

## Arquivo

- Respostas: [entrega/BrayanPletsch_Atividades_Aula1.md](entrega/BrayanPletsch_Atividades_Aula1.md)
- Enunciado: seção "12. Atividades Práticas" do [Notas_de_Aula.md](../../Unidade1_LinguagensFormais/Notas_de_Aula.md) da professora

## O que fiz

Na primeira atividade listei os prefixos e os sufixos da palavra `ab`. Os prefixos são {ε, a, ab} e os sufixos são {ε, b, ab}. Também expliquei por que `b` não é prefixo e `a` não é sufixo, e que uma palavra de tamanho n tem n + 1 prefixos e n + 1 sufixos.

Na segunda, usei a gramática S → aS | ε para gerar três palavras (ε, `a` e `aa`), escrevendo a derivação de cada uma. Como S → aS acrescenta um `a` por vez e S → ε encerra a derivação, a gramática gera qualquer quantidade de `a`, inclusive nenhuma: L(G) = {aⁿ | n ≥ 0}.
