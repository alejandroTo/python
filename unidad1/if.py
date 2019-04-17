#crea un programa que compare dos numeros
#y diga cual es el mayor de los dos
a = 0
b = 0
a = int(input("Ingresa numrero A "))
b = int(input("Ingresa numero B "))
if(a>b):
	print("El numero mayor es: ",a)
elif a==b:
	print("Los dos numeros son iguales")
else:
	print("El numero mayor es: ",b)
