from numpy import genfromtxt, savetxt
import csv
import operator

archivo = open("pg100.txt","r")

diccionario = {}
for linea in archivo:
	for palabra in linea.split():
		diccionario[palabra] = diccionario.get(palabra,0) + 1
archivo.close()
lista = diccionario.items()
lista.sort(key=lambda x:x[1], reverse=True)

listaPalabrasFrecuentes =  [x[0] for x in lista[:158]]

dictPalabras = {}

rangos = []
rangos = range(9) + range(11,13) + range(14,32) + range(127,256)
rangos = map(lambda a: chr(a), rangos)

for indice, palabra in enumerate(listaPalabrasFrecuentes):
	dictPalabras[palabra] = rangos[indice]

lista = dictPalabras.items()
lista.sort(key=lambda x:x[1])
string = "0".join(x[0] for x in lista)
string += "00"
archEnconde = open("pg100Enconde.txt","w")
archEnconde.write(string)

archivo = open("pg100.txt","r")
lineasEncode = []
stringArch=''
for linea in archivo:
	lineaa = linea.split()
	for palabra in lineaa:
		if palabra in dictPalabras.keys():
			stringArch+=dictPalabras[palabra]
		else:
			stringArch+=palabra
		stringArch += " "
	stringArch.rstrip(" ") 
	archEnconde.write(stringArch)
	archEnconde.write("\n")
	stringArch=''
archEnconde.close()

