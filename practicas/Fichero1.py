texto = input("Ingrese sus Datos: ")
nombreFichero = "agenda.txt"
f = open(nombreFichero, "a")
f.write(texto + '/n')
f.close()

leerFichero = open(nombreFichero, 'r')
print(leerFichero.read())
leerFichero.close()