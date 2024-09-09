def entero():
    print("este es un dato entero:")
    return 10 #Sirve para retornar valores

def decimal():
    print("este es un dato decimal:")
    return 90.99

def asignacion():
    return 1, 2, 3, 4, 5 #Sirve para asignar a variables

print(entero()) #Es necesario mandar llamar def con el print para que return se imprima
print(decimal())#Es necesario mandar llamar def con el print para que return se imprima

a, b, c, d, e = asignacion() #El return ordena los datos de la funcion en las variables
print(a)
print(b)
print(c)
print(d)
print(e)