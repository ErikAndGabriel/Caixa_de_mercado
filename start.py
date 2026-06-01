from src.visualizar import Visualizar
from src.carrinho import Carrinho
from core.apagar import clear
from core.carregar import carregar_config
from ui.mensagens import mostrar_erro, pausar, reset_color
from ui.banner import banner
from tabulate import tabulate
import os
     
def NovoProduto():
    valor_total = 0
    reset = Carrinho(None, None, None) 
    while True:
        try:
            clear()
            reset_color()
            print("""
            Atenção, adicionar codigo em seguida  quantidade, para sair do programa e so digitar 000,
            777 para produto e quantidade para resetar compra""")
            codigo = int(input("codigo: "))
            if codigo == 000:
                 print("[1] resetar compra")
                 print("[2] resetar e sair")
                 print("[3] remover produto")
                 escolha = int(input("escolha: ")
                 if escolha == 1:
                    reset.resetar_compra()
                 elif escolha == 2:
                      reset.resetar_compra()
                      break
                 elif escolha == 3:
                      reset.olhar_lista_carrinho()
                      id = int(input("ID para cancelar: ")                      
                      reset.resetar_compra()
                 else:
                     print("escolha invalida")                               
                      
                      
            if codigo == 777:  
               reset.resetar_compra()
               valor_total = 0
               continue
            quantidade = int(input("quantidade: ")) 
            carrinho = Carrinho(codigo, quantidade, None)
        except ValueError:
             mostrar_erro("somente numeros")
             pausar()
             continue

        valor = carrinho.Adicionar_no_carrinho_codigo()
        carrinho.olhar_lista_carrinho()
        valor_total += valor
        print(valor_total)
        pausar()
        continue
                
                                
def Menu():
    while True:
        try:
            
            clear()
            print(banner)
            reset_color()
            print("[1] olhar produtos")
            print("[2] nova compra")
            print("[3] info")
            print("[0] exit")
            escolha = int(input("\nescolha: "))
        
            if escolha == 1:
                pessoa = Visualizar()
                pessoa.Lista()
                pausar()
                continue                 
            elif escolha == 2:
                NovoProduto()
            
            elif escolha == 3:
                config = carregar_config()
                config_lista = []
                for chave, valor in config.items():
                     config_lista.append({
                          "config": chave,
                          "atual": valor,
                     })
                              
                print(tabulate(config_lista, headers="keys", tablefmt="grid"))
                pausar()
                continue                                  
            elif escolha == 0:
               exit()
                
            else:
                mostrar_erro("escolha invalida")
                pausar()
                continue 
        except ValueError:
            mostrar_erro("somente numeros")
            pausar()
            continue 
     
Menu()
