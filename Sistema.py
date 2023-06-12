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
    
    def atualizar_produto(self, id, novo_nome, novo_valor):
        if id is None:
            return "ID do produto não fornecido. Forneça o ID do produto para realizar a atualização."
        
        if novo_nome is None:
            return "Nome não foi inserido, tente novamente"
        
        for produto in self.produtos:
            if produto.id == id:
                produto.nome = novo_nome
                produto.valor = novo_valor
                return "Produto atualizado com sucesso"

        return "Produto com esse ID não encontrado, tente novamente"
    
    def listar_todos_produtos(self):
        if len(self.produtos) == 0:
            return "Nenhum produto adicionado a lista"
        
        return [produto.__dict__ for produto in self.produtos]