import json 
from core.carregar import carregar_mercadorias, carregar_sql
from core.adicionar import adicionar_produto 
class Carrinho:
    def __init__(self, codigo, quantidade):
        self.codigo = codigo
        self.quantidade = quantidade
        self.dados = carregar_sql()
        self.carrinho = carregar_mercadorias()
        self.total = 0
        
    def Adicionar_no_carrinho_codigo(self):
            for chave, valor in self.dados.items():                  
                if self.codigo == valor['codigo']:
                    valor_unitario = valor['valor'] * self.quantidade
                    self.carrinho[self.codigo] = {
                    
                       "nome": valor['nome'],
                       "valor": valor_unitario,
                       "quantidade": self.quantidade,       
                           
                    }
                    adicionar_produto(self.carrinho)
                    
                    self.total += valor_unitario
                    return "produto adicionado!"
                    
            return f"o codigo {self.codigo} não esta cadastrado!"
         
    def olhar_lista_carrinho(self):
        if not self.carrinho:
            return "o carrinho esta vazio!"
            
        for chave, valor in self.carrinho.items():
            print(f"produto : {valor['nome']}  quantidade : {valor['quantidade']}  valor : {valor['valor']}")
        print(f"valor total : {self.total}")           
