"""Simulador de Máquina de Turing de uma fita que lê a máquina de um arquivo .jff do JFLAP.

Exemplos de uso::

    python3 simulador_mt.py 0011 000111 00111
    python3 simulador_mt.py --maquina outra_maquina.jff 01
    python3 simulador_mt.py ""        # cadeia vazia
"""

import argparse
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

BRANCO = "□"
MAQUINA_PADRAO = Path(__file__).with_name("maquina_0n1n.jff")
LIMITE_PASSOS = 10_000
DESLOCAMENTO = {"L": -1, "R": 1, "S": 0}


@dataclass(frozen=True)
class Transicao:
    destino: str
    escreve: str
    move: str


@dataclass(frozen=True)
class MaquinaTuring:
    inicial: str
    finais: frozenset
    transicoes: dict


@dataclass(frozen=True)
class Configuracao:
    estado: str
    fita: str
    cabeca: int

    @property
    def simbolo_lido(self) -> str:
        return self.fita[self.cabeca]

    def __str__(self) -> str:
        esquerda = self.fita[:self.cabeca]
        direita = self.fita[self.cabeca + 1:]
        return f"{esquerda}[{self.simbolo_lido}]{direita}"


@dataclass(frozen=True)
class Execucao:
    aceita: bool
    configuracoes: list

    @property
    def estados(self) -> list:
        return [configuracao.estado for configuracao in self.configuracoes]


def _simbolo(elemento) -> str:
    # O JFLAP grava o branco como tag vazia (<read/>, <write/>).
    texto = elemento.text if elemento is not None else None
    return texto if texto else BRANCO


def carregar_jff(caminho) -> MaquinaTuring:
    """Lê uma Máquina de Turing determinística de uma fita salva pelo JFLAP."""
    raiz = ET.parse(caminho).getroot()
    if raiz.findtext("type") != "turing":
        raise ValueError(f"{caminho} não contém uma Máquina de Turing")
    if raiz.findtext("tapes", "1") != "1":
        raise ValueError("o simulador só trata máquinas de uma fita")

    automato = raiz.find("automaton")
    # JFLAP 7.1 grava <state>; o 6.x gravava cada estado como <block>.
    elementos_estado = automato.findall("state") + automato.findall("block")

    nomes = {}
    iniciais = []
    finais = set()
    for elemento in elementos_estado:
        identificador = elemento.get("id")
        nome = elemento.get("name") or f"q{identificador}"
        nomes[identificador] = nome
        if elemento.find("initial") is not None:
            iniciais.append(nome)
        if elemento.find("final") is not None:
            finais.add(nome)

    if len(iniciais) != 1:
        raise ValueError(f"esperado um estado inicial, encontrado(s) {len(iniciais)}")

    transicoes = {}
    for elemento in automato.findall("transition"):
        origem = nomes[elemento.findtext("from")]
        lido = _simbolo(elemento.find("read"))
        if (origem, lido) in transicoes:
            raise ValueError(f"máquina não determinística em ({origem}, {lido})")
        transicoes[(origem, lido)] = Transicao(
            destino=nomes[elemento.findtext("to")],
            escreve=_simbolo(elemento.find("write")),
            move=elemento.findtext("move", "R"),
        )

    return MaquinaTuring(iniciais[0], frozenset(finais), transicoes)


def _configuracao(estado: str, fita: dict, cabeca: int) -> Configuracao:
    posicoes = [*fita, cabeca]
    inicio, fim = min(posicoes), max(posicoes)
    conteudo = "".join(fita.get(i, BRANCO) for i in range(inicio, fim + 1))
    return Configuracao(estado, conteudo, cabeca - inicio)


def executar(maquina: MaquinaTuring, palavra: str, limite: int = LIMITE_PASSOS) -> Execucao:
    """Executa a máquina sobre a palavra e devolve todas as configurações percorridas.

    Segue a convenção do JFLAP: aceita ao entrar em um estado final e rejeita
    quando para em um estado não final por falta de transição.
    """
    fita = dict(enumerate(palavra))
    cabeca = 0
    estado = maquina.inicial
    configuracoes = [_configuracao(estado, fita, cabeca)]

    passos = 0
    while estado not in maquina.finais:
        transicao = maquina.transicoes.get((estado, fita.get(cabeca, BRANCO)))
        if transicao is None:
            return Execucao(False, configuracoes)
        # Uma MT pode nunca parar, e não há como detectar isso em geral;
        # o limite só impede que o simulador fique preso para sempre.
        if passos == limite:
            raise RuntimeError(f"a máquina não parou em {limite} passos")

        fita[cabeca] = transicao.escreve
        cabeca += DESLOCAMENTO[transicao.move]
        estado = transicao.destino
        configuracoes.append(_configuracao(estado, fita, cabeca))
        passos += 1

    return Execucao(True, configuracoes)


def formatar(palavra: str, execucao: Execucao) -> str:
    linhas = [f"Entrada: {palavra or 'ε'}"]
    for passo, configuracao in enumerate(execucao.configuracoes):
        linhas.append(f"  {passo:>3}  {configuracao.estado:<3} {configuracao}")

    linhas.append("Estados: " + " → ".join(execucao.estados))
    if execucao.aceita:
        linhas.append("Resultado: ACEITA")
    else:
        ultima = execucao.configuracoes[-1]
        linhas.append(
            f"Resultado: REJEITA (parou em {ultima.estado} lendo "
            f"{ultima.simbolo_lido}, sem transição definida)"
        )
    return "\n".join(linhas)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("palavras", nargs="+", help='palavras de entrada ("" para a cadeia vazia)')
    parser.add_argument("--maquina", type=Path, default=MAQUINA_PADRAO, help="arquivo .jff")
    argumentos = parser.parse_args()

    maquina = carregar_jff(argumentos.maquina)
    saidas = [formatar(p, executar(maquina, p)) for p in argumentos.palavras]
    print("\n\n".join(saidas))


if __name__ == "__main__":
    main()
