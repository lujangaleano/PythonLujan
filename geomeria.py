PI = 3.14

def menu():
    print("1. Calcular área Triangulo")
    print("2. Calcular perimetro Triangulo")
    print("3. Calcular área del Rectangulo")
    print("4. Calcular perimetro del Rectangulo")
    print("5. Calcular área de la elipse")
    print("6. Calcular perímetro de la elipse")
    print("0. salir")
    op = input("Opción: ")
    return op

def getAreaTriangulo(base, altura):
    return(base * altura) /2

def getPerimetroTriangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def getAreaRectangulo(largo, ancho):
    return largo * ancho

def getPerimetroRectangulo(largo,ancho):
    return(largo + ancho) * 2

def getAreaElipse(semiejeMayor,semiejeMenor = 1):
    return PI * semiejeMayor * semiejeMenor

def getPerimetroElipse(semiejeMayor,semiejeMenor):
    a = semiejeMayor
    b = semiejeMenor
    return 2*PI* ((a**2 + b**2)/2)**(0.5)

if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == "1":
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            resultado = getAreaTriangulo(base, altura)
            print(f"El area es {resultado} u²")
        elif opcion == "2":
            l1 = float(input("Lado 1:"))
            l2 = float(input("Lado 2:"))
            l3 = float(input("Lado 3:"))
            resultado = getPerimetroTriangulo(l1,l2,l3)
            print(f"El perimetro es {resultado} u") 
        elif opcion == "3":
            largo = float(input("largo: "))
            ancho = float(input("ancho: "))
            resultado = getAreaRectangulo(largo, ancho)
            print(f"El area del rectangulo es {resultado} u")
        elif opcion == "4":
            largo = float(input("largo: "))
            ancho = float(input("ancho: "))
            resultado = getPerimetroRectangulo(largo,ancho)
            print(f"El perimetro del rectangulo es {resultado}")
        elif opcion == "5":
              semiejeMayor = float(input("semiejeMayor: "))
              semiejeMenor = float(input("semiejeMenor: "))
              resultado = getAreaElipse(semiejeMayor,semiejeMenor)
              print(f"El elipse es {resultado}")
        elif opcion == "6":
            semiejeMayor = float(input("semiejemayor: "))
            semiejeMenor = float(input("semiejeMenor: "))
            resultado = getPerimetroElipse(semiejeMayor,semiejeMenor)
            print(f"El perimetro de la elipse es {resultado}")
        elif opcion == "0":
            print("salir")
            break