import unittest
from AdicionarProduto import AdicionarProduto

adicionar_produto = AdicionarProduto()

def test_read_product():
    produtoA = adicionar_produto(1,"Product A", 10.99)
    produtoB = adicionar_produto(2,"Product B", 15.99)
    produtoC = adicionar_produto(3,"Product C", 20.99)

    adicionar_produto.adicionar_produto(produtoA)
    adicionar_produto.adicionar_produto(produtoB)
    adicionar_produto.adicionar_produto(produtoC)
    
    with unittest.assertLogs(level='INFO') as logs:
        read_product("Product A", 2)
        read_product(2, 2)
        read_product(20.99, 3)
        read_product("Product B", "?")

    # Get the printed output
    output = '\n'.join(logs.output)

    # Assert the expected output
    expected_output = f"Product ID: {produtoA.id}\n" \
                     f"Product Name: {produtoA.name}\n" \
                     f"Product Valor: {produtoA.valor}" \
                     f"Product ID: {produtoB.id}\n" \
                     f"Product Name: {produtoB.name}\n" \
                     f"Product Valor: {produtoB.valor}" \
                     f"Product ID: {produtoC.id}\n" \
                     f"Product Name: {produtoC.name}\n" \
                     f"Product Valor: {produtoC.valor}" \
                     f"Insira um método de busca válido."
    
    unittest.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()