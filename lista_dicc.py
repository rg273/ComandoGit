from cgi import print_arguments
from concurrent.futures.thread import _worker
from multiprocessing.sharedctypes import Value
from statistics import multimode
import string


# lista_de_diccionarios=[
#     {"firstname": "rodrigo","lastName":"gutierrez"},
#     {"firstname": "yolanda","lastName":"gutierrez"},
#     {"firstname": "yaqueline","lastName":"gutierrez"},
#     {"firstname": "maximiliano","lastName":"pachao"},
# ]

# for value in lista_de_diccionarios:
#     for key,ida in value.items():
#         print(key, "-" ,ida)

# #///////
# numemeros_al_cuadrado = []
# i = 1
# while(i < 101):
#     valor_multiplicado = i ** 2
#     i = i + 1 
#     if (valor_multiplicado % 3 == 0):
#         continue
#     numemeros_al_cuadrado.append(valor_multiplicado)
    

# print(numemeros_al_cuadrado)

# #Codigo anterior con una sola linea

# list_compresions = [i**2 for i in range(1,101) if i %3 != 0]

# print("list compresions",list_compresions)

# #imprimir en una lista todo los nuemeros de hasta 5 digitos si son multiplo de 4 de 6 y 9

# multiplos = [j for j in range(1,99999) if j % 36 == 0]
# print(multiplos)

# #imprimir en un diccionario los numeros del 1 al 100 y en los value su key elevado al cuadrado

# my_dicc = {}

# for i in range(1,101):
#     if not(i % 3 == 0):
#         my_dicc[i] = i**2 
# print(my_dicc)

# #el paso anterior en una sola linea con
# #list comprehension
# print("#list comprehension")
# mi_dicc2 = {i: i**2 for i in range(1,101) if i % 3 != 0}
# mi_dicc2[100] = "manipulando dicionarios"
# print(mi_dicc2)

# #dic comprehension cuyas llaves son del 1 hasta el 1000 y los valores son las raices cuadradas de las llaves
# print("raiz ")
# dic_comprehension_raiz={ i: round(i**0.5,2) for i in range(1,1001) if type(i) ==int}
# print(dic_comprehension_raiz)

# #Filtrando datos
# DATA = [
#     {
#         'name': 'Facundo',
#         'age': 72,
#         'organization': 'Platzi',
#         'position': 'Technical Coach',
#         'language': 'python',
#     },
#     {
#         'name': 'Luisana',
#         'age': 33,
#         'organization': 'Globant',
#         'position': 'UX Designer',
#         'language': 'javascript',
#     },
#     {
#         'name': 'Héctor',
#         'age': 19,
#         'organization': 'Platzi',
#         'position': 'Associate',
#         'language': 'ruby',
#     },
#     {
#         'name': 'Gabriel',
#         'age': 20,
#         'organization': 'Platzi',
#         'position': 'Associate',
#         'language': 'javascript',
#     },
#     {
#         'name': 'Isabella',
#         'age': 30,
#         'organization': 'Platzi',
#         'position': 'QA Manager',
#         'language': 'java',
#     },
#     {
#         'name': 'Karo',
#         'age': 23,
#         'organization': 'Everis',
#         'position': 'Backend Developer',
#         'language': 'python',
#     },
#     {
#         'name': 'Ariel',
#         'age': 32,
#         'organization': 'Rappi',
#         'position': 'Support',
#         'language': '',
#     },
#     {
#         'name': 'Juan',
#         'age': 17,
#         'organization': '',
#         'position': 'Student',
#         'language': 'go',
#     },
#     {
#         'name': 'Pablo',
#         'age': 32,
#         'organization': 'Master',
#         'position': 'Human Resources Manager',
#         'language': 'python',
#     },
#     {
#         'name': 'Lorena',
#         'age': 56,
#         'organization': 'Python Organization',
#         'position': 'Language Maker',
#         'language': 'python',
#     },
# ]



# list_compresions_python = [worker["name"] for worker in DATA if worker["language"] == "python"]
# print(list_compresions_python,"esta es")
# #the same but whit filter

# let = list(filter(lambda x:x["language"]== "python" ,DATA))
# let2 = list(map(lambda x: x["name"] ,let))
# print(let2, "esta es2")



# #exercise 2, the same as the previouse one
# list_compresions_organization = [i["name"] for i in DATA if i["organization"] == "Platzi"]
# print(list_compresions_organization,"exercise 1 whit list compresions")
# #exercise 2, with filter and map
# list_organization_filter = list(filter(lambda x: x["organization"] == "Platzi",DATA))
# print(list_organization_filter,"ola")
# list_organization_map = list(map(lambda i: i["name"],list_organization_filter))
# print(list_organization_map)

# list_organization_whitout_map = []
# for i in list_organization_filter:
#     for j,k in i.items():
#         if j == "name":
#             list_organization_whitout_map.append(k)


# print(list_organization_whitout_map,"funca?")




# #this return the complete dic
# list_filter_old_people = list(filter(lambda worker: worker["age"] > 18,DATA))

# #we want only the names of those who are older than 18
# list_filter_old_people_only_names = list(map(lambda worker: worker["name"], list_filter_old_people))
# print(list_filter_old_people_only_names)

# #using pip operator
# list_agg_if_they_are_older_70 = list(map(lambda worker: worker | {"old":worker["age"] > 70}, DATA))
# print(list_agg_if_they_are_older_70)



#error handling

# def divisores():
#     div = []
#     num = int(input("ingresa un nro:  "))
#     try:
#         if num < 0:
#             raise ValueError("No se puede ingresar valores negativos")
#     except ValueError as letve:
#         print(letve)
#         return False
#     else:
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 div.append(i)
#     print(div)

# divisores()

#assert statment

def divisores2():
    div2 = []
    num2 = input("ingresa un nro:  ")
    
    assert num2.isnumeric(), "No se puede ingresar un string"    
    
    num2 = int(num2)
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            div2.append(i)
    print(div2)

divisores2()



