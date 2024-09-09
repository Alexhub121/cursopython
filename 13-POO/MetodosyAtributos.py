class FabricaTelefonos():
    marca = "Iphone"
    color = "Negro"     #Estos son los atributos o caracteristicas del objeto
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self , mensaje): #Esto es un metodo o cosas que puede hacer el objeto #Esto es un metodo de estancia por que lo cree yo
        return mensaje 

    def musica(self):
        print("Estas escuchando musica")

telefono = FabricaTelefonos()
telefono.marca #asi agregamos el atributo/caracteristica al objeto
print(telefono.marca)

print(telefono.llamar("Hola, con quien hablo?")) #Aqui mandamos llamar el metodo
telefono.musica() #Mandamos a hablar el metodo musica