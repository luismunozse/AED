'''
Desarrollar un programa que permita ingresar una palabra por teclado y la devuelva enmascarada, mostrando la primer
letra y la última, pero reemplazando los caracteres intermedios por asteriscos.
Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”.
'''

palabra: str = input('Ingrese una palabra: ')
ultima_letra = palabra[len(palabra)-1]
primer_letra = palabra[0]
print(primer_letra + '*' * (len(palabra) - 2) + ultima_letra)
