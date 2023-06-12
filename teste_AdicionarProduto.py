import unittest
from Produto import Produto
from Sistema import Sistema

class TestAdicionarProduto(unittest.TestCase):

    def test_adicionar_produto(self):
        produto = Produto(id = 1, nome = 'arroz', valor = 19.90)
        sistema = Sistema()
        resposta = sistema.adicionar_produto(produto)
        self.assertEqual(resposta, "Adicionado com sucesso")

    def test_produto_sem_id(self):
        produto = Produto( id = None, nome = 'feijao', valor = 6.90)
        sistema = Sistema()
        resposta = sistema.adicionar_produto(produto)
        self.assertEqual(resposta, "Produto sem id, tente novamente")

    def test_produto_ja_adicionado(self):
        produto1 = Produto(id = 1, nome = 'feijao', valor = 6.90)
        produto2 = Produto(id = 1, nome = 'arroz', valor = 19.90)
        sistema = Sistema()
        resposta = sistema.adicionar_produto(produto1)
        resposta = sistema.adicionar_produto(produto2)
        self.assertEqual(resposta, "Produto com esse ID já existe, tente novamente")

if __name__ == '__main__':
    unittest.main()
