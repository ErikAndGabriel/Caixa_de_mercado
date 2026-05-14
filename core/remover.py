import json
import os 

pasta_atual = os.path.dirname(os.path.abspath(__file__))

def adicionar_carrinho(dados):
    arquivo = os.path.join(pasta_atual, "..", "dados", "carrinho.json")
    with open(arquivo, "w") as arq:
        json.dump(dados, arq, indent=4)
