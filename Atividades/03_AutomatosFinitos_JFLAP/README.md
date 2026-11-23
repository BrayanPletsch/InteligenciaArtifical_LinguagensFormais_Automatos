# Autômatos finitos determinísticos no JFLAP

**Estudante:** Brayan Aragão Pletsch  
**RGM:** 38473585  
**Curso/Turma:** Engenharia de Software - N1 (noturno)  
**Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos  
**Professora:** Kadidja Valéria  
**Aula:** 31/08/2026, Autômatos finitos determinísticos (exercícios das Aulas 04 e 5)

## Arquivos

- Relatório com os cinco AFDs: [entrega/BrayanPletsch_Exercicios_AFD_JFLAP.md](entrega/BrayanPletsch_Exercicios_AFD_JFLAP.md)
- Autômatos do JFLAP: [afd_termina_em_1.jff](entrega/afd_termina_em_1.jff), [afd_termina_em_00.jff](entrega/afd_termina_em_00.jff), [afd_exemplo_pratico_1.jff](entrega/afd_exemplo_pratico_1.jff), [afd_dois_zeros_consecutivos.jff](entrega/afd_dois_zeros_consecutivos.jff) e [afd_matricula.jff](entrega/afd_matricula.jff)
- Simulador em Python: [entrega/simulador_afd.py](entrega/simulador_afd.py), com os testes em [entrega/test_simulador_afd.py](entrega/test_simulador_afd.py)
- Capturas do JFLAP: [entrega/capturas/](entrega/capturas/)

## O que fiz

A lista oficial do JFLAP para 31/08 não foi publicada, e o `AtividadesUnidade2.md` marca essa atividade como pendente. Por isso montei os AFDs que os próprios slides das Aulas 04 e 5 propõem: palavras binárias que terminam em 1, palavras que terminam com 00 (a atividade prática da Aula 04), o AFD do Exemplo Prático 1 com as cinco cadeias do slide e palavras com pelo menos dois 0 seguidos. O quinto é o AFD equivalente à regex de matrícula do material de expressões regulares (atividade 04).

Cada autômato tem a definição formal, a tabela de transição e os caminhos de estados das cadeias testadas. Rodei todas as cadeias no JFLAP 7.1 com Input > Multiple Run, e o resultado foi o mesmo do relatório.

Também escrevi um simulador que lê o próprio `.jff`, confere se o autômato é determinístico e mostra o caminho de cada cadeia. Os testes comparam cada AFD binário com a definição da linguagem em todas as palavras de até 12 símbolos e conferem que o AFD da matrícula dá o mesmo resultado que a regex da atividade 04 em 2.370 matrículas.

## Como conferir

```
cd Atividades/03_AutomatosFinitos_JFLAP/entrega
python3 -m unittest -v test_simulador_afd
python3 simulador_afd.py afd_termina_em_00.jff 100 1001
```

São 12 testes. Um deles usa o `padroes_regex.py` da atividade 04, então as duas pastas precisam estar no repositório.
