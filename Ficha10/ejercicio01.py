'''1. Sílaba "mo"
Desarrollar un programa en Python que permita cargar por teclado un texto completo (analizar dos opciones: una es cargar
todo el texto en una variable de tipo cadena de caracteres y recorrerla con un for iterador; y la otra es cargar cada caracter
uno por uno a través de un while). Siempre se supone que el usuario cargará un punto para indicar el final del texto, y que cada palabra de ese texto está
separada de las demás por un espacio en blanco. El programa debe:

a) Determinar cuántas palabras tenían más de 4 letras.

b) Determinar cuántas palabras tenían al menos una vez la letra "x" o la letra "y".

c) Determinar el promedio de letras por palabra en todo el texto.

d) Determinar cuántas palabras contuvieron sólo una vez la expresión "mo".

********************************************************************************
Ejemplo: 'el mono momoxy toca el xilofon.'
********************************************************************************
Palabras con más de 4 letras: 2
Palabras tenían al menos una vez la letra "x" o la letra "y": 2
El promedio de letras por palabra en todo el texto es: 4.17
Determinar cuántas palabras contuvieron sólo una vez la expresión "mo": 1'''

texto = input('Ingrese un texto: ')

cp = cl = clt = c4 = cxy = cmo = 0
es_m = es_x_y = es_mo = mas_de_4 = False

for car in texto:
    if car == ' ' or car == '.':
        if cl == 0:
            continue
        cp += 1
        if es_x_y:
            cxy += 1
        if es_mo:
            cmo += 1
        if mas_de_4:
            c4 += 1
        cl = 0
        es_x_y = False
        es_m = es_mo = False
    else:
        cl += 1
        print(cl)
        clt += 1
        if cl > 4:
            mas_de_4 = True
        if car == 'x' or car == 'y':
            es_x_y = True
        if car == 'm':
            es_m = True
        else:
            if es_m and car == 'o':
                es_mo = True
            es_m = False

print(f'Palabras con más de 4 letras: {c4}')
print(f'Palabras tenían al menos una vez la letra "x" o la letra "y": {cxy}')

if cp > 0:
    promedio = clt / cp
    print(f'El promedio de letras por palabra en todo el texto es: {round(promedio,2)}')

print(f'Determinar cuántas palabras contuvieron sólo una vez la expresión "mo": {cmo}')