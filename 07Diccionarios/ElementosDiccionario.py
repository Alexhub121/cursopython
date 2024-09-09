diccionario = {'Nombre' : "Alex" , 'Apellido' : "Barrientos" , 'Estatura' : 190}

print(diccionario.keys()) #Muestra solo las claves o llaves
print(diccionario.values()) #Muestra solo los valores

print(diccionario['Estatura']) #Muestra el valor de una llave en especifico


diccionario['Peso'] = "70 kilogramos" #si despues pones esto agrega la nueva clave y su valor
print(diccionario)

calveNew = input("Ingresa una nueva clave:")
valorNew = input("Ingresa un nuevo valor:")


diccionario[calveNew] = valorNew #si despues pones esto agrega la nueva clave y su valor
print(diccionario)

diccionario['Estatura'] = 180 #si seleccionas uno ya existente sirve para modificarlo
print(diccionario)