"""Enum com as opções possíveis

Uso:
    from opcao import Opcao
    
    Opcao.SAIR
    Opcao.ADICIONAR_PRODUTO
    etc...

"""

from enum import IntEnum

class Opcao(IntEnum):
    SAIR = 0
    ADICIONAR_PRODUTO = 1
    REMOVER_PRODUTO = 2
    EDITAR_PRODUTO = 3
    LISTAR_PRODUTOS = 4
    LISTAR_POR_ID = 5
