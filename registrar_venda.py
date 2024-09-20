from manipular_banco import consultarBanco, alterarBanco
from funcoes import validar_numero, separador


def registrar_venda():
    separador("registrar venda")
    id_produto = validar_numero("Digite a id do produto: ")
    quantidade = consultarBanco(
        f"SELECT quantidade FROM produtos WHERE id = {id_produto};")
    if quantidade:
        quantidade = quantidade[0][0]
        print(f"Quantidade do produto em estoque: {quantidade}")
        qtde_produto = validar_numero("Digite a quantidade vendida: ")
        if quantidade >= qtde_produto:
            quantidade -= qtde_produto
            inserido = alterarBanco(f"""
            INSERT INTO vendas
                (id_produto, quantidade)
                    VALUES
                        ({id_produto}, {qtde_produto});
            """)
            alterado = alterarBanco(f"""UPDATE produtos SET quantidade = {
                                    quantidade} WHERE id = {id_produto};""")
            if inserido and alterado:
                print("Venda cadastrada com sucesso!")
        else:
            print(f"Quantidade maior que o estoque. Quantidade em estoque: {
                  quantidade}")
    else:
        print("O id digitado não corresponde a nenhum produto.")
