mayor = 0
menor = 99999999
for i in [2,4,1]:
	if(i>mayor):
		mayor = i
	if(i<menor):
		menor = i
pass
print(f"el numero mayor es: {mayor} y el numero menor es {menor}")
