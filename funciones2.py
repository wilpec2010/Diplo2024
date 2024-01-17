import os
os.system("cls")

def multiplicacion (a, b):
    c = a * b
    print(" El resultado es: ",c)
multiplicacion(40,4)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def multi (a,b):
    return 10
x = multi(4,2) + 6
print("El valor retornado de la función es: ",x)
print("Soy un String: ",(str(multi(5,6))))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def triangulo(base, altura):
    area = (base * altura)/2
    return area
base = int(input("Ingrese el valor de la base: "))
altura = int(input("Ingrese el valor de la altura: "))
print(" el area del triángulo es: ", triangulo(base,altura))

def mayor_Valor(valor1,valor2):
    if valor1 > valor2:
        mayor = valor1
    else:
        mayor = valor2
    return 12
v1 = int(input("Ingrese el primer valo: "))
v2 = int(input("Ingrese el segundo valor: "))
print(" el valor mayor es: ", mayor_Valor(v1,v2))