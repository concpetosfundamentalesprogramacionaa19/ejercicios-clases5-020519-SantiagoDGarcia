""""
	file: run3.py
	autor: @SantiagoDGarcia

	Deseamos obtener el costo de una carrera universitaria. 
	El valor Promedio de cada ciclo es de 1200$

	El valor Promedio del seguro educativo es 100$ c/u ciclo,
	si la edad es menor igual a 20, caso contrariario sera de 150$
	
	Si el estudiante tiene una modalidad a distancia el numero
	de ciclos a seguir es 10, contrario seran 8 ciclos
	obtener el costo de la carrera de un estudiante


	EJM:
	modalidad: Distancia
	edad = 18 13000
	modadlidad: Presencial <>
	edad = 22


"""
# Se establece las variables principales
valor_ciclo = 1200
modalidad = input ("Ingrese la modalidad del estudiante: Presencial, Distancia \n")
edad = int (input ("Ingrese la edad del estudiante: \n"))
ciclos = int
seguro = int

# Se establece la condicion anidada de la modalidad para determinar la cantidad de ciclos
if (modalidad == "Distancia" or modalidad == "distancia"):
	ciclos = 10
else:
	ciclos = 8
# Se establece el costo a pagar de la cantidad de ciclos por el valor de cada uno
cant_ciclo = ciclos*valor_ciclo # Se establece el costo total de todos los ciclos

# Se establece la condicion anidad acerca de su seguro, referente a su edad
if (edad <= 20):
	seguro = 100*ciclos
else:
	seguro = 150*ciclos
# Se establece la variable final de las sumas
costo_f = cant_ciclo + seguro

print("El costo Total de la carrera es: ", costo_f)



