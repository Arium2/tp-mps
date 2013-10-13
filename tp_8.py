import time

nbr = int(input("Choisissez un nombre "))
millisStart = int(round(time.time() * 1000))
i = 1

while i <= nbr:
	if nbr % i == 0:
		print (i)
	i += 1

millisEnd = int(round(time.time() * 1000))

print ("Fait en " + str(millisEnd - millisStart) + "ms.")