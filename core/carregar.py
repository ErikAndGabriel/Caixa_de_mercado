import json 
import os 

pasta_atual = os.path.dirname(os.path.abspath(__file__))

def carregar_mercadorias():
    caminho = os.path.join(pasta_atual, "..", "dados", "mercadorias.json")
    with open(caminho, "r", encoding="utf-8") as arq:
        return json.load(arq)
        
def carregar_sql():
    caminho = os.path.join(pasta_atual, "..", "dados", "SQL.json")
    with open(caminho, "r", encoding="utf-8") as arq:
        return json.load(arq)
        
