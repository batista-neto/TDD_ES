import unittest
from Produto import Produto
from DeletarProduto import DeletarProduto

class TestDeletarProduto(unittest.TestCase):

    def test_deletar_produto(self):
        produto1 = Produto(1, 'arroz', 19.90)
        deletar_produto = DeletarProduto()
        deletar_produto.adicionar_produto(produto1)
        resposta = deletar_produto.deletar_produto(1)
        self.assertEqual(resposta, "Produto removido com sucesso")

    def test_deletar_produto_id_incorreto(self):
        deletar_produto = DeletarProduto()
        resposta = deletar_produto.deletar_produto(3)
        self.assertEqual(resposta, "Produto com esse ID náo encontrado, tente novamente")

    def test_deletar_produto_sem_id(self):
        deletar_produto = DeletarProduto()
        resposta = deletar_produto.deletar_produto(None)
        self.assertEqual(resposta, "ID não foi inserido, tente novamente")

if __name__ == '__main__':
    unittest.main()