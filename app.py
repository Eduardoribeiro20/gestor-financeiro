#Importação do Flask
from flask import Flask

#Criação da Aplicação
app = Flask (__name__)

#Criação da primeira "rota" (Página Inicial)
@app.route("/")
def hello_world():
    return "<p>Olá, mundo! Este é o motor do meu Gestor Financeiro!</p>"

if __name__ == "__main__":
    app.run(debug=True)