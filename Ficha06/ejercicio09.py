# 9. Mayor numero en orden par
# Ingresar de a uno una serie de números. Encontrar e imprimir el mayor de todos los números pares cuyo número
# de orden sea par, el proceso terminará cuando el número leído sea igual a cero

num = int(input('Ingrese un numero (con 0 corta): '))

orden = 0
mayor = None

while num != 0:
    if orden % 2 == 0 and num % 2 == 0:
        if mayor is None or num > mayor:
            mayor = num
    orden += 1
    num = int(input('Ingrese otro numero: '))

if not mayor is None:
    print(f'El mayor numero par en orden par es: {mayor}')
else:
    print('No se ingresaron numeros pares en orden par')

