import sqlite3
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

# Conectando ao banco de dados
db = sqlite3.connect('database.db')
cursor = db.cursor()

# Criando as tabelas do banco de dados
def criar_tabelas():
    # Tabela de usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Tabela de estoque
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            produto TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    """)

# Interface de login e registro
def login():
    def perform_login():
        username = username_entry.get()
        password = password_entry.get()

        # Verificando se o usuário existe no banco de dados
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        values = (username, password)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Sucesso", "Login bem-sucedido!")
            login_window.destroy()
            menu_principal(username)
        else:
            messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")

    login_window = Tk()
    login_window.title("Login")
    login_window.geometry("300x150")

    username_label = Label(login_window, text="Nome de usuário:")
    username_label.pack()
    username_entry = Entry(login_window)
    username_entry.pack()

    password_label = Label(login_window, text="Senha:")
    password_label.pack()
    password_entry = Entry(login_window, show="*")
    password_entry.pack()

    login_button = Button(login_window, text="Login", command=perform_login)
    login_button.pack()

    login_window.mainloop()


def register():
    def perform_registration():
        username = register_username_entry.get()
        password = register_password_entry.get()

        # Verificar se o nome de usuário já está em uso
        query = "SELECT * FROM users WHERE username = ?"
        values = (username,)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            messagebox.showerror("Erro", "Nome de usuário já em uso.")
        else:
            # Inserir novo usuário no banco de dados
            query = "INSERT INTO users (username, password) VALUES (?, ?)"
            values = (username, password)
            cursor.execute(query, values)
            db.commit()
            messagebox.showinfo("Sucesso", "Registro bem-sucedido!")
            registration_window.destroy()
            login()

    registration_window = Tk()
    registration_window.title("Registro")
    registration_window.geometry("300x150")

    register_username_label = Label(registration_window, text="Nome de usuário:")
    register_username_label.pack()
    register_username_entry = Entry(registration_window)
    register_username_entry.pack()

    register_password_label = Label(registration_window, text="Senha:")
    register_password_label.pack()
    register_password_entry = Entry(registration_window, show="*")
    register_password_entry.pack()

    register_button = Button(registration_window, text="Registrar", command=perform_registration)
    register_button.pack()

    registration_window.mainloop()

# Interface de cadastro de estoque de produtos
def cadastrar_produto(username):
    def perform_cadastro():
        produto = produto_entry.get()
        quantidade = int(quantidade_entry.get())

        # Inserindo produto no banco de dados vinculado ao usuário logado
        query = "INSERT INTO estoque (username, produto, quantidade) VALUES (?, ?, ?)"
        values = (username, produto, quantidade)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        cadastro_window.destroy()

    cadastro_window = Tk()
    cadastro_window.title("Cadastro de Produto")
    cadastro_window.geometry("300x150")

    produto_label = Label(cadastro_window, text="Nome do produto:")
    produto_label.pack()
    produto_entry = Entry(cadastro_window)
    produto_entry.pack()

    quantidade_label = Label(cadastro_window, text="Quantidade:")
    quantidade_label.pack()
    quantidade_entry = Entry(cadastro_window)
    quantidade_entry.pack()

    cadastrar_button = Button(cadastro_window, text="Cadastrar", command=perform_cadastro)
    cadastrar_button.pack()

    cadastro_window.mainloop()

# Interface de retirada de produtos do estoque
def retirar_produto(username):
    def perform_retirada():
        produto = produto_entry.get()
        quantidade = int(quantidade_entry.get())

        # Verificando se o produto existe no estoque do usuário
        query = "SELECT * FROM estoque WHERE username = ? AND produto = ?"
        values = (username, produto)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            estoque_atual = result[3]  # Quantidade atual no estoque
            if quantidade <= estoque_atual:
                novo_estoque = estoque_atual - quantidade

                # Atualizando a quantidade do produto no estoque
                query = "UPDATE estoque SET quantidade = ? WHERE username = ? AND produto = ?"
                values = (novo_estoque, username, produto)
                cursor.execute(query, values)
                db.commit()
                messagebox.showinfo("Sucesso", "Produto retirado do estoque com sucesso!")
                retirada_window.destroy()
            else:
                messagebox.showerror("Erro", "Quantidade insuficiente no estoque.")
        else:
            messagebox.showerror("Erro", "Produto não encontrado no estoque.")

    retirada_window = Tk()
    retirada_window.title("Retirada de Produto")
    retirada_window.geometry("300x150")

    produto_label = Label(retirada_window, text="Nome do produto:")
    produto_label.pack()
    produto_entry = Entry(retirada_window)
    produto_entry.pack()

    quantidade_label = Label(retirada_window, text="Quantidade:")
    quantidade_label.pack()
    quantidade_entry = Entry(retirada_window)
    quantidade_entry.pack()

    retirar_button = Button(retirada_window, text="Retirar", command=perform_retirada)
    retirar_button.pack()

    retirada_window.mainloop()

# Interface de visualização gráfica do estoque por conta cadastrada
def visualizar_estoque(username):
    # Recuperando dados do estoque do usuário logado
    query = "SELECT produto, quantidade FROM estoque WHERE username = ?"
    values = (username,)
    cursor.execute(query, values)
    result = cursor.fetchall()

    produtos = []
    quantidades = []

    for row in result:
        produtos.append(row[0])
        quantidades.append(row[1])

    # Gerando gráfico de barras
    plt.bar(produtos, quantidades)
    plt.xlabel("Produtos")
    plt.ylabel("Quantidades")
    plt.title("Estoque")
    plt.show()

# Interface de ranking de todas as empresas cadastradas
def exibir_ranking():
    # Recuperando dados de todas as empresas e seus respectivos estoques
    query = "SELECT username, SUM(quantidade) AS total FROM estoque GROUP BY username ORDER BY total DESC"
    cursor.execute(query)
    result = cursor.fetchall()

    empresas = []
    estoques = []

    for row in result:
        empresas.append(row[0])
        estoques.append(row[1])

    # Gerando tabela do ranking
    messagebox.showinfo("Ranking de Empresas", "\n".join(f"{i}. {empresa}: {estoque}" for i, (empresa, estoque) in enumerate(zip(empresas, estoques), 1)))

# Interface para visualização de rastreamento de produto através da leitura de QR
def rastrear_produto():
    qr_code = input("Leia o QR code do produto: ")

    # Realizar o rastreamento do produto com base no QR code
    # Código para rastrear o produto...

# Menu principal
def menu_principal(username):
    def cadastrar_produto():
        cadastrar_produto_window = Tk()
        cadastrar_produto_window.title("Cadastro de Produto")
        cadastrar_produto_window.geometry("300x150")

        cadastrar_produto_label = Label(cadastrar_produto_window, text="Digite o nome do produto:")
        cadastrar_produto_label.pack()
        cadastrar_produto_entry = Entry(cadastrar_produto_window)
        cadastrar_produto_entry.pack()

        cadastrar_quantidade_label = Label(cadastrar_produto_window, text="Digite a quantidade:")
        cadastrar_quantidade_label.pack()
        cadastrar_quantidade_entry = Entry(cadastrar_produto_window)
        cadastrar_quantidade_entry.pack()

        def perform_cadastro():
            produto = cadastrar_produto_entry.get()
            quantidade = int(cadastrar_quantidade_entry.get())

            # Inserindo produto no banco de dados vinculado ao usuário logado
            query = "INSERT INTO estoque (username, produto, quantidade) VALUES (?, ?, ?)"
            values = (username, produto, quantidade)
            cursor.execute(query, values)
            db.commit()
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            cadastrar_produto_window.destroy()

        cadastrar_button = Button(cadastrar_produto_window, text="Cadastrar", command=perform_cadastro)
        cadastrar_button.pack()

        cadastrar_produto_window.mainloop()

    def retirar_produto():
        retirar_produto_window = Tk()
        retirar_produto_window.title("Retirada de Produto")
        retirar_produto_window.geometry("300x150")

        retirar_produto_label = Label(retirar_produto_window, text="Digite o nome do produto:")
        retirar_produto_label.pack()
        retirar_produto_entry = Entry(retirar_produto_window)
        retirar_produto_entry.pack()

        retirar_quantidade_label = Label(retirar_produto_window, text="Digite a quantidade:")
        retirar_quantidade_label.pack()
        retirar_quantidade_entry = Entry(retirar_produto_window)
        retirar_quantidade_entry.pack()

        def perform_retirada():
            produto = retirar_produto_entry.get()
            quantidade = int(retirar_quantidade_entry.get())

            # Verificando se o produto existe no estoque do usuário
            query = "SELECT * FROM estoque WHERE username = ? AND produto = ?"
            values = (username, produto)
            cursor.execute(query, values)
            result = cursor.fetchone()

            if result:
                estoque_atual = result[3]  # Quantidade atual no estoque
                if quantidade <= estoque_atual:
                    novo_estoque = estoque_atual - quantidade

                    # Atualizando a quantidade do produto no estoque
                    query = "UPDATE estoque SET quantidade = ? WHERE username = ? AND produto = ?"
                    values = (novo_estoque, username, produto)
                    cursor.execute(query, values)
                    db.commit()
                    messagebox.showinfo("Sucesso", "Produto retirado do estoque com sucesso!")
                    retirar_produto_window.destroy()
                else:
                    messagebox.showerror("Erro", "Quantidade insuficiente no estoque.")
            else:
                messagebox.showerror("Erro", "Produto não encontrado no estoque.")

        retirar_button = Button(retirar_produto_window, text="Retirar", command=perform_retirada)
        retirar_button.pack()

        retirar_produto_window.mainloop()

    menu_window = Tk()
    menu_window.title("Menu Principal")
    menu_window.geometry("300x150")

    cadastrar_button = Button(menu_window, text="Cadastrar Produto", command=cadastrar_produto)
    cadastrar_button.pack()

    retirar_button = Button(menu_window, text="Retirar Produto", command=retirar_produto)
    retirar_button.pack()

    visualizar_button = Button(menu_window, text="Visualizar Estoque", command=lambda: visualizar_estoque(username))
    visualizar_button.pack()

    ranking_button = Button(menu_window, text="Exibir Ranking", command=exibir_ranking)
    ranking_button.pack()

    rastrear_button = Button(menu_window, text="Rastrear Produto", command=rastrear_produto)
    rastrear_button.pack()

    menu_window.mainloop()

# Função para criar a janela principal
def main_window():
    main_window = Tk()
    main_window.title("Login / Registro")
    main_window.geometry("300x100")

    def open_login():
        main_window.destroy()
        login()

    def open_register():
        main_window.destroy()
        register()

    login_button = Button(main_window, text="Login", command=open_login)
    login_button.pack()

    register_button = Button(main_window, text="Registrar", command=open_register)
    register_button.pack()

    main_window.mainloop()

if __name__ == "__main__":
    main_window()