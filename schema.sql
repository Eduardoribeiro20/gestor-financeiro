CREATE TABLE Usuários (
id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
nome varchar(100) NOT NULL,
email varchar(100) NOT NULL UNIQUE,
senha_hash varchar(100) NOT NULL
);

CREATE TABLE Contas (
id_conta INTEGER PRIMARY KEY AUTOINCREMENT,
id_usuario INTEGER NOT NULL,
nome_conta varchar(100) NOT NULL,
tipo_conta varchar(100) NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
);

CREATE TABLE Categorias (
id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
id_usuário INTEGER NOT NULL,
nome_categoria varchar(100) NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

CREATE TABLE Transacoes (
id_transacoes INTEGER PRIMARY KEY AUTOINCREMENT,
id_usuario INTEGER NOT NULL,
id_conta INTEGER NOT NULL,
id_categoria INTEGER NOT NULL,
valor DECIMAL(10,2) NOT NULL,
tipo varchar(50) NOT NULL,
data DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
descricao TEXT,

FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
FOREIGN KEY (id_conta) REFERENCES Contas(id_conta),
FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria)
);