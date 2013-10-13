a = int(input("Nombre a ? "))
b = int(input("Nombre b ? "))

if a % b == 0:
    print ("Le nombre a=" + str(a) + " est un multiple du nombre b=" + str(b))
else:
    print ("Le nombre a=" + str(a) + " n'est pas un multiple du nombre b=" + str(b))