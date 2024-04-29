'''
13. Triángulo Rectángulo
Desarrollar un programa que, ingresando los dos catetos de un triángulo rectángulo, informe:

Valor de la hipotenusa (redondeado a 2 decimales)
Valor del lado mayor
Valor del lado menor
'''


cat1 = float(input('Ingrese el valor del primer cateto: '))
cat2 = float(input('Ingrese el valor del segundo cateto: '))

hipotenusa = (cat1*cat1) + (cat2*cat2)

print('Valor de la hipotenusa: ' + str(round(hipotenusa,2)))
print('Valor del lado mayor: ' + str(max(cat1,cat2)))
print('valor del lado menor: ' + str(min(cat1,cat2)))