from AdicionarProduto import AdicionarProduto
from Produto import Produto



def Listar_Todos_Produtos (adicionar_produto):
    lista_produtos = adicionar_produto.listar_produtos()
    return lista_produtos


# adicionar_produto = AdicionarProduto()
# produto1 = Produto(1, "Produto A", 10.99)
# produto2 = Produto(2, "Produto B", 19.99)
# produto3 = Produto(3, "Produto C", 5.99)

# adicionar_produto.adicionar_produto(produto1)
# adicionar_produto.adicionar_produto(produto2)
# adicionar_produto.adicionar_produto(produto3)

# print(Listar_Todos_Produtos(adicionar_produto))

