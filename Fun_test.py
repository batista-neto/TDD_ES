import unittest
import mysql.connector


def test_add_product():
    # Conexão com o banco de dados MySQL
    conexao = mysql.connector.connect(

        #   Substituir as strings abaixo pelas utilizadas no banco de dados
        host='localhost', 
        user='usuario',
        password='senha',
        database='banco_de_dados'
    )

    # Criar um cursor para executar as consultas
    cursor = conexao.cursor()

    # Executar a função para adicionar um produto
    add_product("Celular", 9, 999) #Utilizar a função criada que teoricamente ainda nao existe

    #SEGUNDO COMMIT: FOI ADICIONADO O CAMPO "ID"

    # Realizar uma consulta para verificar se o produto foi adicionado
    query = "SELECT * FROM products WHERE name = 'Celular'"
    cursor.execute(query)
    result = cursor.fetchone() #Obter um linha de cada vez

    # Verificar se o produto foi adicionado corretamente
    assert result is not None
    assert result[1] == "Celular"
    assert result[2] == 9
    assert result[2] == 999

    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()

# Executar o teste
test_add_product()