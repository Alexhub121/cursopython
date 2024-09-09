'''NO SE REPITEN LAS CLAVES/KEYS'''

diccionario = {1 : 2 , 2 : 3, 3 : 4}
print(diccionario)


diccionario.pop(3) #Sirve para eliminar una clave con su valor
print(diccionario)

diccionario.popitem() #Sirve para eliminar el último elemento agregado
print(diccionario)

diccionario.clear() #Sirve para eliminar todos los elementos del diccionario
print(diccionario)


diccionario = {1 : 2 , 2 : 3, 3 : 4}
diccionario.setdefault(4, 5) #resive valor de la calve y su valor 
print(diccionario)


diccionario = {1 : 2 , 2 : 3, 3 : 4}
diccionario2 = {4 : 5, 6 : 7, 8 : 9}
diccionario.update(diccionario2) #sirve para actualizar el diccionario
print(diccionario)