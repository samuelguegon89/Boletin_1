uss="pepe"
paswd=1234

for i in range(3):	
	usuario= getpass.getpass(prompt="Introduzca usuario: ")
	contra= getpass.getpass(prompt="Introduzca password: ")

	if usuario == uss and contra == paswd:
		print "El usuario y la passwd es correcto"
		break	
	else:
		print"El usuario y la passwd es incorrecta"

		if i<2:
			print "Vuelve a introducir usuario y passwd" 
	
