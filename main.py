from database import initialize_database
from stock_manager import StockManager
from models import Produto, Venda

def exibir_menu():
    print("\n--- Gerenciador de Estoque da Loja ---")
    print("1. Cadastrar Novo Produto")
    print("2. Consultar Produtos")
    print("3. Atualizar Quantidade de Produto")
    print("4. Remover Produto")
    print("5. Registrar Venda")
    print("6. Listar Vendas")
    print("0. Sair")
    print("--------------------------------------")

def main():
    initialize_database()
    
    gerenciador = StockManager()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n--- Cadastrar Novo Produto ---")
            nome = input("Nome do Produto: ")
            descricao = input("Descrição: ")
            
            while True:
                try:
                    quantidade = int(input("Quantidade Disponível: "))
                    if quantidade < 0:
                        print("Quantidade não pode ser negativa. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro para a quantidade.")
            
            while True:
                try:
                    preco = float(input("Preço: "))
                    if preco < 0:
                        print("Preço não pode ser negativo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número para o preço (ex: 12.50).")
            
            gerenciador.cadastrar_produto(nome, descricao, quantidade, preco)

        elif opcao == '2':
            print("\n--- Consultar Produtos ---")
            consulta_opcao = input("Consultar todos (T) ou por ID (I)? (T/I): ").upper()
            if consulta_opcao == 'I':
                while True:
                    try:
                        produto_id = int(input("Digite o ID do Produto: "))
                        if produto_id <= 0:
                            print("ID inválido. Digite um número positivo.")
                            continue
                        break
                    except ValueError:
                        print("Entrada inválida. Digite um número inteiro para o ID.")
                
                produtos = gerenciador.consultar_produtos(produto_id)
                if produtos:
                    for p in produtos:
                        print(f"ID: {p.id}, Nome: {p.nome}, Descrição: {p.descricao}, Qtd: {p.quantidade_disponivel}, Preço: R${p.preco:.2f}")
                else:
                    print(f"Produto com ID {produto_id} não encontrado.")
            elif consulta_opcao == 'T':
                produtos = gerenciador.consultar_produtos()
                if produtos:
                    print("\n--- Lista de Todos os Produtos ---")
                    for p in produtos:
                        print(f"ID: {p.id}, Nome: {p.nome}, Descrição: {p.descricao}, Qtd: {p.quantidade_disponivel}, Preço: R${p.preco:.2f}")
                    print("----------------------------------")
                else:
                    print("Nenhum produto cadastrado.")
            else:
                print("Opção inválida para consulta.")

        elif opcao == '3':
            print("\n--- Atualizar Quantidade de Produto ---")
            while True:
                try:
                    produto_id = int(input("Digite o ID do Produto a ser atualizado: "))
                    if produto_id <= 0:
                        print("ID inválido. Digite um número positivo.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro para o ID.")
            
            while True:
                try:
                    nova_quantidade = int(input("Digite a Nova Quantidade Disponível: "))
                    if nova_quantidade < 0:
                        print("Quantidade não pode ser negativa. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro para a quantidade.")
            
            gerenciador.atualizar_quantidade_produto(produto_id, nova_quantidade)

        elif opcao == '4':
            print("\n--- Remover Produto ---")
            while True:
                try:
                    produto_id = int(input("Digite o ID do Produto a ser removido: "))
                    if produto_id <= 0:
                        print("ID inválido. Digite um número positivo.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro para o ID.")
            
            gerenciador.remover_produto(produto_id)

        elif opcao == '5':
            print("\n--- Registrar Venda ---")
            while True:
                try:
                    produto_id = int(input("Digite o ID do Produto Vendido: "))
                    if produto_id <= 0:
                        print("ID inválido. Digite um número positivo.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro para o ID.")
            
            while True:
                try:
                    quantidade_vendida = int(input("Quantidade Vendida: "))
                    if quantidade_vendida <= 0:
                        print("Quantidade deve ser maior que zero. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro para a quantidade.")
            
            gerenciador.registrar_venda(produto_id, quantidade_vendida)

        elif opcao == '6':
            print("\n--- Listar Vendas ---")
            vendas = gerenciador.listar_vendas()
            if vendas:
                print("\n--- Todas as Vendas ---")
                for venda in vendas:
                    produto_vendido = gerenciador.consultar_produtos(venda.produto_id)
                    nome_produto = produto_vendido[0].nome if produto_vendido else "Produto Desconhecido"
                    print(f"ID Venda: {venda.id_venda}, Produto: {nome_produto} (ID: {venda.produto_id}), Qtd: {venda.quantidade_vendida}, Data: {venda.data_venda}")
                print("-----------------------")
            else:
                print("Nenhuma venda registrada.")

        elif opcao == '0':
            print("Saindo do Gerenciador de Estoque. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()