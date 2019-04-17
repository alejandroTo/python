'''hacer un programa que pida dos numeros
y se de cuenta cual de ellos es par,
o si ambos lo son
'''
a = int(input("Ingresa numero A: "))
b = int(input("Ingresa numero B: "))
if(a%2==0 and b%2==0):
	print(f"{a} y {b} son pares")
elif(a%2==0):
	print(f"{a} es par")
elif(b%2==0):
	print(f"{b} es par")
else:
	print(f"{a} y {b} son impares")