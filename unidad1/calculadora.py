'''construir una caculadora que contenga 
las operaciones basicas(suma,resta,multipicacion,division)
.El usuario debe de especificar la operacion con el primer caracter 
del nombre de la operacion...
* S, s-suma
* R, r-resta
* P,p,M,m-multiplicacion
* D,d-division
'''
a = float(input("Ingresa numero a: "))
b = float(input("Ingresa numero b: "))
operacion = input("Ingresa operacion: ").lower()
if(operacion == 's'):
	print(f"la suma de {a} y {b} es: ",a+b)
elif(operacion =='r'):
	print(f"la resta de {a} y {b} es: ",a-b)
elif(operacion =='p'or operacion == 'm '):
	print(f"la multiplicacion de {a} y {b} es: ",a*b)
elif(operacion =='d'):
	print(f"la division de {a} y {b} es: ",a/b)
else:
	print("No ingreso una opción correcta")

