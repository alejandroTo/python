#convertir un numero a binario
#los primeros dos caracteres indican que tipo de dato es
a = 10
print(bin(a))
#convertir un numero a hexadecimal
#los primeros dos caracteres indican que tipo de dato es
print(hex(a))
#convertir de binario a base 10 o normal
#en el primeros dos caracteres va el tipo a convertir
#en la segunda va al base en la que estamos convirtiendo
print(int("0b1010",2))
#convertir de hexadecimal a base 10 o normal
print("Conversion de hexadecimal a base normal",int("0xb",16))

#saber la longitud de una cadena
nombre = "jose"
print(f"hello {nombre} your name have {len(nombre)} characters")
