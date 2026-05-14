"""Gerenciador Simples de Produtos

Produtos são salvos em /json/produtos.json

Dev: Anna
Github: https://github.com/0xAA55-P
Data: 12/05/2026
"""

from escolhas import adicionar, remover, editar, listar_id
from input_output import exibir_menu, ler_inteiro
from json_handling import listar_todos
from rich import print as bprint
from opcao import Opcao

FILENAME = "../json/produtos.json"
DEBUG = False


def tratar_escolha(escolha: int) -> bool:
    """Trata a escolha chamando a opção correta de acordo.

    Returns:
        True: Conseguiu finalizar a função
        False: Usuario escolheu sair

    Raises:
        ValueError se a escolha estiver fora do alcance de 0-5

    """

    match escolha:
        case Opcao.SAIR:
            bprint("\n[green][SAIDA][/] Adeus!\n")
            return False

        case Opcao.ADICIONAR_PRODUTO:
            adicionar()

        case Opcao.REMOVER_PRODUTO:
            remover()

        case Opcao.EDITAR_PRODUTO:
            editar()

        case Opcao.LISTAR_PRODUTOS:
            listar_todos(FILENAME)

        case Opcao.LISTAR_POR_ID:
            listar_id()

        case _:
            raise ValueError()

    return True


def main() -> None:
    while True:
        try:
            print()
            exibir_menu()

            escolha = ler_inteiro("[ENTRADA] Digite o número da opção: ")

            if not tratar_escolha(escolha):
                break

        except KeyboardInterrupt:
            bprint("\n[green][SAIDA][/] Adeus!\n")
            break

        except ValueError as e:
            bprint("\n[yellow][AVISO][/] Escolha inválida.")

            if DEBUG:
                print(e)

            continue


if __name__ == "__main__":
    main()
