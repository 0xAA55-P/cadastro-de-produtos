"""Operações principais com JSON e auxiliares para lidar.

Adicionar produto
Remover produto
Editar produto
Listar todos
Listar por id

"""

from rich import print as bprint
from opcao import Editar
import json


def sobrescrever_produtos(dados: list, filename: str) -> None:
    """Sobreescreve os dados atuais do json.
    Evita má formatação, sobreposição indevida, etc...

    Args:
        dados: a lista com os dados atuais
        filename: O nome do arquivo
    """

    with open(filename, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def alterar_produto(
    dado_para_atualizar: str,
    novo_dado: str,
    id_para_atualizar: int,
    dados: list,
    filename: str,
) -> None:
    """Atualiza um dado especifico do produto

    Args:
        dado_para_atualizar: O dado a ser alterado (nome, preco ou estoque)
        novo_dado: O novo valor para aquele dado
        id_para_atualizar: o ID do produto a alterar
        dados: A lista com os produtos
        filename: Nome do arquivo

    """

    for produto in dados:
        if produto.get("id") == id_para_atualizar:
            produto[dado_para_atualizar] = novo_dado
            break

    sobrescrever_produtos(dados, filename)


def adicionar_produto(
    nome_produto: str,
    preco_produto: float,
    estoque_produto: int,
    filename: str,
) -> None:
    """Adiciona um produto no arquivo

    Adiciona o produto e seu id, o id será sempre o
    próximo id disponível.
    Os IDs não são automaticamente ordenados.

    Args:
        nome_produto: O nome do Produto a adicionar
        preco_produto: O preço do Produto
        estoque: O estoque atual
        filename: O nome do arquivo

    """

    try:
        with open(filename, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # arquivo vazio/não encontrado, lista vazia
        dados = []

    produto: dict = {}
    produto["nome"] = nome_produto
    produto["preco"] = preco_produto
    produto["estoque"] = estoque_produto

    # percorre e procura o proximo id disponivel
    novo_id = max((p["id"] for p in dados), default=-1) + 1
    produto["id"] = novo_id  # auto incrementa, 1...2...3

    # adiciona na lista, e formata o arquivo
    # com os produtos atuais
    dados.append(produto)
    sobrescrever_produtos(dados, filename)


def remover_produto(id_para_remover: int, filename: str) -> bool:
    """Remove um Produto da Lista

    Args:
        id_para_remover: O id do produto a ser removido

    Returns:
        True se conseguiu deletar
        False se não conseguiu deletar/Arquivo inexistente
    """

    try:
        with open(filename, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        dados.pop(id_para_remover)
        sobrescrever_produtos(dados, filename)
        return True

    except (IndexError, FileNotFoundError, json.JSONDecodeError):
        return False


def editar_produto(id_para_editar: int, operacao: int, filename: str) -> None:
    """Edita um produto com base na operação

    Args:
        id_para_editar: o ID do produto a ser editado
        operacao: A operação a ser realizada
            Operacao.EDITAR_NOME: 1
            Operacao.EDITAR_PRECO: 2
            Operacao.EDITAR_ESTOQUE: 3

    Raises:
        ValueError se a escolha estiver fora do range de 1-3

    """

    with open(filename, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    match operacao:
        case Editar.NOME:
            novo_nome: str = input("\n[ENTRADA] Novo nome: ")
            alterar_produto("nome", novo_nome, id_para_editar, dados, filename)

        case Editar.PRECO:
            novo_preco = float(input("\n[ENTRADA] Novo preço: "))
            alterar_produto("preco", novo_preco, id_para_editar, dados, filename)

        case Editar.ESTOQUE:
            novo_estoque = int(input("\n[ENTRADA] Novo estoque: "))
            alterar_produto("estoque", novo_estoque, id_para_editar, dados, filename)

        case _:
            raise ValueError()


def listar_todos(filename: str) -> None:
    """Lista todos os Produtos salvos no arquivo
       e suas informações

    Args:
        filename: Nome do arquivo
    """

    with open(filename, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    bprint()
    for produto in dados:
        bprint(f"Produto: {produto.get('nome')}")
        bprint(f"Preço: {produto.get('preco')}")
        bprint(f"Estoque: {produto.get('estoque')}")
        bprint(f"ID: {produto.get('id')}")
        bprint()


def listar_por_id(id_para_buscar: int, filename: str) -> None:
    """Lista um produto especifico por ID e suas informações

    Args:
        id_para_buscar: o ID Do produto
        filename: Nome do arquivo

    """

    with open(filename, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    bprint()
    for produto in dados:
        if produto["id"] == id_para_buscar:
            bprint(f"Produto: {produto.get('nome')}")
            bprint(f"Preço: {produto.get('preco')}")
            bprint(f"Estoque: {produto.get('estoque')}")
            bprint(f"ID: {produto.get('id')}")
