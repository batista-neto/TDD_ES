from Sistema import Sistema
from fastapi  import FastAPI
from Produto import Produto

app = FastAPI()

sistema = Sistema()

@app.post("/produtos")
def adicionar_produto(produto: Produto):
    return sistema.adicionar_produto(produto)

@app.delete("/produtos/{id}")
def deletar_produto(id: int):
    return sistema.deletar_produto(id)

@app.put("/produtos/{id}")
def atualizar_produto(id: int, novo_nome: str, novo_valor: float):
    return sistema.atualizar_produto(id, novo_nome, novo_valor)

@app.get("/produtos")
def listar_todos_produtos():
    return sistema.listar_todos_produtos()

@app.get("/produtos/{id}")
def consultar_um_produto(id: int):
    return sistema.consultar_produto(id)