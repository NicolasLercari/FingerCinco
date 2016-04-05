def decoder(nombreArchivo):

	print "Descomprimiendo archivo: {}...".format(nombreArchivo)

	archivo = open("Encode{name}".format(name=nombreArchivo),"r")
	archDecoder = open("Decode{name}".format(name=nombreArchivo),"w")

	rangos = []
	rangos = range(1,9) + range(11,13) + range(14,32) + range(127,256)
	rangos = map(lambda a: chr(a), rangos)

	linea = archivo.readline()
	linea = linea.rstrip("\n")
	listaDic = linea.split(chr(0))
	listaDic.pop()
	listaDic.pop()
	dicc = {}
	for indice, palabra in enumerate(listaDic):
		dicc[rangos[indice]]=palabra

	for linea in archivo:
		i=0
		copia=""
		while (i < len(linea)):
			if linea[i]==chr(0): 
				copia+=linea[i+1]
				i+=2
				continue
			if linea[i] in dicc.keys():
				copia += dicc[linea[i]]
			else:
				copia+=linea[i]
			i+=1			
		copia2=""
		for char in copia:
			if char!=chr(0): 
				copia2+=char
		archDecoder.write(copia2)
	archDecoder.close()
	archivo.close()
