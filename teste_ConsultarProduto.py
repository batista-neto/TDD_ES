import unittest
from Produto import Produto
from Sistema import Sistema

class TestConsultarProduto(unittest.TestCase):

    def test_consultar_produto(self):
        sistema = Sistema()
        produto1 = Produto(id = 1, nome = "Produto A", valor = 10.99)
        produto2 = Produto(id = 2, nome = "Produto B", valor = 19.99)
        sistema.adicionar_produto(produto1)
        sistema.adicionar_produto(produto2)
        resposta = sistema.consultar_produto(2)
        self.assertEqual(resposta, [{'id': 2, 'nome': 'Produto B', 'valor': 19.99}])
   
    def test_consultar_produto_sem_id(self):
        sistema = Sistema()
        produto1 = Produto(id = 1, nome = "Produto A", valor = 10.99)
        sistema.adicionar_produto(produto1)
        resposta = sistema.consultar_produto(None)
        self.assertEqual(resposta, "ID não inserido, tente novamente")

    def test_consultar_produto_nao_existe(self):
        sistema = Sistema()
        produto1 = Produto(id = 1, nome = "Produto A", valor = 10.99)
        sistema.adicionar_produto(produto1)
        resposta = sistema.consultar_produto(2)
        self.assertEqual(resposta, "Produto com esse ID não encontrado, tente novamente")

if __name__ == '__main__':
    unittest.main()