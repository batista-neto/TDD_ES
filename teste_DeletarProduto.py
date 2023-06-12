import unittest

class TestDeletarProduto(unittest.TestCase):

    def test_deletar_produto(self):
        produto1 = Produto(1, 'arroz', 19.90)
        sistema = Sistema()
        sistema.adicionar_produto(produto1)
        resposta = sistema.deletar_produto(1)
        self.assertEqual(resposta, "Produto removido com sucesso")

    def test_deletar_produto_id_incorreto(self):
        sistema = Sistema()
        resposta = sistema.deletar_produto(3)
        self.assertEqual(resposta, "Produto com esse ID náo encontrado, tente novamente")

    def test_deletar_produto_sem_id(self):
        sistema = Sistema()
        resposta = sistema.deletar_produto(None)
        self.assertEqual(resposta, "ID não foi inserido, tente novamente")

if __name__ == '__main__':
    unittest.main()