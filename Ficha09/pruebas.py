cp, cl, ct, mc = 0, 0, 0, 0
texto = open("prueba.txt","rt")
cadena = texto.read()
texto.close()
input('Presione enter para continuar')
for car in cadena:
    cl += 1
    if car == ' ' or car == '.':
        if cl > 1:
            cp += 1

        if cp == 1:
            mc = cl - 1
        elif cl > mc:
            mc = cl - 1

        cl = 0

print('Longitud de la palabra más corta:', mc)

open("prueba.txt")