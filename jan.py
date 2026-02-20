import tkinter as tk
from tkinter import messagebox
import banco 

banco.criar_tabela()  # Criar a tabela no banco de dados



def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Usuários e senhas cadastraveis

    if banco.verificar_login(usuario, senha):
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos!")
    
def cadastrar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if banco.cadastrar_usuario(usuario, senha): 
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
    else:
        messagebox.showerror("error" , "error ao cadastrar usuario")


# Criando janela
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("300x200")
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="Sistema de Login", font=("Arial", 14))
titulo.pack(pady=10)

# Usuário
label_usuario = tk.Label(janela, text="Usuário:")
label_usuario.pack()

entry_usuario = tk.Entry(janela)
entry_usuario.pack()

# Senha
label_senha = tk.Label(janela, text="Senha:")
label_senha.pack()

entry_senha = tk.Entry(janela, show="*")
entry_senha.pack()

# Botão
botao_login = tk.Button(janela, text="Entrar", command=login)
botao_login.pack(pady=10)


tk.Button(janela, text="Cadastrar", command=cadastrar).pack() 

janela.mainloop()