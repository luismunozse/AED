'''
4. Polinomio de segundo grado
Desarrollar un programa que cargue por teclado los coeficientes a, b y c de un polinomio de segundo grado,
y calcule y muestre el valor del polinomio en el punto x (cargando también x por teclado). Además, para el
mismo polinomio, calcule y muestre el valor del discriminante de la fórmula para el cálculo de las raíces de la ecuación.
'''

a = int(input('Ingrese el valor del coeficiente a: '))
b = int(input('Ingrese el valor del coeficiente b: '))
c = int(input('Ingrese el valor del coeficiente c: '))
x = int(input('Ingrese el valor del punto x: '))

calcular_polinomio = a*x**2 + b*x + c

calcular_discriminante = b**2 - 4*a*c

print('El valor del polinomio es: ' , calcular_polinomio)
print('El valor del discriminante es: ', calcular_discriminante)
