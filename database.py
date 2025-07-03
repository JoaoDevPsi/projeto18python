import sqlite3
import os

DB_NAME = 'estoque_loja.db'

def get_db_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def create_tables():
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()

    create_produtos_table_sql = """
    CREATE TABLE IF NOT EXISTS Produtos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Descricao TEXT,
        QuantidadeDisponivel INTEGER NOT NULL,
        Preco REAL NOT NULL
    );
    """

    create_vendas_table_sql = """
    CREATE TABLE IF NOT EXISTS Vendas (
        IDVenda INTEGER PRIMARY KEY AUTOINCREMENT,
        ProdutoID INTEGER NOT NULL,
        QuantidadeVendida INTEGER NOT NULL,
        DataVenda TEXT NOT NULL,
        FOREIGN KEY (ProdutoID) REFERENCES Produtos(ID) ON DELETE CASCADE
    );
    """

    try:
        cursor.execute(create_produtos_table_sql)
        cursor.execute(create_vendas_table_sql)
        conn.commit()
        print("Tabelas 'Produtos' e 'Vendas' criadas com sucesso ou já existentes.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabelas: {e}")
    finally:
        conn.close()

def initialize_database():
    # if os.path.exists(DB_NAME):
    #     os.remove(DB_NAME)
    #     print(f"Banco de dados '{DB_NAME}' removido para um começo limpo.")
    
    create_tables()

if __name__ == "__main__":
    initialize_database()
