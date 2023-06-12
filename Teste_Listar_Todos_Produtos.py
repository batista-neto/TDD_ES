import unittest
from Produto import Produto
from AdicionarProduto import AdicionarProduto


adicionar_produto = AdicionarProduto()

produto1 = Produto(1, "Produto A", 10.99)
produto2 = Produto(2, "Produto B", 19.99)
produto3 = Produto(3, "Produto C", 5.99)

def test_listar_todos_os_produtos ():
    produtos = Listar_Todos_Produtos()
    assertEqual(len(produtos), 3)
    assertEqual(produtos[0]["id"], 1)
    assertEqual(produtos[0]["nome"], "Produto A")
    assertEqual(produtos[0]["valor"], 10.99)

if __name__ == '__main__':
    unittest.main()