'''Cajero automatico 
   que empiece con un valor de $1000
   1. Ingresa dinero a la cuenta
   2. Retirar dinero a la cuenta
   3. Mostrar el dinero dispobile
   4. Salir
'''
saldo = 1000
while True:
	print("\t.:Menu:.")
	print("1. Ingresa dinero a la cuenta")
	print("2. Retirar dinero a la cuenta")
	print("3. Mostrar el dinero dispobile")
	print("4. Salir")
	print()
	opc = int(input("Digite una opcion: "))
	if (opc==4):
		break
	elif(opc==1):
		abono = int(input("Ingresa abono a la cuenta: "))
		saldo+=abono
	elif(opc==2):
		retiro = int(input("Ingresa retiro a la cuenta"))
		if(retiro>saldo):
			print("Retio imposible<Saldo insificiente>")
		else:
			saldo-=retiro
	elif(opc==3):
		print(f"Tu saldo total es: {saldo}")
	else:
		print("opcion no valida")



		
    