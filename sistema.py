import mysql.connector
from dataclasses import dataclass

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jbneto9!",
    database="tdd"
)
cursor = mydb.cursor()

@dataclass
class Produto:
    name: str
    id: int
    preco: float


def add_product(name, preco):
    query = "INSERT INTO products (name, preco) VALUES (%s, %s)"
    values = (name, preco)
    cursor.execute(query, values)
    mydb.commit()
    return ("Produto cadastrado com sucesso")

