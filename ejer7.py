numero=int(raw_input("Introduce el numero del DNI sin la letra: "))
resto=numero%23
l=["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

print "\n""La letra es:",l[resto]
