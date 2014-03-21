n = 33
z = 0
while n < 127:
    if z / 7 != 1:
        print chr(n),
        n = n + 1
        z = z + 1
    if z / 7 == 1:
        print chr(n)
        n = n + 1
        z = 0
print "\n""\n" "FIN DEL PROGRAMA"
