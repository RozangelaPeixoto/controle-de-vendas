from manipular_banco import alterarBanco
from funcoes import validar_numero, validar_preco, separador


def cadastrar_produto():
    separador("cadastrar produto")
    nome_produto = str(input("Digite o produto: "))
    desc_produto = str(input("Digite a descrição do produto: "))
    qtde_produto = validar_numero(
        "Digite a quantidade do produto no estoque: ")
    preco_produto = validar_preco("Digite o preço do produto: ")
    alterado = alterarBanco(f"""
    INSERT INTO produtos
        (nome, descricao, quantidade, preco)
            VALUES
                ('{nome_produto}', '{desc_produto}',
                 {qtde_produto}, {preco_produto});
    """)
    if alterado:
        print("Produto cadastrado com sucesso!")
