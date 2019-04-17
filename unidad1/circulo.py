import math

radio = float(input("Ingresa radio del circulo: "))
area =math.pi*(radio**2)
circunferencia = 2*math.pi*radio
print(f"El area del circulo es: {area:.3f}")
print(f"La circunferencia del circulo es: {circunferencia:.3f}")