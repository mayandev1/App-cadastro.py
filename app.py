import sqlite3
import tkinter as tk
from tkinter import messagebox

# Passo 2: Configuração do banco de dados
def criar_bd():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para registrar usuários
def registrar_usuario(username, password):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Nome de usuário já existe!")
    conn.close()

# Função para fazer login
def login_usuario(username, password):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password))
    usuario = cursor.fetchone()
    conn.close()
    if usuario:
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        abrir_janela_produtos()
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha inválidos!")

# Função para adicionar produtos
def adicionar_produto(nome, preco, quantidade):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)', (nome, preco, quantidade))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")

# Função para listar produtos
def listar_produtos():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()
    return produtos

# Interface gráfica usando tkinter
def abrir_janela_registro():
    janela_registro = tk.Toplevel()
    janela_registro.title("Registrar")

    tk.Label(janela_registro, text="Nome de usuário").grid(row=0, column=0)
    tk.Label(janela_registro, text="Senha").grid(row=1, column=0)

    entrada_username = tk.Entry(janela_registro)
    entrada_password = tk.Entry(janela_registro, show="*")
    entrada_username.grid(row=0, column=1)
    entrada_password.grid(row=1, column=1)

    tk.Button(janela_registro, text="Registrar", command=lambda: registrar_usuario(entrada_username.get(), entrada_password.get())).grid(row=2, columnspan=2)

def abrir_janela_login():
    janela_login = tk.Tk()
    janela_login.title("Login")

    tk.Label(janela_login, text="Nome de usuário").grid(row=0, column=0)
    tk.Label(janela_login, text="Senha").grid(row=1, column=0)

    entrada_username = tk.Entry(janela_login)
    entrada_password = tk.Entry(janela_login, show="*")
    entrada_username.grid(row=0, column=1)
    entrada_password.grid(row=1, column=1)

    tk.Button(janela_login, text="Login", command=lambda: login_usuario(entrada_username.get(), entrada_password.get())).grid(row=2, columnspan=2)
    tk.Button(janela_login, text="Registrar", command=abrir_janela_registro).grid(row=3, columnspan=2)

    janela_login.mainloop()

def abrir_janela_produtos():
    janela_produtos = tk.Toplevel()
    janela_produtos.title("Produtos")

    tk.Label(janela_produtos, text="Nome do produto").grid(row=0, column=0)
    tk.Label(janela_produtos, text="Preço").grid(row=1, column=0)
    tk.Label(janela_produtos, text="Quantidade").grid(row=2, column=0)

    entrada_nome = tk.Entry(janela_produtos)
    entrada_preco = tk.Entry(janela_produtos)
    entrada_quantidade = tk.Entry(janela_produtos)
    entrada_nome.grid(row=0, column=1)
    entrada_preco.grid(row=1, column=1)
    entrada_quantidade.grid(row=2, column=1)

    tk.Button(janela_produtos, text="Adicionar Produto", command=lambda: adicionar_produto(entrada_nome.get(), float(entrada_preco.get()), int(entrada_quantidade.get()))).grid(row=3, columnspan=2)

    tk.Label(janela_produtos, text="Produtos cadastrados:").grid(row=4, columnspan=2)

    produtos = listar_produtos()
    for idx, produto in enumerate(produtos):
        tk.Label(janela_produtos, text=f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}, Quantidade: {produto[3]}").grid(row=5+idx, columnspan=2)

if __name__ == "__main__":
    criar_bd()  # Chamar a função para criar o banco de dados
    abrir_janela_login()  # Chamar a função para abrir a janela de login
