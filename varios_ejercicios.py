# from tkinter import Menu


# cantidad = input("cuantos pesos tienes?  ")
# cantidad = float(cantidad)
# valor_dolar = 114.39
# cantidad_de_dolares = cantidad / valor_dolar
# cantidad_de_dolares = round(cantidad_de_dolares,2)
# print("tienes",cantidad_de_dolares, "dolares") 


# #////

# centavito = input("cuantos dolares tienes?  ")
# centavito = float(centavito)
# valorPeso = 0.0087
# miseria = centavito / valorPeso
# miseria = round(miseria,2)
# print("Tiene $", miseria, "pesos argentinos")

# ////
# memu = """Bienvenido al conversor de monedas

# 1_Pesos Argentinos
# 2_Pesos Colombianos
# 3_Pesos Mexicanos

# Elige una opcion:
# """
# oppcion = int(input(memu))
# if(oppcion == 1):
#     che = input("cuantos pesos Argentinos tienes?  ")
#     che = float(che)
#     valor_dolar = 114.39
#     cantidad_de_dolares = che / valor_dolar
#     cantidad_de_dolares = round(cantidad_de_dolares,2)
#     print("tienes",cantidad_de_dolares, "dolares")
# elif oppcion ==2: 
#     parce = input("cuantos pesos Colombianos tienes?  ")
#     parce = float(parce)
#     valor_dolar = 3732.00
#     cantidad_de_dolares = parce / valor_dolar
#     cantidad_de_dolares = round(cantidad_de_dolares,2)
#     print("tienes",cantidad_de_dolares, "dolares")
# elif oppcion ==3:
#     wey = input("cuantos pesos Mexicanos tienes?  ")
#     wey = float(wey)
#     valor_dolar = 19.88
#     cantidad_de_dolares = wey / valor_dolar
#     cantidad_de_dolares = round(cantidad_de_dolares,2)
#     print("tienes",cantidad_de_dolares, "dolares")
# else:
#     print("no se reconoce la opcion seleccionada")

# def conversore(value_Dolar, country):
#     pesos = input("cuantos pesos " + country +" tienes?  ")
#     pesos = float(pesos)
#     cantidad_de_dolares = pesos / value_Dolar
#     cantidad_de_dolares = round(cantidad_de_dolares,2)
#     print("Tienes $",cantidad_de_dolares, "dolares")

# memu2 = """Bienvenido al conversor de monedas

# 1_Pesos Argentinos
# 2_Pesos Colombianos
# 3_Pesos Mexicanos

# # Elige una opcion:
# """
# opcione = int(input(memu2))

# if opcione == 1:
#     conversore(114, "Argentinos")
# elif opcione == 2:
#     conversore(3732,"Colombianos")
# elif opcione == 3:
#     conversore(20,"Mexicanos")
# else:
#     print("seleccione una opcion correcta, por favor")

# palabrarecibida = str(input("escribe una frase  "))
# palabrarecibida = palabrarecibida.lower()
# palabrarecibida = palabrarecibida.replace(" ", "")

# if(palabrarecibida == palabrarecibida[::-1]):
#     print("Es palindromo")
# else:
#     print("No es palindromo")


# for i in range(0, 1000):
#     result = 2**i
#     print (result)
#     if(result >= 1000000):
#         print("llegamo al milllon")
#         break

#///buena practica hacer esto de abajo
"""
def run(a):
    pass

if __name__ == "__main__":
    run()
"""
#////NO ME FUNCA

# abecedario = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z"
# abecedario = abecedario.replace(" ", "")
# abecedario = abecedario.replace(",", "")
# vocal = "a, e, i, o, u"
# for i in range(0, abecedario):
#     if(i == vocal):
#             print("funciono")
#             continue
#     print(letra)

"""
////numeros primos

numberRecibed=int(input("elige un numero:   "))


def esPrimo (parametro):
    verificador = 0
    i = 2
    while( i < parametro):
        if parametro % i ==0:
            verificador+=1
        i+=1
    if verificador == 0:
        return True
    else:
        return False


if esPrimo(numberRecibed) == True:
    print("Es primo")
else:
    print("NO Es primo")

//////////

numero = int(input("elige un numero:   "))

numero2= numero-1
def primalidad (parametro ):
    if parametro == 0 or parametro == 1:
        return 1
    return parametro  * primalidad(parametro - 1)
#   
#   7 * 720 
#   6 * 120 
#   5 * 20 
#   4 * 5 
#   3 * 2 
#   2 * 1  

valor = primalidad(numero2)
print(valor)
if (valor + 1) % numero == 0:
    print("es primo")
else:
    print("No lo es")
"""
#/////////


import random

# def buscando_el_nro(num, meta):
#     if (num < meta):
#         print("busca un numero mas alto")
#     elif(num > meta):
#         print("busca un numero mas bajo") qXm+*-6e54z||   ,


# numero_adivinar = random.randint(1,100)
# numero_elegido = int(input("Elige un numero del 1 al 100 "))


# while(numero_elegido != numero_adivinar):
#     buscando_el_nro(numero_elegido,numero_adivinar)
#     numero_elegido = int(input("Elige otro numero "))


# if(numero_elegido == numero_adivinar):
#     print("GANASTE")

print(round(10.3456, 2))

hola = "nuncameatraparan" * 2
print(hola)

number = 10 / 2 + 5 * 7
print(number)