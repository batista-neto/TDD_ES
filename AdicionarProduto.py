class AdicionarProduto:
    def __init__(self):
        self.produtos_adicionados = []

    def adicionar_produto(self, produto):
        if produto.id is None:
            return "Produto sem id, tente novamente"

        for produto in self.produtos_adicionados:
            if produto.id == produto.id:
                return "Produto com esse ID já existe, tente novamente"

        self.produtos_adicionados.append(produto)
        return "Adicionado com sucesso"
