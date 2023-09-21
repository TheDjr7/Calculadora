from math import *
print('Calculadora Malandra' '\n===========================')

def suma(a, b):
    return(a+b)


def resta(a, b):
    return(a-b)


def multiplicacion(a, b):
    return(a*b)


def division(a, b):
    return(a/b)

while True:
     try: 
         operacion = int(input('Seleccione la operacion' 
                               '\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n '))
         if (operacion <=4 and operacion > 0):
            break
    
     except:
        print('Ingrese un numero entero valido')


num1 = float(input('Ingrese el primer numero: '))
num2 =float(input('Ingrese el segundo numero: '))

if  operacion == 1:
    resultado=suma(num1, num2)
elif operacion== 2:
    resultado=resta(num1, num2)
elif operacion ==3:
    resultado = multiplicacion(num1,num2)
elif operacion ==4:
    resultado = division(num1,num2)

print(resultado)