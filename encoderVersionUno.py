def encoderVersionUno(nombreArchivo):
	
	print "Comprimiendo archivo: {}...".format(nombreArchivo)

	archivo = open("{name}".format(name=nombreArchivo),"r")

	diccionario = {}
	for linea in archivo:
		for palabra in linea.split():
			diccionario[palabra] = diccionario.get(palabra,0) + 1

	archivo.close()
	
	for clave in diccionario.keys():
		diccionario[clave] = diccionario[clave]*len(clave)

	lista = diccionario.items()
	lista.sort(key=lambda x:x[1], reverse=True)

	listaPalabrasFrecuentes =  [x[0] for x in lista[:157]]

	dictPalabras = {}

	rangos = []
	rangos = range(1,9) + range(11,13) + range(14,32) + range(127,256)
	rangos = map(lambda a: chr(a), rangos)

	for indice, palabra in enumerate(listaPalabrasFrecuentes):
		dictPalabras[palabra] = rangos[indice]

	lista = dictPalabras.items()
	lista.sort(key=lambda x:x[1])
	string = chr(0).join(x[0] for x in lista)
	string += chr(0)+chr(0)
	archEnconde = open("EncodeV1{name}".format(name=nombreArchivo),"w")
	archEnconde.write(string)
	archEnconde.write("\n")

	archivo = open("{name}".format(name=nombreArchivo),"r")
	lineasEncode = []
	for linea in archivo:	
		copia=""
		for char in linea:
			if (char in rangos) or (char==chr(0)):
				copia+=chr(0)+char
			else:
				copia+=char
		stringArch = copia
		lineaa = copia.split()
		for palabra in lineaa:
			if palabra in dictPalabras.keys():
				stringArch = stringArch.replace(palabra,dictPalabras[palabra])
		archEnconde.write(stringArch)
	archEnconde.close()
	