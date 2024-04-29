'''
3. Jornal de un Operario
Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de
un determinado operario. Usted deberá cargar por teclado el código de turno que el operario trabajó ese día
(1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.

La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno.
Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50
pesos la hora.
'''

turno = int(input('Ingrese el codigo de turno del operario (1-Diurno 2-Nocturno): '))
cant_horas = int(input('Ingrese la cantidad de horas trabajadas: '))

if(turno == 1):
    pago_diurno = cant_horas * 35.50
    print('Monto a cobrar: $' + str(pago_diurno))
if(turno == 2):
    pago_nocturno = cant_horas * 40.60
    print('Monto a cobrar: $' + str(pago_nocturno))