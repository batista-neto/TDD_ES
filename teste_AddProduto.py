import unittest
from AdicionarProduto import AdicionarProduto
from Produto import Produto

class TestAdicionarProduto(unittest.TestCase):

    def test_adicionar_produto(self):
        produto = Produto(1, 'arroz', 19.90)
        adicionar_produto = AdicionarProduto()
        resposta = adicionar_produto.adicionar_produto(produto)
        self.assertEqual(resposta, "Adicionado com sucesso")

    def test_produto_sem_id(self):
        produto = Produto(None, 'feijao', 6.90)
        adicionar_produto = AdicionarProduto()
        resposta = adicionar_produto.adicionar_produto(produto)
        self.assertEqual(resposta, "Produto sem id, tente novamente")

    def test_produto_ja_adicionado(self):
        produto1 = Produto(1, 'feijao', 6.90)
        produto2 = Produto(1, 'arroz', 19.90)
        adicionar_produto = AdicionarProduto()
        resposta = adicionar_produto.adicionar_produto(produto1)
        resposta = adicionar_produto.adicionar_produto(produto2)
        self.assertEqual(resposta, "Produto com esse ID já existe, tente novamente")

if __name__ == '__main__':
    unittest.main()
