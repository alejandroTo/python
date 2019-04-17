#programa para saber la edad de un sujeto...

edad = 0
nombre = ""
nombre = input("ingresa nombre: ")
edad = int(input("Ingresa edad: "))

if edad>=18:
	print(nombre+" :eres mayor de edad")
elif edad >=10 and edad <=17:
	print(nombre +" :eres adolescente")
else:
	print(nombre +" :eres un niño")
pass