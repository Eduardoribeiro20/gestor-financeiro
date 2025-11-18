import sqlite3

# Conecta ao banco de dados
connection = sqlite3.connect('gestor.db')

# Abre o arquivo com a "planta" (schema.sql)
with open ('schema.sql') as f:
    # Executa os comandos SQL do arquivo
    connection.executescript(f.read())

# Cria um cursor (uma ferramenta para mexer no banco)
cur = connection.cursor()

# Faz uma inserção de teste só para garantir que funcionou
cur.execute("INSERT INTO Usuarios (nome, email, senha_hash) VALUES (?, ?, ?)",
            ('Admin', 'admin@exemplo.com', 'senha123'))

# Salva as alterações e fecha conexão
connection.commit()
connection.close()

print("Sucesso! O banco de dados 'gestor.db' foi criado e inicializado")