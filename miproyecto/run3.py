""""
	file: run3.py
	autor: @SantiagoDGarcia

	nota mayor o igual a 18: sobresaliente

	nota mayor o igual a 16 y menor a 18: muy buena

	nota mayor o igual a 13 y menor a 16: buena
"""

from misvariables import *

# Uso de condicional doble

nota = int (input ("Ingrese nota 1: "))


if nota >= 18:
	print ("Usted esta aprobado (SOBRESALIENTE) con %d" % (nota))
else:
	if (nota >= 16) and (nota < 18):
		print ("Usted esta aprobado (MUY BUENA) con %d" % (nota))
	else:
		if (nota >= 13) and (nota < 16):
			print ("Usted esta aprobado (BUENA) con %d" % (nota))
		else:
			print ("%s con %d" % (mensaje2, nota))

