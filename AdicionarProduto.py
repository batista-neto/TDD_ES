from Produto import Produto

class AdicionarProduto:
    def __init__(self):
        self.produtos_adicionados = []

    def adicionar_produto(self, produto):
        if produto.id is None:
            return "Produto sem id, tente novamente"

        for prod in self.produtos_adicionados:
            if prod.id == produto.id:
                return "Produto com esse ID já existe, tente novamente"

        self.produtos_adicionados.append(produto)
        print("Adicionado com sucesso")
        return self.produtos_adicionados

    def listar_produtos(self):
        return [produto.__dict__ for produto in self.produtos_adicionados]

adicionar_produto = AdicionarProduto()    

a = Produto(1, 'arroz', 19.90)
produto2 = Produto(2, 'Produto B', 20.99)

adicionar_produto.adicionar_produto(a)
adicionar_produto.adicionar_produto(produto2)

c = adicionar_produto.listar_produtos()

print(c)