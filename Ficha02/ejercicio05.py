'''
5. Cálculo de ángulos
Se sabe que la suma de dos ángulos desconocidos (alfa + beta) es igual a cierto valor x que se carga por teclado.
Además se sabe que la diferencia entre esos mismos dos ángulos (alfa - beta) es igual a otro valor y que también
se carga por teclado. Desarrolle un programa que dados los valores x e y, determine el valor de los dos ángulos alfa
y beta. No es necesario convertir a grados, minutos y segundos el valor de cada ángulo: expréselos como números reales,
tal cual hayan sido obtenidos.
'''

x = float(input('Ingrese el valor de x: '))
y = float(input('Ingrese el valor de y: '))

alfa = (x+y)/2
print('El valor del angulo alfa es: ' , alfa)
beta = x - alfa
print('El valor del angulo beta es: ' , beta)