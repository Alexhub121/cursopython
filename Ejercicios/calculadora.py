class CALCULADORA():
    def info(self):
        print("Bienvenido a la calculadora de ALEX")
    
    def OPERACION(self):
        lista = []
        while True:

            try:
                self.operacion = str(input("Ingrese operacion a relaizar (+, - , / , x): "))
                self.num1 = float(input("Ingresa el PRIMER valor: "))
                self.num2 = float(input("Ingresa el SEGUNDO valor: "))
                
                if self.operacion == '+':
                    SUMA = self.num1 + self.num2 
                    print("El resultado de la suma es:" ,self.num1 + self.num2)
                    lista.append(SUMA)
                    break

                elif self.operacion == "-":
                    RESTA = self.num1 - self.num2 
                    print("El resultado de la resta es:" ,self.num1 - self.num2)
                    lista.append(RESTA)
                    break

                elif self.operacion == "/":
                        DIVISION = self.num1 / self.num2
                        print("El resultado de la division es:" ,self.num1 / self.num2)
                        lista.append(DIVISION)
                        break


                elif self.operacion == "x":
                    MULTIPLICACION = self.num1 * self.num2 
                    print("El resultado de la multiplicacion es:" ,self.num1 * self.num2)
                    lista.append(MULTIPLICACION)
                    break

            except:
                print("Ingrese datos correctos")
                continue

        pregunta = input(f"Este es el historial de resultados {lista}, deseas continuar?: ")
        if pregunta.lower() == "si" or pregunta.lower() == "s":
            self.info()
            self.OPERACION()
        elif pregunta.lower() == "no" or pregunta.lower() == "n":
                print("Gracias por usar la calculadora \nEXIT")
                quit()


calculadora = CALCULADORA()
calculadora.info()
calculadora.OPERACION()

