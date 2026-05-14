import json

"""
 adicionar produto
 remover produto
 editar produto
 listar todos
 listar por id
"""

def sobrescrever_produtos(dados: list, filename: str) -> None:
    """Sobreescreve os dados atuais do json.
       Evita má formatação, sobreposição indevida, etc...

       Args:
           dados: a lista com os dados atuais
           filename: O nome do arquivo
    """

    with open(filename, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def adicionar_produto(
    nome_produto: str,
    preco_produto: float,
    estoque_produto: int,
    filename: str,
) -> None:
    """Adiciona um produto no arquivo

    Args:
        nome_produto: O nome do Produto a adicionar
        preco_produto: O preço do Produto
        estoque: O estoque atual
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
    produto["id"] = len(dados) # auto incrementa, 1...2...3

    dados.append(produto)
    sobrescrever_produtos(dados, "../json/produtos.json")
    

def remover_produto(
    dados: list,
    id_para_remover: int,
    filename: str
) -> None:
    pass

def editar_produto(id_para_editar: int, filename: str) -> None:
    pass

def listar_todos(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    print()
    for produto in dados:
        print(f"Produto: {produto.get('nome')}")
        print(f"Preço: {produto.get('preco')}")
        print(f"Estoque: {produto.get('estoque')}")
        print()

def listar_por_id(id_para_buscar: int, filename: str) -> None:
    pass
