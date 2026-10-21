import itertools
import tempfile
import unittest
from pathlib import Path

from simulador_mt import BRANCO, MAQUINA_PADRAO, carregar_jff, executar

ACEITAS = ["01", "0011", "000111", "00001111"]
REJEITADAS = ["0", "1", "001", "011", "00111"]


def pertence_0n1n(palavra: str) -> bool:
    n = len(palavra) // 2
    return n >= 1 and palavra == "0" * n + "1" * n


def jff_temporario(pasta: str, transicoes: str) -> Path:
    caminho = Path(pasta) / "maquina.jff"
    caminho.write_text(
        "<structure><type>turing</type><automaton>"
        '<state id="0" name="q0"><x>0</x><y>0</y><initial/></state>'
        '<state id="1" name="q1"><x>0</x><y>0</y><final/></state>'
        f"{transicoes}</automaton></structure>",
        encoding="utf-8",
    )
    return caminho


class TestMaquina0n1n(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maquina = carregar_jff(MAQUINA_PADRAO)

    def test_estrutura_lida_do_jff(self):
        self.assertEqual(self.maquina.inicial, "q0")
        self.assertEqual(self.maquina.finais, {"q4"})
        self.assertEqual(len(self.maquina.transicoes), 10)
        self.assertEqual(self.maquina.transicoes[("q3", BRANCO)].move, "S")

    def test_aceita_exemplos_do_enunciado(self):
        for palavra in ACEITAS:
            with self.subTest(palavra=palavra):
                self.assertTrue(executar(self.maquina, palavra).aceita)

    def test_rejeita_exemplos_do_enunciado(self):
        for palavra in REJEITADAS:
            with self.subTest(palavra=palavra):
                self.assertFalse(executar(self.maquina, palavra).aceita)

    def test_rejeita_cadeia_vazia(self):
        execucao = executar(self.maquina, "")
        self.assertFalse(execucao.aceita)
        self.assertEqual(execucao.estados, ["q0"])

    def test_rejeita_mesma_quantidade_fora_de_ordem(self):
        for palavra in ["10", "0101", "0110", "1100"]:
            with self.subTest(palavra=palavra):
                self.assertFalse(executar(self.maquina, palavra).aceita)

    def test_todas_as_palavras_ate_tamanho_10(self):
        for tamanho in range(11):
            for simbolos in itertools.product("01", repeat=tamanho):
                palavra = "".join(simbolos)
                with self.subTest(palavra=palavra):
                    self.assertEqual(
                        executar(self.maquina, palavra).aceita, pertence_0n1n(palavra)
                    )

    def test_estados_percorridos_em_0011(self):
        execucao = executar(self.maquina, "0011")
        self.assertEqual(
            execucao.estados,
            ["q0", "q1", "q1", "q2", "q2", "q0", "q1", "q1", "q2", "q2", "q0", "q3", "q3", "q4"],
        )
        self.assertEqual(str(execucao.configuracoes[-1]), f"XXYY[{BRANCO}]")


class TestCarregarJff(unittest.TestCase):
    def test_recusa_maquina_nao_deterministica(self):
        duplicadas = (
            "<transition><from>0</from><to>1</to><read>a</read><write>a</write><move>R</move></transition>"
            "<transition><from>0</from><to>0</to><read>a</read><write>b</write><move>R</move></transition>"
        )
        with tempfile.TemporaryDirectory() as pasta:
            with self.assertRaises(ValueError):
                carregar_jff(jff_temporario(pasta, duplicadas))

    def test_interrompe_maquina_que_nao_para(self):
        laco_no_branco = (
            "<transition><from>0</from><to>0</to><read/><write/><move>R</move></transition>"
        )
        with tempfile.TemporaryDirectory() as pasta:
            maquina = carregar_jff(jff_temporario(pasta, laco_no_branco))
        with self.assertRaises(RuntimeError):
            executar(maquina, "", limite=50)


if __name__ == "__main__":
    unittest.main()
