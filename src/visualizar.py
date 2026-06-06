import json 
from colorama import init, Fore
from core.carregar import carregar_sql 
init()

class Visualizar:
    def __init__(self, dados = carregar_sql()):
        self.dados = dados 
        self.enumerar = 0
        
    def Lista(self):
        for info, produto in self.dados.items():
            self.enumerar += 1 
            print(f"{self.enumerar} produto: {info}  codigo: {produto['codigo']}")  
             
