from manipular_banco import consultarBanco, alterarBanco
from funcoes import validar_numero, validar_preco


def atualizar_produto(id_produto):
    produto = consultarBanco(
        f"SELECT * FROM produtos WHERE id = {id_produto};")
    if produto:
        produto = produto[0]
        print(">> O valor será mostrado entre [], caso não queira alterar tecle enter")
        nome_produto = input(
            f"Digite o produto [{produto[1]}]: ") or produto[1]
        desc_produto = input(f"Digite a descrição do produto [{
                             produto[2]}]: ") or produto[2]
        qtde_produto = input(
            f"Digite a quantidade do produto no estoque [{produto[3]}]: ")
        qtde_produto = validar_numero(f"Digite a quantidade do produto no estoque [{
                                      produto[3]}]: ", qtde_produto) if qtde_produto else produto[3]
        preco_produto = input(f"Digite o preço do produto [{produto[4]}]: ")
        preco_produto = validar_preco(f"Digite o preço do produto [{
                                      produto[4]}]: ", preco_produto) if preco_produto else produto[4]
        alterado = alterarBanco(f"""
        UPDATE produtos SET
            nome = '{nome_produto}',
            descricao = '{desc_produto}',
            quantidade = {qtde_produto},
            preco = {preco_produto}
        WHERE id = {id_produto};""")
        if alterado:
            print("Produto alterado com sucesso!")
    else:
        print("Produto não encontrado.")
