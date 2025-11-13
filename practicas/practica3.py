import os


traducciones = {"hola":"hello","adios":"bye"}

while True:
    palabra = input("Ingrese una palabra a traducir: ")

    if palabra in traducciones:
        os.system("cls")
        print(f" (es) {palabra} : (en) {traducciones[palabra]}")
    elif palabra != "0":
        resp = input ("No existe {palabra}, desea registrarlo (S/N)")
        if resp == "S" or resp == "s":
            trad = input(f"Ingrese la traduccion de {palabra}:")
            if len(trad) > 0:
                traducciones[palabra] = trad
    else:
        break
        