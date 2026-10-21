"""Atividade prática da seção 10 do tutorial de validação de e-mail.

Lê cinco endereços, separa os formatos válidos dos inválidos e explica
por que cada inválido foi rejeitado pela Regex do tutorial.
"""

from padroes_regex import EMAIL, EMAIL_DOMINIO, EMAIL_EXTENSAO, EMAIL_USUARIO, validar

QUANTIDADE_DE_EMAILS = 5


def motivos_rejeicao(email: str) -> list[str]:
    """Lista os motivos de rejeição; lista vazia quando o e-mail é aceito.

    A extensão não tem ponto, então ela é sempre o trecho depois do último
    ponto. Por isso dividir em ``@`` e no último ``.`` reproduz exatamente
    as partes que a Regex tenta casar.
    """
    if validar(EMAIL, email):
        return []

    motivos = []
    if any(caractere.isspace() for caractere in email):
        motivos.append("contém espaço em branco")

    quantidade_arrobas = email.count("@")
    if quantidade_arrobas == 0:
        motivos.append("não possui o símbolo @")
        return motivos
    if quantidade_arrobas > 1:
        motivos.append("possui mais de um @")
        return motivos

    usuario, _, resto = email.partition("@")
    if not usuario:
        motivos.append("não possui usuário antes do @")
    elif not validar(EMAIL_USUARIO, usuario):
        motivos.append("o usuário tem caractere fora de letras, números, '.', '_', '+' e '-'")

    dominio, ponto, extensao = resto.rpartition(".")
    if not resto:
        motivos.append("não possui domínio depois do @")
    elif not ponto:
        motivos.append("não possui extensão (falta o ponto depois do domínio)")
    else:
        if not dominio:
            motivos.append("não possui domínio entre o @ e o ponto")
        elif not validar(EMAIL_DOMINIO, dominio):
            motivos.append("o domínio tem caractere fora de letras, números, '.' e '-'")
        if not validar(EMAIL_EXTENSAO, extensao):
            motivos.append("a extensão precisa ter pelo menos duas letras e só letras")
    return motivos


def separar_emails(emails: list[str]) -> tuple[list[str], list[tuple[str, list[str]]]]:
    """Separa os e-mails em válidos e inválidos (com os motivos)."""
    validos = []
    invalidos = []
    for email in emails:
        motivos = motivos_rejeicao(email)
        if motivos:
            invalidos.append((email, motivos))
        else:
            validos.append(email)
    return validos, invalidos


def main() -> None:
    emails = [
        input(f"E-mail {numero}: ")
        for numero in range(1, QUANTIDADE_DE_EMAILS + 1)
    ]
    validos, invalidos = separar_emails(emails)

    print(f"\nFormatos válidos ({len(validos)}):")
    for email in validos:
        print(f"  {email}")

    print(f"\nFormatos inválidos ({len(invalidos)}):")
    for email, motivos in invalidos:
        print(f"  {email}: {'; '.join(motivos)}")


if __name__ == "__main__":
    main()
