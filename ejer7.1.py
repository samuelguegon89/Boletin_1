letra_dni= "TRWAGMYFPDXBNJZSQVHLCKE"

dni= raw_input("Introduce el DNI con la letra incluido: ")
numeros= int(dni[:-1])
letra= str(dni[-1])
resto = numeros%23

if letra_dni[resto] == dni[-1].upper():
	print "El DNI ES CORRECTO"

else:
	print "El DNI ES INCORRECTO"
