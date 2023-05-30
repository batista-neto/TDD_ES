import mysql.connector
from dataclasses import dataclass

#estabelece uma conexao com o bd
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jbneto9!",
    database="tdd"
)
cursor = mydb.cursor()

#Funcao que adiciona um produto ao bd
def add_product(name, id, preco):
    try:
        query = "INSERT INTO products (name, id, preco) VALUES (%s, %s, %s)"
        values = (name, id, preco)
        cursor.execute(query, values)
        mydb.commit()
        return ("Produto cadastrado com sucesso")
    except:
        return ("Produto não cadastrado")
    

