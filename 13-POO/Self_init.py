"""class FabricaTelefonos():
    marca = "Samsung"

    def ElaborarHuawei(self): #Self sirve para elglobar atributos a todo en general 
        self.marca = "Huawei" #agregamos self. para englobar el atributo

telefono = FabricaTelefonos()
telefono.ElaborarHuawei() #llamamos al metodo para estar dentro del contexto 
print(telefono.marca) #para despues imprimirlo """


#__init__ es el costructor de la class , es el primer metodo que se ejecuta al crear metodo

class FabricaTelefono():
    def __init__(self, marca,color): #Sirve para ajecutarce al iniciar el objeto
        self.marca = marca #self es el contexto de la clase
        self.color = color #self es el contexto de la clase


telefono = FabricaTelefono('Huawei', 'Rojo')
print(telefono.marca) #imprime huawei
print(telefono.color) #imprime rojo