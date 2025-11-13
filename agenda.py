#agenda telefonica 
#usar dicc: clave:valor, nombre:telefono
agenda = {}
def guardarRegistro(nombre, telefono):
    agenda[nombre] = telefono

def imprimirAgenda():
    print(agenda) 

#crear menu 
while True:
    print("1.Guardar contacto\n2.Imprimir\n3.Salir")
    opcion = input("Opcion: ")
    if opcion == "1":
        nomb = input("Nombre. ")
        tel = input("Telfono: ")
        guardarRegistro(nomb, tel)
    elif opcion == "2":
        imprimirAgenda()
    elif opcion == "0":
        break
    else:
        print("Opcion invalida")
         