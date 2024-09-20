from manipular_banco import consultarBanco
from funcoes import calcular_espaco


def relatorio_estoque():
    produtos = consultarBanco("SELECT * FROM produtos")
    print("-------------------- RELATÓRIO ESTOQUE ---------------------")
    print("  Id  |             Produto            |  Qt. |    Preço    ")
    for produto in produtos:
        print("{}|{}|{}|{}".format(
            calcular_espaco(str(produto[0]), 6),
            calcular_espaco(produto[1], 32),
            calcular_espaco(str(produto[3]), 6),
            calcular_espaco(f"{produto[4]:.2f}", 13, 5)
        ))


def relatorio_vendas():
    vendas = consultarBanco(f"""SELECT
                vendas.id,
                DATE_FORMAT(vendas.data_venda, '%d/%m/%Y %H:%i'),
                produtos.nome,
                vendas.quantidade,
                produtos.preco,
                (vendas.quantidade * produtos.preco)
                FROM vendas
                INNER JOIN produtos ON vendas.id_produto = produtos.id""")

    print("-------------------------------------- RELATÓRIO DE VENDAS --------------------------------------")
    print("Venda |        Data        |             Produto            |  Qt. |    Preço    |     Total     ")
    total_relatorio = 0
    for venda in vendas:
        total = f"{venda[5]:.2f}"
        total_relatorio += float(total)
        print("{}|  {}  |{}|{}|{}  |{}".format(
            calcular_espaco(str(venda[0]), 6),
            venda[1],
            calcular_espaco(venda[2], 32),
            calcular_espaco(str(venda[3]), 6),
            calcular_espaco(f"{venda[4]:.2f}", 13, 5),
            calcular_espaco(total, 15, 5)
        ))
    print(
        f"---------------------------------------------------------------- TOTAL DAS VENDAS:   R$ {total_relatorio:.2f}")
