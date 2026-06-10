import json 
from core.carregar import carregar_carrinho, carregar_sql
from core.adicionar import adicionar_carrinho
from core.resetar import resetar_carrinho
from core.remover import remover_produto 
from ui.mensagens import mostrar_erro, mostrar_sucesso 

class Carrinho:
    def __init__(self, codigo, quantidade, id):
        self.codigo = codigo
        self.quantidade = quantidade
        self.id = id
        self.dados = carregar_sql()
        self.carrinho = carregar_carrinho()
        self.enumerar = 0
        self.total = 0
        
    def Adicionar_no_carrinho_codigo(self):
            for chave, valor in self.dados.items():                  
                if self.codigo == valor['codigo']:
                    valor_unitario = valor['valor'] * self.quantidade

                    if self.carrinho:
                        proximo_id = max(int(penis) for penis in self.carrinho.keys()) + 1
                    else:
                        proximo_id = 1
                        
                    self.carrinho[proximo_id] = {
                    
                       "nome": valor['nome'],
                       "valor": valor_unitario,
                       "quantidade": self.quantidade,
                       "cancelamento": False,                           
                    }
                    adicionar_carrinho(self.carrinho)
                    
                    self.total += valor_unitario
                    mostrar_sucesso("produto adicionado!")
                    return self.total
                    
            return f"o codigo {self.codigo} não esta cadastrado!"
         
    def olhar_lista_carrinho(self):
        if not self.carrinho:
            return "o carrinho esta vazio!"
            
        for chave, valor in self.carrinho.items():
            self.enumerar += 1
            print(f"{self.enumerar} produto : {valor['nome']}  quantidade : {valor['quantidade']}  valor : {valor['valor']}")
        
        
    def resetar_compra(self):
        resetar_carrinho()  
        
    def cancelar_um_produto(self):
        data = self.carrinho 
        if self.id == data:
            for i in data:
                self.total += int(i['valor'])
        else:
            return "produto não adicionado"
        remover_produto(self.id)
        return self.total
        
    def obter_dados(self):
        return self.dados
