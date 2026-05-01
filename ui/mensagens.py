from color import erro, sucesso, aviso, pausa

def erro(msg):
    print(erro + msg)
    
def sucesso(msg):
    print(sucesso + msg)
    
def aviso(msg):
    print(aviso + msg)
    
def pausar(msg):
    input(pausa + "precione [ENTER]")  
    continue    