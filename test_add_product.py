import unittest
import mysql.connector
from sistema import add_product
from sistema import mydb


def test_add_product():
    # Conexão com o banco de dados MySQL
    conexao = mydb

    # Criar um cursor para executar as consultas
    cursor = conexao.cursor()

    # Executar a função para adicionar um produto
    resultado = add_product("Celular", 3, 999) 
    
    # Realizar uma consulta para verificar se o produto foi adicionado
    query = "SELECT * FROM products WHERE id = 3"
    cursor.execute(query)
    result = cursor.fetchone() #Obter um linha de cada vez

    # Verificar se o produto foi adicionado corretamente
    assert result is not None
    assert result[0] == 3
    assert result[1] == "Celular"
    assert result[2] == 999

    # Excluir o produto adicionado
    query = "DELETE FROM products WHERE id = %s"
    values = (3,) 
    cursor.execute(query, values)
    conexao.commit()
    
    # Consuma todos os resultados antes de fechar o cursor
    cursor.fetchall()
    
    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()

# Executar o teste
test_add_product()