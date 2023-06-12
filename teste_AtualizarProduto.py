import unittest
from Produto import Produto
from Sistema import Sistema

class TestDeletarProduto(unittest.TestCase):

    def test_atualizar_produto(self):
        produto1 = Produto(id = 1, nome = 'arroz', valor = 19.90)
        sistema = Sistema()
        sistema.adicionar_produto(produto1)
        resposta = sistema.atualizar_produto(1, "feijao", 19.90)
        self.assertEqual(resposta, "Produto atualizado com sucesso")

    def test_atualizar_produto_nao_existe(self):
        produto1 = Produto(id = 1, nome = 'arroz', valor = 19.90)
        sistema = Sistema()
        sistema.adicionar_produto(produto1)
        resposta = sistema.atualizar_produto(2, "feijao", 19.90)
        self.assertEqual(resposta, "Produto com esse ID não encontrado, tente novamente")

    def test_atualizar_produto_sem_nome(self):
        produto1 = Produto(id = 1, nome = 'arroz', valor = 19.9)
        sistema = Sistema()
        sistema.adicionar_produto(produto1)
        resposta = sistema.atualizar_produto(2, None, 19.90)
        self.assertEqual(resposta, "Nome não foi inserido, tente novamente")


if __name__ == '__main__':
    unittest.main()