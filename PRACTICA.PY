def saludo():
    while True:
        try:
            nombre = input("Ingresa tu nombre:")
            if nombre.isalpha() and len(nombre) >= 3:
                print(f"Hola {nombre}, bienvenido a mi programa")
                break
            else:
                print("El nombre debe ser alfanumerico y tener al menos 3 caracteres")
                continue
        except :
            print("Error, por favor ingresa un nombre")
            continue


def menu():
    while True:

        menu = "cafe", "Leche"
        lista = []
        pedir = input("Deseas Ordenar? (s/n):")
        if pedir == "s":
            print(f"\nMenu de opciones:{menu}")        
            opcion = str(input("Ingresa tu opcion: (Cantidad y Producto)")).title()
            lista.append(opcion)
            pedir2 = input("Deseas Ordenar mas? (s/n):")
            if pedir2 == "s":
                print(f"\nMenu de opciones:{menu}")
                opcion2 = str(input("Ingresa tu opcion: (producto y cantidad)")).title()
                lista.append(opcion2)
                print(f"Tu pedido actual es{lista}")
                break
            elif pedir2 == "n":
                print(f"Tu pedido actual es{lista}")
                break
                
        elif pedir == "n":
            print("Gracias por visitar")
            break

saludo()
menu()