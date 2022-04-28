from multiprocessing.sharedctypes import Value
from statistics import multimode


lista_de_diccionarios=[
    {"firstname": "rodrigo","lastName":"gutierrez"},
    {"firstname": "yolanda","lastName":"gutierrez"},
    {"firstname": "yaqueline","lastName":"gutierrez"},
    {"firstname": "maximiliano","lastName":"pachao"},
]

for value in lista_de_diccionarios:
    for key,ida in value.items():
        print(key, "-" ,ida)

#///////
numemeros_al_cuadrado = []
i = 1
while(i < 101):
    valor_multiplicado = i ** 2
    i = i + 1 
    if (valor_multiplicado % 3 == 0):
        continue
    numemeros_al_cuadrado.append(valor_multiplicado)
    

print(numemeros_al_cuadrado)

#Codigo anterior con una sola linea

list_compresions = [i**2 for i in range(1,101) if i %3 != 0]

print("list compresions",list_compresions)

#imprimir en una lista todo los nuemeros de hasta 5 digitos si son multiplo de 4 de 6 y 9

multiplos = [j for j in range(1,99999) if j % 36 == 0]
print(multiplos)

#imprimir en un diccionario los numeros del 1 al 100 y en los value su key elevado al cuadrado

my_dicc = {}

for i in range(1,101):
    if not(i % 3 == 0):
        my_dicc[i] = i**2 
print(my_dicc)

#el paso anterior en una sola linea con
#list comprehension
print("#list comprehension")
mi_dicc2 = {i: i**2 for i in range(1,101) if i % 3 != 0}
mi_dicc2[100] = "manipulando dicionarios"
print(mi_dicc2)

#dic comprehension cuyas llaves son del 1 hasta el 1000 y los valores son las raices cuadradas de las llaves
print("raiz ")
dic_comprehension_raiz={ i: round(i**0.5,2) for i in range(1,1001) if type(i) ==int}
print(dic_comprehension_raiz)

#
data = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    }
]