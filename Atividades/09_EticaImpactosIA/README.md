# Ética e impactos da IA na triagem de pull requests

**Estudante:** Brayan Aragão Pletsch  
**RGM:** 38473585  
**Curso/Turma:** Engenharia de Software - N1 (noturno)  
**Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos  
**Professora:** Kadidja Valéria  
**Aula:** 16/11/2026, Ética e implicações em IA (A1, 0,5 pt)

## Arquivos

- Análise: [entrega/BrayanPletsch_Atividade_EticaImpactosIA.md](entrega/BrayanPletsch_Atividade_EticaImpactosIA.md), também em [PDF](entrega/BrayanPletsch_Atividade_EticaImpactosIA.pdf)
- Projeto analisado: [08_AprendizadoSupervisionado](../08_AprendizadoSupervisionado/)

## O que fiz

A atividade pede uma análise ética do projeto da disciplina. Analisei o sistema de triagem de pull requests da atividade 08, seguindo as quatro partes do enunciado.

Na leitura, usei o artigo de Lacerda Júnior (*Revista Foco*, 2026) para discutir a integridade acadêmica: quem usa IA precisa conseguir explicar as decisões do próprio trabalho. Do vídeo do IEA-USP escolhi o trecho de 21:52 a 23:30, em que o Steven Gouveia diz que a explicabilidade sozinha não define quem responde pelo erro.

Na análise do projeto montei a tabela com os cinco aspectos (privacidade, viés, transparência, supervisão e impacto social). Ao fazer a análise percebi um problema que não tinha visto no projeto: as linhas de teste contam como linhas alteradas, então escrever mais teste pode fazer um PR passar de risco baixo para risco alto.

O dilema é se o líder técnico deveria ver um relatório de risco por autor. Escolhi mostrar só o resultado por módulo, sem o autor, e a reflexão individual explica o que eu manteria e o que mudaria no sistema. No fim estão as duas declarações de uso de IA.
