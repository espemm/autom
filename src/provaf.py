"""
Prova Final d'automatització
"""
def sumar2(a,b):
    '''
    Sumar 2 valos enters.
    param a: valor enter 1
    param b: valor enter 2
    '''
    return a+b

# Programa Principal

try:
    x=int(input("Valor 1: "))
    y=int(input("Valor 2: "))
except ValueError:
    print("Problema")

print(x,"+",y,"=",sumar2(x,y))
