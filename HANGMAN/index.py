from ntpath import join
from operator import index, le
import os
import random
from smtplib import quotedata
from turtle import clear
from pyparsing import line

leter = []

with open("./palabras.txt","r",encoding="utf-8") as f:
    for line in f:
        line = line.strip("\n") # this removes the jump lines
        leter.append(line)


real_list= []

for i in leter: #aca vamos a pasar los elementos de la lista a string para poder usar el metodo maketrans, y luego pasar el string a lista
    i = str(i)
    letras_convertir = i.maketrans('áéíóú', 'aeiou')
    n_leter = i.translate(letras_convertir)
    n_leter = list(n_leter)
    n_leter = "".join(n_leter)
    real_list.append(n_leter)

numberrandom = random.randint(0,len(real_list) - 1)

PalabraElegida = real_list[numberrandom]

listPalabraElegida = list(PalabraElegida)

word_guion = list("-" * len(PalabraElegida))

def convertirAlista(param1):
    i = 0
    while(i < param1):
        if select_letter == PalabraElegida[i]:
            word_guion[i] = select_letter
            i = i + 1
            continue
        i = i + 1
    os.system("cls")
    print("  ".join(word_guion))
vidas = 10

while(vidas):
    if word_guion == listPalabraElegida:
        print("GANASTE")
        break
    select_letter = str(input("elige una palabra:  "))
    convertirAlista(len(PalabraElegida))
    print(f"te quedan {vidas} vidas")
    vidas -=1
if vidas == 0:
    print(f"La palabra era {leter[numberrandom]}")
