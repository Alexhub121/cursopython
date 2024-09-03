class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self): #Esto es lo que se va a herdedar a las classes "Perro" y "Pez" , a eso se llama polimorfismo y es cuando se modifica
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo hago Woof") #Aqui modificamos el metodo heredado de hablar paso de self.mensaje a lo que esta en el print

class Pez(Animales):
    def hablar(self):
        print("Yo hago gluglu") #Aqui modificamos el metodo heredado de hablar paso de self.mensaje a lo que esta en el print

perro = Perro("Guaaau!!")
animal = Animales("Miau")
pez = Pez("Gluglu")

animal.hablar()
perro.hablar()
pez.hablar()
