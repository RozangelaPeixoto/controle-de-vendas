from dotenv import load_dotenv
import mysql.connector

import os
load_dotenv()

configuracoes = {
    "host": os.getenv("HOST"),
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "database": os.getenv("DATABASE")
}


def consultarBanco(comando):
    conexao = mysql.connector.connect(**configuracoes)
    janelinha = conexao.cursor()
    janelinha.execute(comando)
    todos_os_dados = janelinha.fetchall()
    janelinha.close()
    conexao.close()
    return todos_os_dados


def alterarBanco(comando):
    conexao = mysql.connector.connect(**configuracoes)
    janelinha = conexao.cursor()
    janelinha.execute(comando)
    conexao.commit()
    janelinha.close()
    conexao.close()
    return True
