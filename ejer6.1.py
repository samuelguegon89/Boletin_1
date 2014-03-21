numero = int(raw_input("Dame un numero: "))

while numero < 0 or numero > 9:
	print("Dame un numero entre el 0 y el 9")
	numero = int(raw_input("Dame otro numero: "))
	if numero < 0:
		print "numero demasiado bajo"
	elif numero > 9:
		print "numero demasiado alto"		
for i in range(11):
	resultado=i*numero
	print i,"X",numero,"=",resultado
	i=i+1
	
print "La tabla de multiplicar del",numero,"esta terminada"
