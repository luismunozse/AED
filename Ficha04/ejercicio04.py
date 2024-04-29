'''
4. Temperatura diaria
Se solicita realizar un programa que permita ingresar tres temperaturas correspondientes a diferentes momentos de un
día y determinar:

Cual es el promedio de las temperaturas.
Si existe alguna temperatura que sea mayor al promedio.
'''


t1 = float(input('Temperatura N°1: '))
t2 = float(input('Temperatura N°2: '))
t3 = float(input('Temperatura N°3: '))

suma = t1 + t2 + t3
promedio = suma / 3
print('El promedio de temperaturas es: ' + str(promedio))

temp_mayor = max(t1,t2,t3)

if(temp_mayor > promedio):
    print('Existe una temperatura mayor al promedio y es: ' + str(temp_mayor))
else:
    print('No existen temperaturas mayores al promedio')