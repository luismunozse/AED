'''
5. Tarjeta de Bingo
Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100, que representaria la tarjeta
de bingo de una persona. Una vez generados los números aleatorios solicitar al usuario que ingrese 3 números enteros y
a partir de alli mostrar los siguientes mensajes:

Si el usuario no marcó ninguno de los números indicarlo diciendo "El jugador tiene mala suerte, no marcó ninguna casilla"
Caso contrario mostrar "El jugador marcó algún numero de la tarjeta".
'''

import random

numeros = random.sample(range(1,100),15)
print(numeros)

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))

if num1 in numeros or num2 in numeros or num3 in numeros:
    print('El jugador marco algun numero de la tarjeta')
else:
    print('El jugador tiene mala suerte, no marco ninguna casilla')


