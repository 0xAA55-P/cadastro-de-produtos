"""
Enums para facilitar a legibilidade de código
E evitar valores mágicos.

IntEnum é usado para não precisar fazer o type casting.

"""

from enum import IntEnum


class Opcao(IntEnum):
    """Enum com as opções possíveis para o match principal

    Uso:
        from opcao import Opcao

        Opcao.SAIR
        Opcao.ADICIONAR_PRODUTO
        etc...
    """

    SAIR = 0
    ADICIONAR_PRODUTO = 1
    REMOVER_PRODUTO = 2
    EDITAR_PRODUTO = 3
    LISTAR_PRODUTOS = 4
    LISTAR_POR_ID = 5


class Editar(IntEnum):
    """Enum para as operações de edição de um prpduto

    Uso:
        from opcao import Editar

        Editar.NOME
        Editar.PRECO
        Editar.ESTOQUE

    """

    NOME = 1
    PRECO = 2
    ESTOQUE = 3
