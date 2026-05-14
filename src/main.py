"""Gerenciador Simples de Produtos

Produtos são salvos em /json/produtos.json

Dev: Anna
Github: https://github.com/0xAA55-P
Data: 12/05/2026
"""

from rich import print as bprint
from input_output import exibir_menu, ler_inteiro
from opcao import Opcao
from json_handling import adicionar_produto, listar_todos

FILENAME = "../json/produtos.json"

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
            nome = str(input("\nNome do Produto: "))
            preco = float(input("Preço do Produto: "))
            estoque = int(input("Estoque: "))
            
            adicionar_produto(nome, preco, estoque, FILENAME)

        case Opcao.REMOVER_PRODUTO:
            pass
        case Opcao.EDITAR_PRODUTO:
            pass
        case Opcao.LISTAR_PRODUTOS:
            listar_todos(FILENAME)
        case Opcao.LISTAR_POR_ID:
            pass
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

        except ValueError:
            bprint("\n[yellow][AVISO][/] Escolha inválida.")
            continue


if __name__ == "__main__":
    main()
