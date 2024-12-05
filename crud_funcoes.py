"""
Cada funcao realiza uma das seguintes tarefas:
    1- Estabelece uma conexão com o banco de dados.
    2- Executa um comando SQL para inserir os dados.
    3- Comita as alterações e fecha a conexão.
    4- Encerra a conexao com o banco de dados.

"""

# Importa as bibliotecas necessárias para conectar ao MySQL e manipular dados usando Pandas.
import mysql.connector
import pandas as pd  # Importando pandas para manipulação de dados

# Cria e retorna uma conexão com o banco de dados MySQL com as credenciais fornecidas.
def criar_conexao():
    return mysql.connector.connect(
        user='root',
        password='332211aa',
        host='localhost',
        database='bdyoutube'
    )

# Adiciona produto e valor na tabela
def InserirDados(produto, valor):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    comando = f'INSERT INTO vendas_table (produto, valor) VALUES (%s, %s)'

    cursor.execute(comando, (produto, valor))
    conexao.commit()

    cursor.close()
    conexao.close()


# Função para ler dados da tabela retorna um DataFrame para ser exibido com streamlit table
def LerDados():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    comando = 'SELECT * FROM vendas_table'

    cursor.execute(comando)

    # Obtendo os resultados e os nomes das colunas
    colunas = [desc[0] for desc in cursor.description]
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()
    # Retorna df que sera exibido com streamlit
    return pd.DataFrame(resultados, columns=colunas)

# Função atualiza registro existente na tabela, atraves do ID do produto junto com os novos valores.
def UpdateDados(id, produto, valor):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    comando = f'UPDATE vendas_table SET produto=%s, valor=%s WHERE idvendas_table=%s'

    cursor.execute(comando, (produto, valor, id))

    conexao.commit()

    cursor.close()
    conexao.close()

# Função apaga um registro específico da tabela baseado no ID fornecido.
def ApagarDados(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    comando = f'DELETE FROM vendas_table WHERE idvendas_table=%s'
    # comando e tupla de 1 elemento
    cursor.execute(comando, (id,))

    conexao.commit()

    cursor.close()
    conexao.close()
