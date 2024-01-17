import os
os.system("cls")

# ****************************************************************

def suma (a,b):
    c = a + b
    print("La suma de a + b es: ",c)

# suma(2,3)

def resta (a,b):
    c = a - b
    print("La resta de a - b es: ",c)
# resta(2,3)

      
def multiplicacion (a,b):
    c = a * b
    print("La multiplicación  de a * b es: ",c)
    
# multiplicacion(2,3)

def division (a,b):
    if b == 0:
        print("La división no se puede realizar")
    else:
        c = a/b
        print("La división de a / b es: ",c)
division(2,4)
    