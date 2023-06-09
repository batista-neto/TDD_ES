import unittest

class TestAdicionarProduto(unittest.TestCase):

    def test_adicionar_produto(self):
        produto = Produto(1, 'arroz', 19.90)
        adicionar_produto = AdicionarProduto()
        resposta = adicionar_produto.adicionar_produto(produto)
        self.assertEqual(resposta, "Adicionado com sucesso")

if __name__ == '__main__':
    unittest.main()
