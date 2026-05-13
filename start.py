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
    while True:
        try:
            clear()
            reset_color()
            print("""
            Atenção, adicionar codigo em seguida  quantidade, para sair do programa e so digitar 000""")
            codigo = int(input("codigo: "))                
            quantidade = int(input("quantidade: ")) 
        except ValueError:
             mostrar_erro("somente numeros")
             pausar()
             continue
        if codigo == 000 or quantidade == 000:
           break
        if codigo == 777 or quantidade == 777:
            pessoa = Carrinho(None, None)
            pessoa.resetar_compra()
            valor_total = 0
        else:
            pessoa = Carrinho(codigo, quantidade)
            valor = pessoa.Adicionar_no_carrinho_codigo()
            print(pessoa.olhar_lista_carrinho())
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
                config_lista = [{
                     "config": c,
                     "atual": v,
                     } for k in v config.items()]
                              
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
