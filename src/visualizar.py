import json 
from colorama import init, Fore
from core.carregar import carregar_sql 
init()

class Visualizar:
    def __init__(self, dados = carregar_sql()):
        self.dados = dados 
        
    def Lista(self):
        for info, produto in self.dados.items():
            print(f"produto: {info}  codigo: {produto['codigo']}")  
             
