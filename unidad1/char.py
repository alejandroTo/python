#comprobar si una letra es vocal
vocal = input("Ingresa vocal: ").lower()
if(vocal=='a' or vocal=='e' or vocal=='i' or vocal=='o'or vocal=='u'):
	print(f"<{vocal}> si es una vocal")
else:
	print(f"<{vocal}> no es una vocal")