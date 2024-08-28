class FabricaTelefonos():
    def __init__(self, marca , color): #Primer metodo constructor
        self.marca = marca
        self.color = color
        print(f"El objeto {self.marca} ah sido creado") 

    def __str__(self):
        return f"El objeto {self.marca} es de color {self.color}" #Sirve para brindar una mejor descripcion

    def __del__(self): #Elimina el objeto 
        print(f"El objeto {self.marca} se ha eliminado")

telefono = FabricaTelefonos("Nokia" , "Negro")
print(telefono.marca)
print(telefono)
