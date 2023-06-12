from AdicionarProduto import AdicionarProduto
from Produto import Produto

adicionar_produto = AdicionarProduto()


def read_product(product, search_method): #Nesta função o usuário deve informar
                                          # o método de busca (ID, nome, valor)

    lista_produtos = adicionar_produto.listar_produtos()
    if search_method == 1: #ID   
        for i in lista_produtos:
            if i['id'] == product:
            
                return i

        print("Produto não encontrado.")

    elif search_method == 2: #NAME
        
        lista_nomes_iguais = []
        for i in lista_produtos:
            
            if i['nome'] == product:
                lista_nomes_iguais.append(i)
                return lista_nomes_iguais

    elif search_method == 3: #VALOR

        lista_valores_iguais = []
        for i in lista_produtos:
            if i['valor'] == product:
                lista_valores_iguais.append(i)

                return lista_valores_iguais
            
    else: 
        print("Insira um método de busca válido.")



