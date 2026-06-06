import json 
from colorama import init, Fore
from core.carregar import carregar_sql 
init()

enumerar = 0
class Visualizar:
    def __init__(self, dados = carregar_sql()):
        self.dados = dados 
        
    def Lista(self):
        for info, produto in self.dados.items():
            enumerar += 1 
            print(f"{enumerar} produto: {info}  codigo: {produto['codigo']}")  
             
