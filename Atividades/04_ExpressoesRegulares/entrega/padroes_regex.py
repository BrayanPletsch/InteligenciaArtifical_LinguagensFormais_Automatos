"""Padrões da atividade de Expressões Regulares (Aula 05).

Os padrões estão escritos como no material da disciplina, com ``^`` e ``$``,
para poderem ser colados sem mudança no Regex Learn. A validação usa
``re.fullmatch``, que exige a cadeia inteira, então as âncoras ficam
redundantes no Python, mas não atrapalham.
"""

import re

SUFIXO_00 = r"^[01]*00$"
EXATAMENTE_DOIS_A = r"^b*ab*ab*$"
IDENTIFICADOR_ACADEMICO = r"^[A-Z]{2}[0-9]{3}[a-z]?$"

MATRICULA = r"^(CCO|ESW|SIS)-202[4-9]-[0-9]{4}-[MTN]$"

EMAIL_USUARIO = r"[A-Za-z0-9._+-]+"
EMAIL_DOMINIO = r"[A-Za-z0-9.-]+"
EMAIL_EXTENSAO = r"[A-Za-z]{2,}"
EMAIL = rf"^{EMAIL_USUARIO}@{EMAIL_DOMINIO}\.{EMAIL_EXTENSAO}$"

EMAIL_APRIMORADO_USUARIO = r"[A-Za-z0-9_+-]+(?:\.[A-Za-z0-9_+-]+)*"
EMAIL_APRIMORADO_ROTULO = r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?"
EMAIL_APRIMORADO = (
    rf"^{EMAIL_APRIMORADO_USUARIO}@(?:{EMAIL_APRIMORADO_ROTULO}\.)+{EMAIL_EXTENSAO}$"
)


def validar(padrao: str, cadeia: str) -> bool:
    """Retorna True se a cadeia inteira pertence à linguagem do padrão."""
    return re.fullmatch(padrao, cadeia) is not None
