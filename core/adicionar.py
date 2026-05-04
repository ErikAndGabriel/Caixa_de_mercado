import json
import os 

def adicionar_carrinho(dados):
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    arquivo = os.path.join(pasta_atual, "..", "dados", "carrinho.json")
    with open(arquivo, "w") as arq:
        json.dump(dados, arq, indent=4)
