#sintaxis
#for variable in elemento a recorrer:
	#cuerpo del bucle(con identacion o separacion)
	#pass   . para terminar el ciclo
edad = int(input("Ingresa edad del alumno "))
noAlu = int(input("Ingresa matricula del alumno "))
size = int(input("Ingresa numero de calificaiones a capturar "))
calif = []
for i in range(size):
	cal = input("ingresa calif")
	calif.append(cal)
pass
print(calif[0])