'''
6. Analisis de palabra
Se pide un programa que le solicite al usuario que ingrese una palabra. Con esa palabra calcular los siguientes puntos:

Determinar la cantidad de letras que tiene  la palabra.
Mostrar un mensaje que informe si la palabra termina en vocal.
'''


palabra = input('Porfavor, ingrese una palabra: ')

cant_letras = len(palabra)
ultima_letra = palabra[cant_letras - 1]
vocales = ('a','e','i','o','u')

if ultima_letra in vocales:
    print('La palabra ingresada termina en vocal')
else:
    print('La palabra indicada no termina en vocal')