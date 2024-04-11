'''
7. Votación en el Congreso
En el Congreso se vota la sanción de una ley muy importante. Desarrollar un programa que permita
ingresar la cantidad de votos a favor y en contra, e informe el porcentaje obtenido en cada caso.
'''

votos_favor = int(input('Ingrese la cantidad de votos a favor: '))
votos_contra = int(input('Ingrese la cantidad de votos en contra: '))

votos_total = votos_favor + votos_contra

porcentaje_votos_favor = (votos_favor * 100)/votos_total
print('Votos a favor: ' , porcentaje_votos_favor, '%')

porcentaje_votos_contra = (votos_contra * 100)/votos_total
print('Votos en contra: ', porcentaje_votos_contra, '%')