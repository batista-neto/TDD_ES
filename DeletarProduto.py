class DeletarProduto:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def deletar_produto(self, id):
        if id is None:
            return "ID não foi inserido, tente novamente"
        
        for produto in self.produtos:
            if produto.id == id:
                self.produtos.remove(produto)
                return "Produto removido com sucesso"
            
        return "Produto com esse ID náo encontrado, tente novamente"