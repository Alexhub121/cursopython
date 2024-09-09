class Preparatoria():
    def __init__(self, Name, year):
        self.Name = Name
        self.year = year

class Carrera():
    def carrera(self, especiality):
        self.especiality = especiality

class Alumno(Preparatoria, Carrera):
    def alumno(self, name, years):
        self.name = name
        self.years = years
        print(f"My name is {self.name} i have {self.years} years old, study in {self.Name} year:{self.year}, especiality: {self.especiality}")

persona = Alumno(input("input name to school:"), input("Year you curse?:"))
persona.carrera(input("what's ypu are study?:"))
persona.alumno(input("Input your name:"), input("how old are you?:"))