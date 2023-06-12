class Sistema:
    def __init__(self):
            self.produtos = []


    def adicionar_produto(self, produto):
        if produto.id is None:
            return "Produto sem id, tente novamente"

        for p in self.produtos:
            if p.id == produto.id:
                return "Produto com esse ID já existe, tente novamente"

        self.produtos.append(produto)
        return "Adicionado com sucesso"
    
    def deletar_produto(self, id):
        if id is None:
            return "ID não foi inserido, tente novamente"
            
        for produto in self.produtos:
            if produto.id == id:
                self.produtos.remove(produto)
                return "Produto removido com sucesso"
                
        return "Produto com esse ID náo encontrado, tente novamente"