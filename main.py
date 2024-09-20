from funcoes import separador, validar_numero
from casdastrar_produto import cadastrar_produto
from editar_produto import atualizar_produto
from listar_produtos import mostrar_produtos_resumido, mostrar_produtos
from registrar_venda import registrar_venda
from relatorios import relatorio_estoque, relatorio_vendas

menu = """1 - Adicionar produto
2 - Atualizar produto
3 - Mostrar produtos
4 - Registrar venda 
5 - Relatório de estoque
6 - Relatório de vendas
0 - Sair
Escolha uma opção: """

while True:
    separador("menu principal")
    resposta = validar_numero(menu)
    match resposta:
        case 1:
            cadastrar_produto()
        case 2:
            mostrar_produtos_resumido()
            separador("atualizar produto")
            id_alterar = validar_numero(
                "Digite a id do produto que deseja alterar: ")
            atualizar_produto(id_alterar)
        case 3:
            mostrar_produtos()
        case 4:
            mostrar_produtos_resumido()
            registrar_venda()
        case 5:
            relatorio_estoque()
        case 6:
            relatorio_vendas()
        case 0:
            print("Fim do programa")
            break
        case _:
            print("Opção inválida. Tente novamente")
