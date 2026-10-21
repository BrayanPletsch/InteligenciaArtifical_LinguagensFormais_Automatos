import itertools
import re
import unittest

import padroes_regex as p
from validador_email import motivos_rejeicao, separar_emails


class PadraoTestCase(unittest.TestCase):
    def assertAceita(self, padrao, cadeias):
        for cadeia in cadeias:
            with self.subTest(cadeia=cadeia):
                self.assertTrue(p.validar(padrao, cadeia))

    def assertRejeita(self, padrao, cadeias):
        for cadeia in cadeias:
            with self.subTest(cadeia=cadeia):
                self.assertFalse(p.validar(padrao, cadeia))


def binarias_ate(tamanho, alfabeto="01"):
    for n in range(tamanho + 1):
        for simbolos in itertools.product(alfabeto, repeat=n):
            yield "".join(simbolos)


class ExerciciosGuiadosTest(PadraoTestCase):
    def test_sufixo_00(self):
        self.assertAceita(p.SUFIXO_00, ["00", "100", "0100", "11000"])
        self.assertRejeita(p.SUFIXO_00, ["", "0", "10", "001", "1001", "002"])

    def test_sufixo_00_contra_definicao(self):
        for palavra in binarias_ate(10):
            with self.subTest(palavra=palavra):
                self.assertEqual(p.validar(p.SUFIXO_00, palavra), palavra.endswith("00"))

    def test_exatamente_dois_a(self):
        self.assertAceita(p.EXATAMENTE_DOIS_A, ["aa", "aba", "baab", "bbabab", "abbbbbab"])
        self.assertRejeita(p.EXATAMENTE_DOIS_A, ["", "a", "b", "bab", "aaa", "ababa", "aca"])

    def test_exatamente_dois_a_contra_definicao(self):
        for palavra in binarias_ate(9, alfabeto="ab"):
            with self.subTest(palavra=palavra):
                self.assertEqual(
                    p.validar(p.EXATAMENTE_DOIS_A, palavra), palavra.count("a") == 2
                )

    def test_identificador_academico(self):
        self.assertAceita(p.IDENTIFICADOR_ACADEMICO, ["ES123", "LF001", "AB999z"])
        self.assertRejeita(
            p.IDENTIFICADOR_ACADEMICO,
            ["E123", "es123", "ES12", "ES1234", "ES123Z", "ES123ab", "ES-123", " ES123"],
        )


class MatriculaTest(PadraoTestCase):
    ACEITOS_DO_MATERIAL = [
        "CCO-2024-0001-M",
        "ESW-2026-1042-N",
        "SIS-2029-9999-T",
        "CCO-2027-0100-N",
        "ESW-2025-4321-M",
    ]
    REJEITADOS_DO_MATERIAL = [
        "ADS-2026-0001-N",
        "CCO-2030-0001-M",
        "SIS-2027-123-N",
        "esw-2026-1042-N",
        "CCO/2026/0001/M",
        "CCO-2026-0001-X",
    ]
    ACEITOS_CRIADOS = ["ESW-2024-0000-T", "SIS-2029-0042-N"]
    REJEITADOS_CRIADOS = [
        "ESW-2023-1042-N",
        "ESW-2026-10420-N",
        "CCO-2026-0001-MN",
        " CCO-2026-0001-M",
        "SIS-2028-0O01-T",
        "CCO-2026-0001-M\n",
    ]

    def test_casos_do_material(self):
        self.assertAceita(p.MATRICULA, self.ACEITOS_DO_MATERIAL)
        self.assertRejeita(p.MATRICULA, self.REJEITADOS_DO_MATERIAL)

    def test_casos_criados(self):
        self.assertAceita(p.MATRICULA, self.ACEITOS_CRIADOS)
        self.assertRejeita(p.MATRICULA, self.REJEITADOS_CRIADOS)

    def test_todos_os_anos(self):
        for ano in range(2000, 2100):
            with self.subTest(ano=ano):
                self.assertEqual(
                    p.validar(p.MATRICULA, f"ESW-{ano}-1042-N"), 2024 <= ano <= 2029
                )

    def test_fullmatch_rejeita_quebra_de_linha_que_o_cifrao_deixa_passar(self):
        self.assertIsNotNone(re.match(p.MATRICULA, "CCO-2026-0001-M\n"))
        self.assertFalse(p.validar(p.MATRICULA, "CCO-2026-0001-M\n"))


class VersoesComFalhaDaMatriculaTest(unittest.TestCase):
    """Versões erradas usadas na análise de falhas do relatório."""

    SEM_PARENTESES = r"^CCO|ESW|SIS-202[4-9]-[0-9]{4}-[MTN]$"
    NUMERO_COM_MAIS = r"^(CCO|ESW|SIS)-202[4-9]-[0-9]+-[MTN]$"

    def test_sem_parenteses_busca_trechos_soltos(self):
        self.assertIsNotNone(re.search(self.SEM_PARENTESES, "CCO/2026/0001/M"))
        self.assertIsNotNone(re.search(self.SEM_PARENTESES, "ADS-ESW-qualquer"))

    def test_sem_parenteses_rejeita_matricula_valida_de_cco(self):
        self.assertFalse(p.validar(self.SEM_PARENTESES, "CCO-2024-0001-M"))
        self.assertTrue(p.validar(self.SEM_PARENTESES, "SIS-2029-9999-T"))

    def test_mais_no_lugar_de_quatro_aceita_numero_longo(self):
        self.assertTrue(p.validar(self.NUMERO_COM_MAIS, "ESW-2026-10420-N"))
        self.assertFalse(p.validar(p.MATRICULA, "ESW-2026-10420-N"))


class EmailTutorialTest(PadraoTestCase):
    def test_padrao_identico_ao_do_tutorial(self):
        self.assertEqual(p.EMAIL, r"^[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

    def test_tabela_da_secao_5(self):
        self.assertAceita(
            p.EMAIL,
            [
                "aluno@gmail.com",
                "nome.sobrenome@udf.edu.br",
                "estudante_01@faculdade.com",
                "contato+curso@exemplo.com.br",
            ],
        )
        self.assertRejeita(
            p.EMAIL,
            [
                "aluno.gmail.com",
                "aluno@",
                "@gmail.com",
                "aluno@gmail",
                "aluno@gmail.c",
                "aluno gmail.com",
            ],
        )

    def test_casos_minimos_da_secao_10(self):
        validos, invalidos = separar_emails(
            [
                "maria@gmail.com",
                "joao.silva@udf.edu.br",
                "estudante_01@faculdade.com",
                "pedro.gmail.com",
                "ana@dominio",
            ]
        )
        self.assertEqual(
            validos, ["maria@gmail.com", "joao.silva@udf.edu.br", "estudante_01@faculdade.com"]
        )
        self.assertEqual(
            invalidos,
            [
                ("pedro.gmail.com", ["não possui o símbolo @"]),
                ("ana@dominio", ["não possui extensão (falta o ponto depois do domínio)"]),
            ],
        )

    def test_limitacoes_aceitas_pelo_padrao_do_tutorial(self):
        self.assertAceita(
            p.EMAIL,
            [".ana@udf.edu.br", "ana.@udf.edu.br", "ana..silva@udf.edu.br", "ana@-udf.edu.br"],
        )


class MotivosRejeicaoTest(unittest.TestCase):
    def test_motivos_da_tabela_do_tutorial(self):
        casos = {
            "aluno@": ["não possui domínio depois do @"],
            "@gmail.com": ["não possui usuário antes do @"],
            "aluno@gmail.c": ["a extensão precisa ter pelo menos duas letras e só letras"],
            "aluno gmail.com": ["contém espaço em branco", "não possui o símbolo @"],
            "ana@@udf.edu.br": ["possui mais de um @"],
            "ana@.com": ["não possui domínio entre o @ e o ponto"],
            "ana@udf.com2": ["a extensão precisa ter pelo menos duas letras e só letras"],
            "ana@udf_edu.br": ["o domínio tem caractere fora de letras, números, '.' e '-'"],
        }
        for email, esperado in casos.items():
            with self.subTest(email=email):
                self.assertEqual(motivos_rejeicao(email), esperado)

    def test_sem_motivo_somente_quando_a_regex_aceita(self):
        partes = ["", "a", "a.b", "a b", "_", "@", ".", "a@b", "-", "co", "c"]
        for usuario, dominio, extensao in itertools.product(partes, repeat=3):
            for email in (f"{usuario}@{dominio}.{extensao}", f"{usuario}{dominio}{extensao}"):
                with self.subTest(email=email):
                    self.assertEqual(motivos_rejeicao(email) == [], p.validar(p.EMAIL, email))


class EmailAprimoradoTest(PadraoTestCase):
    def test_continua_aceitando_os_validos_do_tutorial(self):
        self.assertAceita(
            p.EMAIL_APRIMORADO,
            [
                "aluno@gmail.com",
                "nome.sobrenome@udf.edu.br",
                "estudante_01@faculdade.com",
                "contato+curso@exemplo.com.br",
                "ana@minha-instituicao.com",
            ],
        )

    def test_regras_do_desafio(self):
        self.assertRejeita(
            p.EMAIL_APRIMORADO,
            [
                ".ana@udf.edu.br",
                "ana.@udf.edu.br",
                "ana..silva@udf.edu.br",
                "ana@udf..edu.br",
                "ana@-udf.edu.br",
                "ana@udf-.edu.br",
                "ana@udf.-edu.br",
            ],
        )

    def test_continua_rejeitando_os_invalidos_do_tutorial(self):
        self.assertRejeita(
            p.EMAIL_APRIMORADO,
            ["aluno.gmail.com", "aluno@", "@gmail.com", "aluno@gmail", "aluno@gmail.c"],
        )


if __name__ == "__main__":
    unittest.main()
