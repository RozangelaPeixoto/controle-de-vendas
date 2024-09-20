from manipular_banco import consultarBanco
from funcoes import separador


def mostrar_produtos_resumido():
    produtos = consultarBanco("SELECT * FROM produtos")
    print("\n------------------- LISTA IDs --------------------")
    for produto in produtos:
        print(f"{produto[0]} - {produto[1]}")


def mostrar_produtos():
    separador("Lista de produtos")
    produtos = consultarBanco("SELECT * FROM produtos")
    for produto in produtos:
        print(f"""
ID: {produto[0]}
Produto: {produto[1]}
Descrição: {produto[2]}
Quantidade: {produto[3]}
Preço: R$ {produto[4]:.2f}""")
