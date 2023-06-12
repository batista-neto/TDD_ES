import unittest
from Produto import Produto
from Sistema import Sistema

class TestListarTodosProdutos(unittest.TestCase):

    def test_listar_produtos (self):
        sistema = Sistema()
        produto1 = Produto(1, 'arroz', 19.90)
        produto2 = Produto(2, 'feijao', 6.90)
        produto3 = Produto(3, "macarrao", 8.99)
        sistema.adicionar_produto(produto1)
        sistema.adicionar_produto(produto2)
        sistema.adicionar_produto(produto3)

        produtos = sistema.listar_todos_produtos()
        self.assertEqual(len(produtos), 3)
        self.assertEqual(produtos[0]["id"], 1)
        self.assertEqual(produtos[1]["nome"], "feijao")
        self.assertEqual(produtos[2]["valor"], 8.99)

    def test_listar_produtos_com_zero_produtos_na_lista (self):
        sistema = Sistema()
        resposta = sistema.listar_todos_produtos()
        self.assertEqual(resposta, "Nenhum produto adicionado a lista")
    
if __name__ == '__main__':
    unittest.main()