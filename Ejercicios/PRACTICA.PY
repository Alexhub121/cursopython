import datetime

def saludo(): #Se programa el saludo al ususario 
    while True:
        print("Bienvenido a la Cafeteria 'CafeAstetic' ")
        print("--------------------------")
        try:
            now = datetime.datetime.now()
            nombre = input("Ingresa tu nombre:") #Usuario ingresa nombre
            if nombre.isalpha() and len(nombre) >= 3: #Aqui se valida que el nombre sean solo letras y sea mayor a tres caractere
                print(f"Hola {nombre}, hoy es {now.strftime('%d/%m/%Y')}")
                break
            else:
                print("El nombre debe ser alfanumerico y tener al menos 3 caracteres") #Esto se imprime si el nombre cumple las reglas
                continue #regresa desde el principio del while
        except : #Si hay un error reinicia el codigo
            print("Error, por favor ingresa un nombre")
            continue #Reinicia el codigo


def pedido(): #Se programa el pedido
    while True:

        menu = "cafe", "Leche", "Frappe", "Pan", "Agua" #Menu del negocio
        lista = [] #Aqui se agregara lo que el cliente agregue
        pedir = input("Deseas Ordenar? (s/n):") #se pregunta si desea ordenar
        if pedir == "s": #Inicia proceso de pedido 
            print(f"\nMenu de opciones:{menu}")   #Imprime el menu 
            opcion = str(input("Ingresa tu opcion: (Cantidad y Producto)")).title() #Ingresa lo que quiere el usuario
            lista.append(opcion) #Se agrega lo ingresado a la lista
            pedir2 = input("Deseas Ordenar mas? (s/n):") #Se le pregunta de nuevo si quiere ordenar
            if pedir2 == "s": #Inicia proceso de pedido 
                print(f"\nMenu de opciones:{menu}") #Imprime el menu 
                opcion2 = str(input("Ingresa tu opcion: (producto y cantidad):")).title() #Ingresa lo que quiere el usuario
                lista.append(opcion2) #Se agrega lo ingresado a la lista
                print(f"Tu pedido actual es{lista}") #se muestra al usuario su pedido 
                break #Termina el while
            elif pedir2 == "n": #Se cancela el proceso de pedido la segunda vez que se pregunta
                print(f"Tu pedido actual es{lista}") #se muestra al usuario su pedido 
                break #Termina el while
                
        elif pedir == "n": #Se cancela el proceso de pedido la primera vez que pregunta
            print("Gracias por visitar") #Despide al usuario
            break #aqui termina el while

def procesoPaga():
    while True:
        print("¿Desea pagar con tarjeta o efectivo?") #Se le pregunta
        pago = input("Ingrese su opcion (tarjeta/efectivo):").lower() #
        if pago == "tarjeta": #Si el usuario elige pagar con tarjeta
            print("Su pago se ha realizado con exito") #Se le avisa que se ha
            break #Termina el while
        elif pago == "efectivo": #Si el usuario elige pagar con efectivo
            print("Su pago se ha realizado con exito") #Se le avisa que se ha
            break #Termina el while
        else: #Si el usuario ingresa algo que no sea tarjeta o efectivo
            print("Opcion no valida, por favor ingrese una opcion valida") #Se le av
            continue #Reinicia el while



saludo() #llama a la funcion SALUDO
pedido() #Llama a la funcion PEDIDO 