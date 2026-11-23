# Máquina de Turing que reconhece 0ⁿ1ⁿ

**Estudante:** Brayan Aragão Pletsch  
**RGM:** 38473585  
**Curso/Turma:** Engenharia de Software - N1 (noturno)  
**Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos  
**Professora:** Kadidja Valéria  
**Aula:** 09 (28/09/2026), Máquinas de Turing

## Arquivos

- Relatório: [entrega/BrayanPletsch_Atividade_MaquinasDeTuring.md](entrega/BrayanPletsch_Atividade_MaquinasDeTuring.md), também em [PDF](entrega/BrayanPletsch_Atividade_MaquinasDeTuring.pdf)
- Máquina do JFLAP: [entrega/maquina_0n1n.jff](entrega/maquina_0n1n.jff)
- Simulador em Python: [entrega/simulador_mt.py](entrega/simulador_mt.py), com os testes em [entrega/test_simulador_mt.py](entrega/test_simulador_mt.py)
- Capturas do JFLAP: [entrega/capturas/](entrega/capturas/)

## O que fiz

Montei no JFLAP 7.1 uma máquina de uma fita que reconhece L = {0ⁿ1ⁿ | n ≥ 1}. A cada volta ela marca um 0 com X e o 1 correspondente com Y, e aceita quando não sobra nada sem par. Considerei n ≥ 1 porque o menor exemplo aceito no enunciado é `01`, então a máquina rejeita a cadeia vazia. O relatório mostra a transição que seria preciso acrescentar se a intenção fosse n ≥ 0.

Rodei os três testes obrigatórios (`0011`, `000111` e `00111`) e os outros exemplos do enunciado, com as configurações passo a passo e as capturas do JFLAP. Nas rejeições, o estado em que a máquina para mostra o motivo. Também contei os passos: 5 para `01`, 13 para `0011`, 25 para `000111` e 41 para `00001111`, o que dá 2n² + 2n + 1.

O simulador em Python lê o mesmo `.jff` e imprime cada configuração. Os testes passam a máquina por todas as 2.047 palavras de 0 e 1 com até 10 símbolos.

Nas partes escritas respondi as perguntas de introdução, a reflexão sobre os limites da computação (o problema da parada) e a questão final, sobre como diferenciar um problema difícil de um problema sem algoritmo.

## Como conferir

Na raiz do repositório:

```
python3 -m unittest discover -s Atividades/05_MaquinasDeTuring/entrega
```

Dentro de `entrega/`:

```
python3 simulador_mt.py 0011 000111 00111
```

São 9 testes.
