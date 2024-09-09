#Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.
class Universidad():
    def __init__(self,Nombre):
        self.Nombre = Nombre

class Carerra():
    def carrera(self,especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad,Carerra):
    def datos(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} años, mi especialidad es {self.especialidad}. Estudio en la Universidad {self.Nombre}")

persona = Estudiante("Don Bosco")
persona.carrera("Sistemas")
persona.datos("Carlos", 20)