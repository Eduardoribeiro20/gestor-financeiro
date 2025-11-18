#Importação do Flask
#from flask import Flask

#Criação da Aplicação
#app = Flask (__name__)

#Criação da primeira "rota" (Página Inicial)
#@app.route("/")
#def hello_world():
#    return "<p>Olá, mundo! Este é o motor do meu Gestor Financeiro!</p>"

#if __name__ == "__main__":
 #   app.run(debug=True)




import sqlite3
from flask import Flask

app = Flask(__name__)

# Função para conectar ao Banco de Dados
def get_db_connection():
    conn = sqlite3.connect('gestor.db')
    conn.row_factory = sqlite3.Row #Irá permitir as colunas pelo nome
    return conn

@app.route("/")
def index():
    # 1. Conecta no Banco
    conn = get_db_connection()

   # 2. Busca todos os usuários
    usuarios = conn.execute('SELECT * FROM Usuarios').fetchall()

   # 3. Fecha conexão
    conn.close()

  # 4. Pega o primeiro usuário da lista (o admin)
    usuario_admin = usuarios[0]

  # 5. Mostra na Tela
    return f"<h1> Olá, {usuario_admin['nome']}! </h1> <p>Seu email é: {usuario_admin['email']}</p>"

if __name__ == "__main__":
    app.run (debug=True)