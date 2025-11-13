lluvia = False
finde = True
if not lluvia and finde:
    print("Voy al shopping")

elif lluvia or finde:
    print("Me quedo en casa")          
else:
    print("Voy al snpp")





#ejercicios condicionales
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segudo numero: "))
if num1 > num2:
    mayor = num1
else:
    mayor = num2

if mayor % 2 == 0:
    print(f"el numero mayor es {mayor} and es par.")
else:
    print(f"el numero mayor es {mayor} and es impar.")


#ejercicio 2
nombre = input("Ingrese su nombre: ")
contraseña = input("Ingrese su contraseña: ")
if nombre == "admin" and contraseña == "12344":
    print("Acceso correcto")
else:
    print("Acceso denegado")
    