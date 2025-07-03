# projeto18python

Gerenciador de Estoque da Loja
Este é um sistema de gerenciamento de estoque para uma loja, desenvolvido em Python. Ele permite o cadastro, consulta, atualização e remoção de produtos, além do registro e listagem de vendas. O sistema utiliza um banco de dados SQLite para persistência de dados e é construído com princípios de Programação Orientada a Objetos (POO).

Funcionalidades
Cadastro de Produtos: Adicionar novos produtos ao estoque com nome, descrição, quantidade disponível e preço.

Consulta de Produtos: Visualizar todos os produtos cadastrados ou buscar um produto específico por ID.

Atualização de Quantidade: Alterar a quantidade disponível de um produto existente.

Remoção de Produtos: Excluir produtos do cadastro.

Registro de Vendas: Registrar transações de vendas, deduzindo a quantidade do estoque.

Listagem de Vendas: Visualizar todas as vendas realizadas.

Persistência de Dados: Todas as informações são armazenadas em um banco de dados SQLite, garantindo que os dados não sejam perdidos ao fechar o programa.

Estrutura do Projeto
O projeto é organizado em módulos para melhor separação de responsabilidades:

database.py: Responsável pela conexão com o banco de dados SQLite e pela criação das tabelas (Produtos e Vendas).

models.py: Define as classes Produto e Venda, que representam os objetos do sistema, com seus atributos e métodos de conversão para/de dicionários (para o banco de dados).

stock_manager.py: Contém a lógica de negócio principal do sistema, implementando as operações de CRUD para produtos e o gerenciamento de vendas, interagindo com o banco de dados através das funções de database.py e os objetos de models.py.

main.py: A interface de linha de comando (CLI) para o usuário interagir com o sistema.

main_flet.py (Opcional): Uma interface gráfica (GUI) alternativa para o sistema, desenvolvida com a biblioteca Flet.

Tecnologias Utilizadas
Python 3.x

SQLite3: Banco de dados leve e embutido.

Flet (Opcional, para a versão GUI): Framework para construir interfaces gráficas em Python.

Como Usar
Para configurar e executar o projeto, siga os passos abaixo:

Pré-requisitos
Python 3.x instalado no seu sistema.

Git (opcional, para clonar o repositório).

1. Configuração do Ambiente Virtual
É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.

Crie uma pasta para o projeto e navegue até ela no seu terminal:

mkdir gerenciador_estoque_loja
cd gerenciador_estoque_loja

Crie o ambiente virtual:

python -m venv .venv

Ative o ambiente virtual:

No Windows (CMD ou PowerShell):

.venv\Scripts\activate

No Windows (Git Bash):

source .venv/Scripts/activate
# Se o comando acima não funcionar no Git Bash, tente:
# source .venv/bin/activate

No macOS / Linux:

source .venv/bin/activate

Você saberá que o ambiente está ativo quando (.venv) aparecer no início da linha de comando.

2. Instalação das Dependências
Se você for usar a versão com Flet, instale a biblioteca Flet:

pip install flet

3. Copiar os Arquivos do Projeto
Certifique-se de que todos os arquivos (database.py, models.py, stock_manager.py, main.py e main_flet.py) estão na pasta gerenciador_estoque_loja.

4. Inicialização do Banco de Dados
O banco de dados (estoque_loja.db) será criado e as tabelas serão configuradas automaticamente na primeira execução do main.py ou main_flet.py. Se você quiser resetar o banco de dados (apagar todos os dados e tabelas e começar do zero), você pode deletar o arquivo estoque_loja.db da pasta do projeto.

5. Execução do Programa
Você tem duas opções para executar o sistema:

a) Versão de Linha de Comando (CLI)
Use esta versão se preferir interagir via texto no terminal.

Certifique-se de que o ambiente virtual está ativo.

Execute o main.py:

python main.py

Siga as opções do menu no terminal para interagir com o sistema.

b) Versão com Interface Gráfica (GUI - Flet)
Use esta versão se preferir uma interface visual com botões e campos de texto.

Certifique-se de que o ambiente virtual está ativo e o Flet foi instalado (pip install flet).

Execute o main_flet.py:

python main_flet.py

Uma janela do Flet será aberta, permitindo a interação visual com o sistema.

Contribuição
Sinta-se à vontade para explorar o código, sugerir melhorias ou adicionar novas funcionalidades!
