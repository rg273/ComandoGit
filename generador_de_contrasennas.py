import random
from traceback import print_tb #HERRAMIENTA MISTERIOSA QUE NOS SERVIRA MAS TARDE

def run():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    def generador_contrasenna(digitos):
        i = 0
        new_contrasenna = []
        
        while (i < digitos):
            selector_de_tipo_caracter = random.randint(0,200)
            if selector_de_tipo_caracter <= 50:
                elegir_caracter = random.randint(0, len(MAYUS) -1)
                new_contrasenna.append(MAYUS[elegir_caracter])
            elif selector_de_tipo_caracter <= 100:
                elegir_caracter = random.randint(0, len(MINUS) -1)
                new_contrasenna.append(MINUS[elegir_caracter])
            elif selector_de_tipo_caracter <= 150:
                elegir_caracter = random.randint(0, len(NUMS) -1)
                new_contrasenna.append(NUMS[elegir_caracter])
            elif selector_de_tipo_caracter <= 200:
                elegir_caracter = random.randint(0, len(CHARS) -1)
                new_contrasenna.append(CHARS[elegir_caracter])
            i = i + 1
        
        new_contrasenna = "".join(new_contrasenna)
        
        return print("Tu nueva contraseña es", new_contrasenna)
    generador_contrasenna(18)

    #/////////////////
    lista_prueba5 = [5,10,15]
    lista_prueba2 = [2,4,8]
    sum = lista_prueba5[1] + lista_prueba2[1]
    print(sum)
    #/////////////////
    #ingresar a filas columnas
    matriz =([[1,2,3],
    [4,5,6],[7,8,9]])
    print(matriz)
    print(matriz[0][2])
    #en numpy = matriz[0,2]

    #/////////////////
    array = ([1,2,3,4,5,6,7,8,9])
    print(type(array))
    print(array[0:3])








if __name__ =="__main__":
    run()