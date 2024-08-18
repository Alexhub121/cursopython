conjunto = {1, 2, 3, 4, 5} #No permite datos repetidos 
lista = [1, 1, 2, 3, 4, 4] #Permite datos repetidos

conjunto.add(20) #sirve para agregar nuevo elemento
print(conjunto)

conjunto.remove(1) #Eliminar un valor (remove/discard)
print(conjunto)

conjunto.pop() #En conjuntos toma cualquier valor y lo elimina
print(conjunto)

conjunto.update([1, 2, 3]) #Agrega elementos literables
print(conjunto)

conjunto.clear() #deja el conjunto vacio 
print(conjunto)