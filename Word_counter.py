
import os.path

def contar_palabras (x):
    return len(x.split(" "))

if not os.path.isfile('Phrases.txt'):
    Archivo = open("Phrases.txt","w")
    Archivo.close

Archivo = open("Phrases.txt","r")
Lineas = 0
Palabras = 0
linea = Archivo.readline()
while linea:
    Palabras = Palabras + contar_palabras(linea)
    Lineas = Lineas + 1
    linea = Archivo.readline()

print("Habia ",Palabras," Palabras en ", Lineas, " frases previamente"  )
Archivo.close

UnaFrase = ""
while UnaFrase != "end" :
    UnaFrase = input ("Ingrese una frase:  ")
    if UnaFrase != "end":
        UnaPalabra = contar_palabras(UnaFrase)
        Palabras = Palabras + UnaPalabra
        print("La frase ingresada tiene ", UnaPalabra," Palabras")
        Archivo = open("Phrases.txt","a")
        Archivo.writelines(UnaFrase + "\n")
        Archivo.close
