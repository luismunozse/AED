# 8. Censo
# Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.
#
# Por cada habitante se ingresa: sexo (M/F) y edad. La carga de datos finaliza al ingresar cualquier otro valor para sexo.
#
# El programa debe informar:
#
# a) A qué sexo corresponde la mayor cantidad de habitantes (considerar que puede ser igual)
#
# b) Cantidad de mujeres en edad escolar (4 a 18 años inclusive)
#
# c) Si hay algún varón que supere los 80 años de edad

print('\t\tCENSO\t\t')

cont_m = cont_f = cant_mujeres_esc = 0
mayor_80 = False

sexo = input('Ingrese el sexo del habitante (M - masculino o F - femenino): ')

while sexo == 'M' or sexo == 'F':
    edad = int(input('Ingrese su edad: '))
    if sexo == 'M':
        cont_m += 1
        if edad > 80:
            mayor_80 = True
    else:
        cont_f += 1
        if edad >= 4 and edad <= 18:
            cant_mujeres_esc += 1
    sexo = input('Ingrese el sexo del habitante (M - masculino o F - femenino): ')

if cont_m > cont_f:
    print('El sexo masculino tiene la mayor cantidad de habitantes')
elif cont_m < cont_f:
    print('El sexo femenino tiene la mayor cantidad de habitantes')
else:
    print('Ambos sexos tienen igual cantidad de habitantes')

print(f'Cantidad de mujeres en edad escolar: {cant_mujeres_esc} mujeres')

if mayor_80:
    print('Existe al menos un varon mayor a 80 años')