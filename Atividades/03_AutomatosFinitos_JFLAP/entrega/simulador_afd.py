"""Simulador de AFD que lê o arquivo .jff salvo pelo JFLAP 7.

Uso: python3 simulador_afd.py automato.jff cadeia [cadeia ...]
Use "" para testar a cadeia vazia.
"""

import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass

ESTADO_SUMIDOURO = "qerro"


@dataclass(frozen=True)
class AFD:
    nomes: dict[str, str]
    inicial: str
    finais: frozenset[str]
    transicoes: dict[tuple[str, str], str]

    @property
    def alfabeto(self) -> list[str]:
        return sorted({simbolo for _, simbolo in self.transicoes})

    def destino(self, estado: str, simbolo: str) -> str | None:
        return self.transicoes.get((estado, simbolo))


def carregar_jff(caminho: str) -> AFD:
    """Lê um autômato finito do JFLAP e confere se ele é determinístico."""
    raiz = ET.parse(caminho).getroot()
    if raiz.findtext("type") != "fa":
        raise ValueError(f"{caminho}: o arquivo não é um autômato finito (<type>fa</type>)")
    automato = raiz.find("automaton")

    nomes = {}
    iniciais = []
    finais = set()
    for estado in automato.iter("state"):
        identificador = estado.get("id")
        nomes[identificador] = estado.get("name")
        if estado.find("initial") is not None:
            iniciais.append(identificador)
        if estado.find("final") is not None:
            finais.add(identificador)
    if len(iniciais) != 1:
        raise ValueError(f"{caminho}: o AFD precisa de exatamente um estado inicial")

    transicoes = {}
    for transicao in automato.iter("transition"):
        origem = transicao.findtext("from")
        destino = transicao.findtext("to")
        simbolo = transicao.findtext("read") or ""
        if len(simbolo) != 1:
            raise ValueError(
                f"{caminho}: transição de {nomes[origem]} lê {simbolo!r}; "
                "em um AFD cada transição lê exatamente um símbolo"
            )
        if (origem, simbolo) in transicoes:
            raise ValueError(
                f"{caminho}: {nomes[origem]} tem mais de uma transição com {simbolo!r}"
            )
        transicoes[(origem, simbolo)] = destino

    return AFD(nomes, iniciais[0], frozenset(finais), transicoes)


def executar(afd: AFD, cadeia: str) -> tuple[bool, list[str]]:
    """Processa a cadeia e devolve (aceita, nomes dos estados percorridos).

    O JFLAP deixa de fora as transições para o sumidouro; aqui elas levam
    a ESTADO_SUMIDOURO, que não é final e prende o autômato até o fim da
    cadeia, por isso a leitura para ali.
    """
    atual = afd.inicial
    caminho = [afd.nomes[atual]]
    for simbolo in cadeia:
        atual = afd.destino(atual, simbolo)
        if atual is None:
            caminho.append(ESTADO_SUMIDOURO)
            return False, caminho
        caminho.append(afd.nomes[atual])
    return atual in afd.finais, caminho


def main(argumentos: list[str]) -> int:
    if len(argumentos) < 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    afd = carregar_jff(argumentos[0])
    for cadeia in argumentos[1:]:
        aceita, caminho = executar(afd, cadeia)
        rotulo = cadeia if cadeia else "ε"
        print(f"{rotulo}: {' -> '.join(caminho)}  {'ACEITA' if aceita else 'REJEITA'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
