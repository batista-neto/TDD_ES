class AdicionarProduto:
    def __init__(self):
        self.produtos_adicionados = []

    def adicionar_produto(self, produto):
        self.produtos_adicionados.append(produto)

        if len(self.produtos_adicionados) > 0:
            return "Adicionado com sucesso"
