"""Utilitários básicos"""

def exibir_menu() -> None:
    menu = [
        "Sair",
        "Adicionar Produto",
        "Remover Produto",
        "Editar Produto",
        "Listar Produtos",
        "Listar Por ID\n",
    ]

    for i, opcao in enumerate(menu):
        print(f"{i}. {opcao}")

def ler_inteiro(mensagem: str) -> int:
    """Lê um inteiro, o prompt é a mensagem passada

    Args:
        mensagem: mensagem usada para o prompt
        e.x: ler_inteiro("Digite o id do produto")

    Returns:
        O inteiro lido
    """

    return int(input(mensagem))
