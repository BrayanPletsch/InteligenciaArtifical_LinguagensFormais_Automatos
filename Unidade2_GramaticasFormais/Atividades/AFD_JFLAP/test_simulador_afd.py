import importlib.util
import itertools
import os
import tempfile
import unittest
from pathlib import Path

from simulador_afd import ESTADO_SUMIDOURO, carregar_jff, executar

PASTA = Path(__file__).resolve().parent
RAIZ_DO_REPOSITORIO = PASTA.parents[2]


def carrega(nome):
    return carregar_jff(str(PASTA / nome))


def binarias_ate(tamanho):
    for n in range(tamanho + 1):
        for simbolos in itertools.product("01", repeat=n):
            yield "".join(simbolos)


def termina_em_1(w):
    return w.endswith("1")


def termina_em_00(w):
    return w.endswith("00")


def tem_00(w):
    return "00" in w


def linguagem_exemplo_pratico_1(w):
    """Tem pelo menos um 1 e, depois do último 1, uma quantidade par de 0."""
    if "1" not in w:
        return False
    zeros_no_fim = len(w) - 1 - w.rindex("1")
    return zeros_no_fim % 2 == 0


class AutomatosBinariosTest(unittest.TestCase):
    CASOS = {
        "afd_termina_em_1.jff": termina_em_1,
        "afd_termina_em_00.jff": termina_em_00,
        "afd_exemplo_pratico_1.jff": linguagem_exemplo_pratico_1,
        "afd_dois_zeros_consecutivos.jff": tem_00,
    }

    def test_funcao_de_transicao_total(self):
        for arquivo in self.CASOS:
            afd = carrega(arquivo)
            for estado in afd.nomes:
                for simbolo in "01":
                    with self.subTest(arquivo=arquivo, estado=afd.nomes[estado], simbolo=simbolo):
                        self.assertIsNotNone(afd.destino(estado, simbolo))

    def test_linguagem_reconhecida_ate_tamanho_12(self):
        for arquivo, pertence in self.CASOS.items():
            afd = carrega(arquivo)
            for palavra in binarias_ate(12):
                with self.subTest(arquivo=arquivo, palavra=palavra):
                    self.assertEqual(executar(afd, palavra)[0], pertence(palavra))

    def test_cadeias_do_exemplo_pratico_1(self):
        afd = carrega("afd_exemplo_pratico_1.jff")
        esperado = {
            "1": True,
            "0011001": True,
            "010010": False,
            "1101": True,
            "000011010": False,
        }
        for cadeia, aceita in esperado.items():
            with self.subTest(cadeia=cadeia):
                self.assertEqual(executar(afd, cadeia)[0], aceita)

    def test_caminho_da_palavra_101_do_slide(self):
        afd = carrega("afd_termina_em_1.jff")
        self.assertEqual(executar(afd, "101"), (True, ["q0", "q1", "q0", "q1"]))


def carrega_padroes_regex():
    caminho = RAIZ_DO_REPOSITORIO / "Expressoes_Regulares" / "Atividades" / "padroes_regex.py"
    especificacao = importlib.util.spec_from_file_location("padroes_regex", caminho)
    modulo = importlib.util.module_from_spec(especificacao)
    especificacao.loader.exec_module(modulo)
    return modulo


class AutomatoMatriculaTest(unittest.TestCase):
    ACEITOS = [
        "CCO-2024-0001-M",
        "ESW-2026-1042-N",
        "SIS-2029-9999-T",
        "CCO-2027-0100-N",
        "ESW-2025-4321-M",
        "ESW-2024-0000-T",
        "SIS-2029-0042-N",
    ]
    REJEITADOS = [
        "ADS-2026-0001-N",
        "CCO-2030-0001-M",
        "SIS-2027-123-N",
        "esw-2026-1042-N",
        "CCO/2026/0001/M",
        "CCO-2026-0001-X",
        "ESW-2023-1042-N",
        "ESW-2026-10420-N",
        "CCO-2026-0001-MN",
        "",
    ]

    @classmethod
    def setUpClass(cls):
        cls.afd = carrega("afd_matricula.jff")

    def test_casos_do_material_e_criados(self):
        for cadeia in self.ACEITOS:
            with self.subTest(cadeia=cadeia):
                self.assertTrue(executar(self.afd, cadeia)[0])
        for cadeia in self.REJEITADOS:
            with self.subTest(cadeia=cadeia):
                self.assertFalse(executar(self.afd, cadeia)[0])

    def test_unico_estado_final(self):
        self.assertEqual([self.afd.nomes[e] for e in self.afd.finais], ["qF"])

    def test_simbolo_extra_vai_para_o_sumidouro(self):
        aceita, caminho = executar(self.afd, "CCO-2026-0001-MN")
        self.assertFalse(aceita)
        self.assertEqual(caminho[-2:], ["qF", ESTADO_SUMIDOURO])

    def test_equivalente_a_regex_da_atividade(self):
        padroes = carrega_padroes_regex()
        simbolos = "CEOSWIADMTNX0123456789-/c "
        cadeias = set(self.ACEITOS + self.REJEITADOS)
        for base in self.ACEITOS[:3]:
            for i in range(len(base) + 1):
                cadeias.add(base[:i] + base[i + 1:])
                for simbolo in simbolos:
                    cadeias.add(base[:i] + simbolo + base[i + 1:])
                    cadeias.add(base[:i] + simbolo + base[i:])
        for cadeia in sorted(cadeias):
            with self.subTest(cadeia=cadeia):
                self.assertEqual(
                    executar(self.afd, cadeia)[0], padroes.validar(padroes.MATRICULA, cadeia)
                )


class LeituraDoJffTest(unittest.TestCase):
    MODELO = """<?xml version="1.0" encoding="UTF-8"?><structure>
\t<type>fa</type>
\t<automaton>
\t\t<state id="0" name="q0"><x>0.0</x><y>0.0</y><initial/></state>
\t\t<state id="1" name="q1"><x>0.0</x><y>0.0</y><final/></state>
{transicoes}
\t</automaton>
</structure>
"""

    def carrega_texto(self, transicoes):
        descritor, caminho = tempfile.mkstemp(suffix=".jff")
        with os.fdopen(descritor, "w", encoding="utf-8") as arquivo:
            arquivo.write(self.MODELO.format(transicoes=transicoes))
        self.addCleanup(os.remove, caminho)
        return carregar_jff(caminho)

    @staticmethod
    def transicao(origem, destino, simbolo):
        leitura = f"<read>{simbolo}</read>" if simbolo else "<read/>"
        return f"<transition><from>{origem}</from><to>{destino}</to>{leitura}</transition>"

    def test_rejeita_nao_determinismo(self):
        with self.assertRaises(ValueError):
            self.carrega_texto(self.transicao(0, 0, "a") + self.transicao(0, 1, "a"))

    def test_rejeita_transicao_vazia(self):
        with self.assertRaises(ValueError):
            self.carrega_texto(self.transicao(0, 1, ""))

    def test_rejeita_rotulo_com_mais_de_um_simbolo(self):
        with self.assertRaises(ValueError):
            self.carrega_texto(self.transicao(0, 1, "ab"))

    def test_le_automato_simples(self):
        afd = self.carrega_texto(self.transicao(0, 1, "a"))
        self.assertEqual(executar(afd, "a"), (True, ["q0", "q1"]))
        self.assertEqual(executar(afd, "b"), (False, ["q0", ESTADO_SUMIDOURO]))


if __name__ == "__main__":
    unittest.main()
