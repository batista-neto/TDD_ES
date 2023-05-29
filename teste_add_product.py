import unittest
import mysql.connector
from sistema import add_product


def test_add_product():
    # Conexão com o banco de dados MySQL
    conexao = mysql.connector.connect(

        #   Substituir as strings abaixo pelas utilizadas no banco de dados
        host='localhost', 
        user='root',
        password='jbneto9!',
        database='tdd'
    )

    # Criar um cursor para executar as consultas
    cursor = conexao.cursor()

    # Executar a função para adicionar um produto
    add_product("Celular", 999) #Utilizar a função criada que teoricamente ainda nao existe

    # Realizar uma consulta para verificar se o produto foi adicionado
    query = "SELECT * FROM products WHERE name = 'Celular'"
    cursor.execute(query)
    result = cursor.fetchone() #Obter um linha de cada vez

    # Verificar se o produto foi adicionado corretamente
    assert result is not None
    assert result[1] == "Celular"
    assert result[2] == 999

    # Consuma todos os resultados antes de fechar o cursor
    cursor.fetchall()
    
    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()

# Executar o teste
test_add_product()