"""Arquivo com funções para chamar as operações

Proposito: Match Case na Main estava crescendo além do desejado
           Então, aqui estão os blocos internos deles

Uso:

match escolha:
    case Opcao.ADICIONAR_PRODUTO:
        adicionar()

etc...

A função listar_todos não está inclusa pois é one-line.

"""

from json_handling import (
    adicionar_produto,
    remover_produto,
    editar_produto,
    listar_todos,
    listar_por_id,
)
from input_output import ler_inteiro
from rich import print as bprint

FILENAME = "../json/produtos.json"


def adicionar() -> None:
    nome = str(input("\n[ENTRADA] Nome do Produto: "))
    preco = float(input("[ENTRADA] Preço do Produto: "))
    estoque = ler_inteiro("[ENTRADA] Estoque: ")

    adicionar_produto(nome, preco, estoque, FILENAME)


def remover() -> None:
    listar_todos(FILENAME)

    id_para_remover = ler_inteiro("[ENTRADA] ID Para Remover: ")

    if not remover_produto(id_para_remover, FILENAME):
        bprint("\n[yellow][AVISO][/] ID Inválido/Arquivo inexistente.")
        bprint("[green][AJUDA][/] Insira o id correto ou adicione um produto.")
    else:
        bprint("\n[green][SUCESSO][/] Produto deletado.")


def editar() -> None:
    print("\n1. Editar Nome")
    print("2. Editar Preço")
    print("3. Editar Estoque")

    escolha = ler_inteiro("\n[ENTRADA] Digite sua escolha: ")

    listar_todos(FILENAME)

    id_para_editar = ler_inteiro("\n[ENTRADA] ID Para editar: ")

    editar_produto(id_para_editar, escolha, FILENAME)


def listar_id() -> None:
    id_para_buscar = ler_inteiro("\n[ENTRADA] ID Para Buscar: ")

    listar_por_id(id_para_buscar, FILENAME)
