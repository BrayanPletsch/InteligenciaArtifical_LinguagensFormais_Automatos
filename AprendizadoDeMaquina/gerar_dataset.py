"""Gera o dataset simulado de pull requests usado no notebook da atividade.

Os dados NÃO vêm de um repositório real. Cada linha é um PR inventado, e o
rótulo é sorteado a partir de uma chance de dar problema que eu defini abaixo.
A semente é fixa, então rodar de novo gera exatamente o mesmo CSV.

Uso:
    python gerar_dataset.py
"""

import csv
import math
import random
from pathlib import Path

SEMENTE = 2026
QUANTIDADE = 200
ARQUIVO = Path(__file__).with_name("dataset_pull_requests.csv")


def chance_de_problema(linhas, arquivos, inclui_testes):
    """Chance de o PR precisar de revert ou hotfix em até 14 dias após o merge.

    Os pesos são uma suposição minha, não foram medidos:
    - todo PR tem uma chance pequena de dar problema (5%);
    - passar de 300 linhas aumenta bastante a chance, e passar de 800 aumenta mais;
    - mexer em muitos arquivos (mais de 12) espalha a mudança pelo sistema;
    - PR sem teste novo ou alterado é o fator que mais pesa.
    """
    p = 0.05
    if linhas > 300:
        p += 0.35
    if linhas > 800:
        p += 0.15
    if arquivos > 12:
        p += 0.10
    if not inclui_testes:
        p += 0.40
    return min(p, 0.95)


def gerar(semente=SEMENTE, quantidade=QUANTIDADE):
    rng = random.Random(semente)
    linhas_csv = []
    for i in range(1, quantidade + 1):
        # Tamanho do PR: a maioria é pequena e alguns são enormes, por isso o
        # sorteio é log-normal (mediana perto de 130 linhas).
        linhas = round(math.exp(rng.gauss(math.log(130), 1.1)))
        linhas = min(max(linhas, 2), 2500)

        # Arquivos acompanham o tamanho, com variação de 15 a 60 linhas por arquivo.
        arquivos = max(1, round(linhas / rng.uniform(15, 60)))
        arquivos = min(arquivos, 60)

        inclui_testes = 1 if rng.random() < 0.55 else 0
        if inclui_testes:
            # Se tem teste, tem pelo menos o arquivo alterado e o arquivo de teste.
            arquivos = max(arquivos, 2)

        p = chance_de_problema(linhas, arquivos, inclui_testes)
        risco = "alto" if rng.random() < p else "baixo"

        linhas_csv.append({
            "id_pr": f"PR-{i:03d}",
            "linhas_alteradas": linhas,
            "arquivos_alterados": arquivos,
            "inclui_testes": inclui_testes,
            "risco": risco,
        })
    return linhas_csv


def main():
    dados = gerar()
    with ARQUIVO.open("w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=list(dados[0].keys()))
        escritor.writeheader()
        escritor.writerows(dados)
    altos = sum(1 for d in dados if d["risco"] == "alto")
    print(f"{len(dados)} PRs gravados em {ARQUIVO.name} ({altos} alto, {len(dados) - altos} baixo)")


if __name__ == "__main__":
    main()
