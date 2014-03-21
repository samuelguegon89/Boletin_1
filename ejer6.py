numero = 10

while numero < 0 or numero > 9:
	print("Dame un numero entre el 0 y el 9")
	numero = int(raw_input("Dame un numero: "))
	if numero < 0:
		print "numero demasiado bajo"
	elif numero > 9:
		print "numero demasiado alto"
	else:
		for i in range(11):	
			resultado=i*numero
			print i,"X",numero,"=",resultado
			i=i+1
	print "La tabla de multiplicar del",numero,"esta terminada"
	respuesta = str(raw_input("Otra vez? "))
	if respuesta == "si":
		numero = 10
	elif respuesta == "no":
		exit()
	





		
	
