import json 
from ui.color import erro, sucesso
from core.carregar import carregar_sql 

class Visualizar:
    def __init__(self, dados = carregar_sql()):
        self.dados = dados 
        self.enumerar = 0
        
    def Lista(self):
        for info, produto in self.dados.items():
            print(f"{sucesso}{self.enumerar} produto: {info}  codigo: {produto['codigo']}")  

