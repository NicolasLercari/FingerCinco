# FingerCinco

Ejemplo:

python fingerCinco.py "nombreDelArchivo".txt

esto nos genera un Encode"nombreDelArchivo".txt y un Decode"nombreDelArchivo".txt.
El primero es el archivo comprimido y el segundo el descomprimido.

Se puede verificar que el archivo original y el descomprimido son iguales con "diff".

diff "nombreDelArchivo".txt Decode"nombreDelArchivo".txt
