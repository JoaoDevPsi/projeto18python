import sqlite3 # Adicionado: Importa o módulo sqlite3
from database import get_db_connection
from models import Produto, Venda
from datetime import datetime

class StockManager:
    def __init__(self):
        pass

    def cadastrar_produto(self, nome, descricao, quantidade_disponivel, preco):
        conn = get_db_connection()
        if conn is None:
            return None
        
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Produtos (Nome, Descricao, QuantidadeDisponivel, Preco) VALUES (?, ?, ?, ?)",
                (nome, descricao, quantidade_disponivel, preco)
            )
            conn.commit()
            print(f"Produto '{nome}' cadastrado com sucesso! ID: {cursor.lastrowid}")
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar produto: {e}")
            return None
        finally:
            conn.close()

    def consultar_produtos(self, produto_id=None):
        conn = get_db_connection()
        if conn is None:
            return []
        
        cursor = conn.cursor()
        produtos = []
        try:
            if produto_id:
                cursor.execute("SELECT ID, Nome, Descricao, QuantidadeDisponivel, Preco FROM Produtos WHERE ID = ?", (produto_id,))
            else:
                cursor.execute("SELECT ID, Nome, Descricao, QuantidadeDisponivel, Preco FROM Produtos")
            
            rows = cursor.fetchall()
            for row in rows:
                produto = Produto(row[0], row[1], row[2], row[3], row[4])
                produtos.append(produto)
        except sqlite3.Error as e:
            print(f"Erro ao consultar produtos: {e}")
        finally:
            conn.close()
        return produtos

    def atualizar_quantidade_produto(self, produto_id, nova_quantidade):
        conn = get_db_connection()
        if conn is None:
            return False
        
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE Produtos SET QuantidadeDisponivel = ? WHERE ID = ?",
                (nova_quantidade, produto_id)
            )
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Quantidade do produto ID {produto_id} atualizada para {nova_quantidade}.")
                return True
            else:
                print(f"Produto ID {produto_id} não encontrado.")
                return False
        except sqlite3.Error as e:
            print(f"Erro ao atualizar quantidade: {e}")
            return False
        finally:
            conn.close()

    def remover_produto(self, produto_id):
        conn = get_db_connection()
        if conn is None:
            return False
        
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Produtos WHERE ID = ?", (produto_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Produto ID {produto_id} removido com sucesso.")
                return True
            else:
                print(f"Produto ID {produto_id} não encontrado.")
                return False
        except sqlite3.Error as e:
            print(f"Erro ao remover produto: {e}")
            return False
        finally:
            conn.close()

    def registrar_venda(self, produto_id, quantidade_vendida):
        conn = get_db_connection()
        if conn is None:
            return None
        
        cursor = conn.cursor()
        try:
            # 1. Verificar a disponibilidade do produto
            produto = self.consultar_produtos(produto_id)
            if not produto:
                print(f"Erro: Produto ID {produto_id} não encontrado.")
                return None
            
            produto = produto[0] # Pega o objeto Produto da lista
            if produto.quantidade_disponivel < quantidade_vendida:
                print(f"Erro: Quantidade insuficiente em estoque para o produto '{produto.nome}'. Disponível: {produto.quantidade_disponivel}")
                return None
            
            # 2. Registrar a venda
            data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                "INSERT INTO Vendas (ProdutoID, QuantidadeVendida, DataVenda) VALUES (?, ?, ?)",
                (produto_id, quantidade_vendida, data_venda)
            )
            venda_id = cursor.lastrowid
            
            # 3. Atualizar a quantidade disponível do produto
            nova_quantidade_produto = produto.quantidade_disponivel - quantidade_vendida
            self.atualizar_quantidade_produto(produto_id, nova_quantidade_produto)
            
            conn.commit()
            print(f"Venda registrada com sucesso! ID da Venda: {venda_id}")
            return venda_id
        except sqlite3.Error as e:
            print(f"Erro ao registrar venda: {e}")
            return None
        finally:
            conn.close()

    def listar_vendas(self):
        conn = get_db_connection()
        if conn is None:
            return []
        
        cursor = conn.cursor()
        vendas = []
        try:
            cursor.execute("SELECT IDVenda, ProdutoID, QuantidadeVendida, DataVenda FROM Vendas")
            rows = cursor.fetchall()
            for row in rows:
                venda = Venda(row[0], row[1], row[2], row[3])
                vendas.append(venda)
        except sqlite3.Error as e:
            print(f"Erro ao listar vendas: {e}")
        finally:
            conn.close()
        return vendas
