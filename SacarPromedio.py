#declaracion de variables
nombre = ""
size = 0
matricula = 0
calif = []
nombre = input("Ingresa nombre del alumno ")
matricula = int(input("Ingresa matricula del alumno "))
promedio = 0
size = int(input("Ingresa numero de calif a capturar "))
for i in range(size):
	cal = int(input("Ingresa Calificaion: "))
	calif.append(cal)
	promedio = promedio + cal
	pass
if (promedio/size)<7:
	print("El alumno ["+ nombre+ "] esta: Reprobado")
	print(calif)
	pass
else:
	print("Aprobado")
	print(calif)
	pass