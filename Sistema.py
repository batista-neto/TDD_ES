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
