import sqlite3
import getpass
import bcrypt

def limpar_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPressione Enter para continuar...")

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

criar_bd()

def registrar_usuario():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    username = input("Digite um nome de usuário: ")
    password = getpass.getpass("Digite uma senha: ")
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        print("Usuário registrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Nome de usuário já existe!")
    conn.close()
    pausar()

def login_usuario():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    username = input("Digite seu nome de usuário: ")
    password = getpass.getpass("Digite sua senha: ")

    cursor.execute('SELECT password FROM usuarios WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()

    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
        print("Login bem-sucedido!")
        pausar()
        return True
    else:
        print("Nome de usuário ou senha inválidos!")
        pausar()
        return False

def adicionar_produto():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))

    cursor.execute('INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)', (nome, preco, quantidade))
    conn.commit()
    conn.close()
    print("Produto adicionado com sucesso!")
    pausar()

def listar_produtos():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()

    if produtos:
        for produto in produtos:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}, Quantidade: {produto[3]}")
    else:
        print("Nenhum produto encontrado!")
    pausar()

def remover_produto():
    listar_produtos()
    produto_id = int(input("Digite o ID do produto que deseja remover: "))
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM produtos WHERE id = ?', (produto_id,))
    conn.commit()
    conn.close()
    print("Produto removido com sucesso!")
    pausar()

def main():
    while True:
        limpar_terminal()
        print("1. Registrar")
        print("2. Login")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            registrar_usuario()
        elif escolha == '2':
            if login_usuario():
                while True:
                    limpar_terminal()
                    print("1. Adicionar Produto")
                    print("2. Listar Produtos")
                    print("3. Remover Produto")
                    print("4. Logout")
                    escolha_produto = input("Escolha uma opção: ")

                    if escolha_produto == '1':
                        adicionar_produto()
                    elif escolha_produto == '2':
                        listar_produtos()
                    elif escolha_produto == '3':
                        remover_produto()
                    elif escolha_produto == '4':
                        break
                    else:
                        print("Escolha inválida!")
                        pausar()
            else:
                print("Falha no login!")
                pausar()
        elif escolha == '3':
            break
        else:
            print("Escolha inválida!")
            pausar()

if __name__ == "__main__":
    main()
