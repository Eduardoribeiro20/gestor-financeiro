import sqlite3
from flask import Flask, render_template

app = Flask (__name__)

def get_db_connection():
    conn = sqlite3.connect('gestor.db')
    conn.row_factory = sqlite3.Row #Irá permitir as colunas pelo nome
    return conn

@app.route("/")
def index():
    conn = get_db_connection()

    # 1. Pegará o Usuário
    usuario = conn.execute('SELECT * FROM Usuarios').fetchone()

    # 2. Pegará as Transações
    # Nesse momento, ocorrerá a junção da tabela Transacoes com Categorias e Contas, para que seja mostrado o nome da categoria ao ínves de
    # somente mostrar o número de ID.
    query = """SELECT t.*, c.nome_categoria, co.nome_conta
               FROM Transacoes t
               JOIN Categorias c ON t.id_categoria = c.id_categoria
               JOIN Contas co ON t.id_conta = co.id_conta
               ORDER BY t.data DESC"""

    transacoes = conn.execute(query).fetchall()

    conn.close()

# 3. Envia tudo para o HTML
    return render_template('index.html', nome=usuario['nome'], lista_transacoes = transacoes)

if (__name__) == "__main__":
    app.run(debug=True)