import sqlite3

def conectar():
    return sqlite3.connect('login.db')

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS login (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        senha TEXT NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()

def verificar_login(usuario, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM login WHERE usuario = ? AND senha = ?",
        (usuario, senha)
    )

    resultado = cursor.fetchone()
    conexao.close()

    return resultado

def cadastrar_usuario(usuario, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "INSERT INTO login (usuario, senha) VALUES (?, ?)",
            (usuario, senha)
        )
        conexao.commit()
    except:
        conexao.close()
        return False

    conexao.close()
    return True

   


        