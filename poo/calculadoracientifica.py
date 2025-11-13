class Calculadora:
    #atributos ¿?
    n1,n2 = None, None 
    #Constructor
    def __init__(self):
        self.n1 = 0
        self.n2 = 0

    def cargarNumeros(self,x,y):
        self.n1 = x
        self.n2 = y

    def sumar(self):
        return self.n1 + self.n2
    
#CalculadiraCientifica hereda de Calculadora
class CalculadoraCientfica(Calculadora):

    def __init__(self):
        super()#llama al constructos de la clase heredada
    
    def factorial(self):
        ac = 1
        for x in range(1,(self.n1+1)):
            ac = ac * x

        return ac
    
    def calcularPotencia( self, base, exponente):
        return base ** exponente

    def calcilarRaizCuadrada(self, valor):
        return valor ** (0.5)



if __name__ == "__main__":
    casio = Calculadora()                     #Declaracion y Construccion
    casio.cargarNumeros(15,9)                 #metodos
    print(f"La suma es {casio.sumar()}")      #metodos

    print("Calculadora Cientifica")
    casioFX = CalculadoraCientfica()
    casioFX.cargarNumeros(5,4)
    print(f"La suma es {casioFX.sumar()}")
    print(f"El factorial de 5 es: {casioFX.factorial()}")
    print(f"Raiz de 25 es: {casioFX.calcilarRaizCuadrada(25)}")
    print(f"5²: {casioFX.calcularPotencia(5,2)}")
   