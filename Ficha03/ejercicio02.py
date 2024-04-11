'''
2. Fecha como cadena
Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa una fecha
en formato 'dd/mm/aaaa', y muestre por separado el día, el mes y el año. Ejemplo: si la cadena ingresada
es '16/03/2016' el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'.
'''

fecha = input('Ingrese una fecha (en formato dd/mm/aaaa):' )
dia = fecha[0] + fecha[1]
mes = fecha[3] + fecha[4]
anio = fecha[6] + fecha[7] + fecha[8] + fecha[9]
print('Dia: ', dia, 'Mes: ', mes, 'Año: ', anio)