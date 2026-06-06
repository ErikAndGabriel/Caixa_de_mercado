from src.visualizar import Visualizar
from src.carrinho import Carrinho
from core.apagar import clear
from core.carregar import carregar_config
from ui.mensagens import mostrar_erro, pausar, reset_color
from ui.banner import banner
from ui.menus import menu_nova_compra, menu_inicial, menu_forma_de_pagamento
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
            Atenção, adicionar codigo em seguida a quantidade, para menu de reset
            ou remover produto digitar (0 ou 00 ou 000....""")
            print(10 * "=", "produtos", 10 * "=")
            reset.olhar_lista_carrinho()
            prin(29 * "=")
            codigo = int(input("codigo: "))
            
            if codigo == 000:
                while True:
                    clear()
                    try:
                        print(menu_nova_compra)
                        escolha = int(input("escolha: "))
                        
                        if escolha == 1:
                            reset.resetar_compra()
                            valor_total = 0
                            break
                        elif escolha == 2:
                            reset.resetar_compra()
                            valor_total = 0
                            return  
                        elif escolha == 3:
                               
                            reset.olhar_lista_carrinho()
                            try:
                                id_produto = int(input("ID para cancelar: "))
                                remover = Carrinho(None, None, id_produto)
                                remover.cancelar_um_produto()  
                            except ValueError:
                                mostrar_erro("ID inválido!")
                            break
                        else:
                            print("escolha invalida")
                            pausar()
                    except ValueError:
                        mostrar_erro("somente numeros")
                        pausar()
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
        print(f"Valor total: R$ {valor_total:.2f}")
        pausar()
        continue
                
def Menu():
    while True:
        try:
            clear()
            print(banner)
            print(menu_inicial)
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
     
if __name__ == "__main__":
    Menu()
