def saludo(): #Se programa el saludo al ususario 
    while True:
        try:
            nombre = input("Ingresa tu nombre:") #Usuario ingresa nombre
            if nombre.isalpha() and len(nombre) >= 3: #Aqui se valida que el nombre sean solo letras y sea mayor a tres caracteres
                print(f"Hola {nombre}, bienvenido a mi programa") #saluda al usuario despues de validar su nombre
                break #Termina el while
            else:
                print("El nombre debe ser alfanumerico y tener al menos 3 caracteres") #Esto se imprime si el nombre cumple las reglas
                continue #regresa desde el principio del while
        except : #Si hay un error reinicia el codigo
            print("Error, por favor ingresa un nombre")
            continue #Reinicia el codigo


def pedido(): #Se programa el pedido
    while True:

        menu = "cafe", "Leche" #Menu del negocio
        lista = [] #Aqui se agregara lo que el cliente agregue
        pedir = input("Deseas Ordenar? (s/n):") #se pregunta si desea ordenar
        if pedir == "s": #Inicia proceso de pedido 
            print(f"\nMenu de opciones:{menu}")   #Imprime el menu 
            opcion = str(input("Ingresa tu opcion: (Cantidad y Producto)")).title() #Ingresa lo que quiere el usuario
            lista.append(opcion) #Se agrega lo ingresado a la lista
            pedir2 = input("Deseas Ordenar mas? (s/n):") #Se le pregunta de nuevo si quiere ordenar
            if pedir2 == "s": #Inicia proceso de pedido 
                print(f"\nMenu de opciones:{menu}") #Imprime el menu 
                opcion2 = str(input("Ingresa tu opcion: (producto y cantidad)")).title() #Ingresa lo que quiere el usuario
                lista.append(opcion2) #Se agrega lo ingresado a la lista
                print(f"Tu pedido actual es{lista}") #se muestra al usuario su pedido 
                break #Termina el while
            elif pedir2 == "n": #Se cancela el proceso de pedido la segunda vez que se pregunta
                print(f"Tu pedido actual es{lista}") #se muestra al usuario su pedido 
                break #Termina el while
                
        elif pedir == "n": #Se cancela el proceso de pedido la primera vez que pregunta
            print("Gracias por visitar") #Despide al usuario
            break #aqui termina el while

saludo() #llama a la funcion SALUDO
pedido() #Llama a la funcion PEDIDO 