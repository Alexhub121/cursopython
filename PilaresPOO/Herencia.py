class animales(): #Ests es la clase pare por que hereda datos
    def habla(self):
        print("Yo soy un animal")

    def descripcion(self):
        print("Soy un {}".format(self.animal))

class perro(animales): #Aqui la classe perro hereda los metodos y atributos de la clase animales
    pass

class abeja(animales):
    def __init__(self, animal):
        self.animal = animal

animal = animales()
animal.habla()
perro = perro()
perro.habla()
abeja = abeja("Abeja")
abeja.descripcion()