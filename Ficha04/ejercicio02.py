'''
2. Suma - División - Potencia
Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir
por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.
'''


num1 = float(input('Ingrese el primer numero: '))
num2 = float(input('Ingrese el segundo numero: '))
num3 = float(input('Ingrese el tercer numero: '))

suma = num1 + num2 + num3

if(suma > 10):
    print(suma//2)
else:
    print(pow(suma,3))