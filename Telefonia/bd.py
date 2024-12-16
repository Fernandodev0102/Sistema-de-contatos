
# Autor: Fernando Pereira Alves
# GitHub: @Fernandodev0102
# Contato: 85976014779



import mysql.connector  # Importa o módulo para interagir com o MySQL

# Função para configurar e abrir a conexão com o banco de dados
def conectar():
    # Conecta ao banco de dados com as credenciais fornecidas
    return mysql.connector.connect(
        host="localhost",   # O host onde o banco de dados está rodando (ex. localhost)
        user="root",        # Usuário do banco de dados (substitua pelo seu usuário)
        port="3306",        # Porta padrão do MySQL
        password="1234",    # Senha do banco de dados (substitua pela sua senha)
        database="telefonia" # Nome do banco de dados onde a tabela de contatos está
    )

# Função para adicionar um novo contato ao banco de dados
def adicionar_contato(nome, numero, cidade):
    # Conecta ao banco de dados e cria um cursor para executar comandos SQL
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        # Executa a instrução SQL para inserir um novo contato na tabela ListaContatos
        cursor.execute(
            "INSERT INTO ListaContatos (Nome, Numero, Cidade) VALUES (%s, %s, %s)",
            (nome, numero, cidade)
        )
        # Confirma a transação, salvando as alterações no banco de dados
        conexao.commit()
    except mysql.connector.Error as err:
        # Exibe uma mensagem de erro caso ocorra algum problema durante a inserção
        print("Erro ao adicionar contato:", err)
    finally:
        # Fecha o cursor e a conexão com o banco de dados
        cursor.close()
        conexao.close()

# Função para listar todos os contatos no banco de dados
def listar_contatos():
    # Conecta ao banco de dados e cria um cursor para executar comandos SQL
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        # Executa a instrução SQL para selecionar todos os contatos da tabela ListaContatos
        cursor.execute("SELECT Nome, Numero, Cidade FROM ListaContatos")
        # Obtém todos os resultados da consulta e os retorna
        contatos = cursor.fetchall()
        return contatos
    except mysql.connector.Error as err:
        # Exibe uma mensagem de erro caso ocorra algum problema na consulta
        print("Erro ao listar contatos:", err)
        return []
    finally:
        # Fecha o cursor e a conexão com o banco de dados
        cursor.close()
        conexao.close()

# Função para deletar um contato da tabela com base no número de telefone
def deletar_contato(numero):
    # Conecta ao banco de dados e cria um cursor para executar comandos SQL
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        # Executa a instrução SQL para deletar o contato com o número especificado
        cursor.execute("DELETE FROM ListaContatos WHERE Numero = %s", (numero,))
        # Confirma a transação, salvando as alterações no banco de dados
        conexao.commit()
    except mysql.connector.Error as err:
        # Exibe uma mensagem de erro caso ocorra algum problema na exclusão
        print("Erro ao deletar contato:", err)
    finally:
        # Fecha o cursor e a conexão com o banco de dados
        cursor.close()
        conexao.close()
