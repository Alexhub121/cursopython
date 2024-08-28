class FabricaTelefonos(): #Esta es la classe 
    def __init__(self, marca, *colores, **modelos): #un * es para crear tuplas y ** son para crear diccionarios
        self.marca = marca
        self.colores = colores #Estos son los atributos y con el self se engloban 
        self.modelos = modelos

telefono = FabricaTelefonos("Alcatel","Negro", "Azul", m1 =  500, m2 = 1000) #Aqui asigamos el diccionario agregando clave (m1) y su valor (500) // TELEFONO es el objeto
print(telefono.marca)  # Alcatel
print(telefono.colores)  # ('Negro', 'Azul', 'Verde')
print(telefono.modelos) #m1 = 500 , m2 = 1000
telefono.memoria = 512 #Asi se crean atributos temporales
print(telefono.memoria) #512