lista = ["lunes","Martes","Miercoles","Jueves","Viernes"]
#acceso al último elemento de la lista
print(lista[len(lista)-1])
#imprimir desde 0 hasta el indice 2 
#desde el cero hasta n-1 igual a indice 2
print(lista[0:3]) 
#desde el dos a el final
print(lista[2:])
#agregar un valor a la lista a el final
lista.append(1)
#insrta un valor en la lista donde quieras
#en el indice dos, voy a guardar el valor de 3
lista.insert(2,3)
print(lista[:])
#agreagr varios elementos de golpe...los agreaga al final
lista.extend([7,8,4])
print(lista[:])
#conactenar dos listas
lista2 = [2,4,5,6,2,2,2,2]
lista3 = lista+lista2
print(lista3)
#saber si un valor esta en la lista
print(2 in lista2)
#saber en que indice de la lista esta
print(lista2.index(5))
#saber cunatas veces se encueuntra un elemento en la lista
print("numero de las veces que se ecuentra el numero 2: ",lista2.count(2))
#eliminar un elemento en la lista
lista2.pop()
lista2.pop(2)#eliminar el valor del indice 2
print(lista2)
lista2.remove(2)#rem el valor 2 de la lista. el primero que encuentre
print(lista2)
#lista2.clear()#eliminar toda la lista
print(lista2)
#volter la lista de reversa
lista2.reverse()
print(lista2)
lista4 = [23,4,-1,44]
#ordenar una lista ascendenetemte
lista4.sort()
print(lista4)
#ordenar una lista descenentemente
lista4.sort(reverse=True)
print(lista4)

