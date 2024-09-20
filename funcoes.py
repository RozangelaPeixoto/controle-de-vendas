from math import floor, ceil


def separador(texto):
    texto = " "+texto.upper()+" "
    print("-"*50)
    espaco = (50-len(texto))/2
    print("-"*floor(espaco)+texto+"-"*ceil(espaco))


def validar_numero(pergunta, resposta=0):
    if not (resposta):
        resposta = input(pergunta)
    while isinstance(resposta, str):
        try:
            return int(resposta)
        except:
            print("Digite um número válido.")
            resposta = input(pergunta)


def validar_preco(pergunta, resposta=0):
    if not (resposta):
        resposta = input(pergunta)
    while isinstance(resposta, str):
        try:
            return float(resposta.replace(",", "."))
        except:
            print("Digite um número válido.")
            resposta = input(pergunta)


def calcular_espaco(texto, et, te=0):
    if te:
        espaco = et-(te+len(texto))
        return " "*espaco+"R$ " + texto
    else:
        espaco = (et-len(texto))/2
        return " "*ceil(espaco)+texto+" "*floor(espaco)
