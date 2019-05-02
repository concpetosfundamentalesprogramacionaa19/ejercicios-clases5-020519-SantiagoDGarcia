""""
	file: run2.py
	autor: @SantiagoDGarcia
"""

from misvariables import *

# Uso de condicional doble

nota = input ("Ingrese nota 1: ")
nota2 = input ("Ingrese nota 2: ")

nota = int (nota)
nota2 = int (nota2)


if nota >= 18:
	print ("%s con %d" % (mensaje, nota))
else:
	print ("%s con %d" % (mensaje2, nota))


if nota2 >= 18:
	print ("%s con %d" % (mensaje, nota2))
else:
	print ("%s con %d" % (mensaje2, nota2))