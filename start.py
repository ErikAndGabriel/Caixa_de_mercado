from src.visualizar import Visualizar
from src.carrinho import Carrinho
from core.apagar import clear
from core.carregar import carregar_config
import os

print("carregando templates")
os.system("python run.py")
def NovoProduto():
    while True:
        try:
            clear()
            print("""
            Atenção, adicionar codigo em seguida  quantidade, para sair do programa e so digitar 000""")
            codigo = int(input("codigo: "))                
            quantidade = int(input("quantidade: ")) 
        except ValueError:
             print("somente numeros!")
             input("precione [Enter]")
             continue
        if codigo == 000 or quantidade == 000:
           break
        else:
            pessoa = Carrinho(codigo, quantidade)
            pessoa.Adicionar_no_carrinho_codigo()
            print(pessoa.olhar_lista_carrinho())
            input()
            continue
                
                                
def Menu():
    while True:
        try:
            clear()
            print("[1] olhar produtos")
            print("[2] nova compra")
            print("[3] info")
            print("[0] exit")
            escolha = int(input("\nescolha: "))
        
            if escolha == 1:
                pessoa = Visualizar()
                pessoa.Lista()
                input("\nprecione [ENTER]")
            elif escolha == 2:
                NovoProduto()
            
            elif escolha == 3:
                for chave, valor in carregar_config().items():
                    print(chave, valor)
                input("precione [ENTER]")
                clear()
                                 
            elif escolha == 0:
               exit()
                
            else:
                print("escolha invalida")
                input("precione [ENTER]")
                continue
        except ValueError:
            print("somente numeros")
            input("precione [ENTER]")
            continue
if __name__ == "__main__":
     Menu()
