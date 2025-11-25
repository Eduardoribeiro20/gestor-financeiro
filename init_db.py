import sqlite3
import os

if os.path.exists('gestor.db'):
    os.remove('gestor.db')
    
connection = sqlite3.connect('gestor.db')

with open ('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


# 1. Criação de Usuário
print("Criando Usuário...")
cur.execute("INSERT INTO Usuarios (nome, email, senha_hash) VALUES(?, ?, ?)" , ('Eduardo Admin', 'eduardo@admin.com', 'senha123'))

# 2. Criando Contas (Carteira e Banco)
print("Criando Contas...")
cur.execute("INSERT INTO Contas (id_usuario, nome_conta, tipo_conta) VALUES(?, ?, ?)", (1, 'Carteira Física', 'Dinheiro'))
cur.execute("INSERT INTO Contas (id_usuario, nome_conta, tipo_conta) VALUES(?, ?, ?)", (1, 'Inter', 'Conta Corrente'))

# 3. Criação de Categorias
print("Criando Categorias...")
cur.execute("INSERT INTO Categorias (id_usuario, nome_categoria) VALUES(?, ?)", (1, 'Salário'))
cur.execute("INSERT INTO Categorias (id_usuario, nome_categoria) VALUES(?, ?)", (1, 'Alimentação'))
cur.execute("INSERT INTO Categorias (id_usuario, nome_categoria) VALUES(?, ?)", (1, 'Transporte'))
cur.execute("INSERT INTO Categorias (id_usuario, nome_categoria) VALUES(?, ?)", (1, 'Lazer'))
cur.execute("INSERT INTO Categorias (id_usuario, nome_categoria) VALUES (?, ?)", (1, 'Carro'))

# 4. Criações de Transações Fictícias
print("Criando Transações...")

# Receita (Salário) na conta Inter (ID 2)
cur.execute("""INSERT INTO Transacoes (id_usuario, id_conta, id_categoria, valor, tipo, descricao, data)
            VALUES (1, 2, 1, 7000.00, 'Receita', 'Salário Mensal', '2025-11-01')""")

# Despesa (Fast Food) no Inter (ID 2)
cur.execute("""INSERT INTO Transacoes (id_usuario, id_conta, id_categoria, valor, tipo, descricao, data)
            VALUES (1, 2, 2, 600.00, 'Despesa', 'Fast Food', '2025-11-25')""")

# Despesa (Manutenção do Carro) na Carteira (ID 1)
cur.execute("""INSERT INTO Transacoes (id_usuario, id_conta, id_categoria, valor, tipo, descricao, data)
            VALUES (1, 1, 5, 750.00, 'Despesa', 'Troca de Óleo', '2025-11-30')""")

connection.commit()
connection.close()

print("Sucesso! Banco de Dados recriado com dados de teste.")