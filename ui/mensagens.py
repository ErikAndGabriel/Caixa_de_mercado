from ui.color import erro, sucesso, aviso, pausa, reset

def mostrar_erro(msg):
    print(erro + msg)
    
def mostrar_sucesso(msg):
    print(sucesso + msg)
    
def mostrar_aviso(msg):
    print(aviso + msg)
    
def pausar():
    input(pausa + "precione [ENTER]")

def reset_color():
    return reset
