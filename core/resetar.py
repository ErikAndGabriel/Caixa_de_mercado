import json 

pasta_atual = os.path.dirname(os.path.abspath(__file__))

def resetar_carrinho():
  arquivo = os.path.join(pasta_atual, "..", "dados", "carrinho.json")
  with open(arquivo, "w") as arq:
    json.dump({}, arq, indent=4)
