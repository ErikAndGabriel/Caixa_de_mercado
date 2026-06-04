import json
import os 

pasta_atual = os.path.dirname(os.path.abspath(__file__))

def remover_produto(id_produto):
    arquivo = os.path.join(pasta_atual, "..", "dados", "carrinho.json")
    with open(arquivo, "r") as arq:
        data = json.load(arq)
    for p in data:
        if p == id_produto:
           p['cancelamento'] == True
    with open(arquivo, "w") as arq:
        json.dump(data, arq, indent=4)
