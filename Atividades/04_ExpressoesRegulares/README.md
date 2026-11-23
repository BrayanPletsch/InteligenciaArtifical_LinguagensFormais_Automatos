# Expressões regulares: matrícula acadêmica e validação de e-mail

**Estudante:** Brayan Aragão Pletsch  
**RGM:** 38473585  
**Curso/Turma:** Engenharia de Software - N1 (noturno)  
**Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos  
**Professora:** Kadidja Valéria  
**Aula:** 05, Expressões regulares

## Arquivos

- Relatório: [entrega/BrayanPletsch_Atividade_ExpressoesRegulares.md](entrega/BrayanPletsch_Atividade_ExpressoesRegulares.md)
- Padrões da atividade: [entrega/padroes_regex.py](entrega/padroes_regex.py)
- Programa do tutorial de e-mail: [entrega/validador_email.py](entrega/validador_email.py)
- Testes: [entrega/test_padroes_regex.py](entrega/test_padroes_regex.py)
- Capturas do Regex Learn: [entrega/capturas/](entrega/capturas/)

## O que fiz

Resolvi os três exercícios guiados do material (sufixo `00`, exatamente dois `a` e identificador acadêmico) e o desafio final, a regex do código de matrícula:

```
^(CCO|ESW|SIS)-202[4-9]-[0-9]{4}-[MTN]$
```

No Regex Learn testei a versão final com 18 cadeias e mais duas versões com erro, uma sem os parênteses e outra com `+` no número. Na versão sem parênteses a alternância pega só o trecho `CCO`, e o relatório mostra o motivo de cada falha. O AFD equivalente a essa regex ficou na atividade 03.

Da parte do tutorial de e-mail, escrevi o programa da seção 10. Além de dizer se o e-mail é válido, ele explica por que um e-mail foi rejeitado. No fim do relatório respondi as sete perguntas de reflexão, entre elas a relação entre ER, NFA e DFA e o motivo de {aⁿbⁿ} não ser regular.

Todos os resultados do relatório saíram da execução dos padrões em Python com `re.fullmatch`.

## Como conferir

```
cd Atividades/04_ExpressoesRegulares/entrega
python3 -m unittest -v test_padroes_regex
python3 validador_email.py
```

São 21 testes.
