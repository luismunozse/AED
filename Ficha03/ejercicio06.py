'''
6. Cálculo de sueldo
Se conoce el monto del salario actual de un empleado, el nombre del empleado y el área funcional al cual pertenece.
Se pide calcular el nuevo salario del empleado sabiendo que obtuvo un incremento del 8% sobre su salario actual y
un descuento de 2.5% por servicios, informando los resultados con el formato que se especifica a continuación:

       Nombre Empleado:  xxxxxxxxx            Nuevo Salario: $ xxx

       Área Funcional:  xxxxxxxxxxxx

       Salario Actual: $ xxxx
'''

print('*' * 65)
print('Calculadora de Sueldo')
print('*' * 65)

nom_emp = input('Ingrese el nombre del empleado: ')
sal_emp = float(input('Ingrese el salario del empleado: '))
area_emp = input('Ingrese el area funcional a la cual pertenece el empleado: ')

nuevo_salario = ((sal_emp * 0.08) + sal_emp) - (sal_emp * 0.025)

print('Nombre Empleado: ', nom_emp)
print('Area Funcional: ', area_emp)
print('Salario Actual: $', sal_emp)
print('Nuevo Salario: $', nuevo_salario)

