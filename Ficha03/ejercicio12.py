'''
12. Calculo de Posta de Natacion
En la disciplina olímpica una de las pruebas mas esperadas en la natacion es la posta 4x100. En esta disciplina el
equipo ganador registró los siguientes tiempos en cada estilo:

Espalda: 52 segundos 15 centésimas.
Pecho: 1 minuto 2 segundos 75 centésimas.
Mariposa: 59 segundos 80 centésimas.
Libre: 48 segundos 15 centésimas.
Usted debe averiguar el tiempo total de la carrera del equipo ganador y representarlo en minutos, segundos y centésimas.

Para recordar:

1 minutos son 60 segundos.
1 segundo son 100 centesimas.
'''

espalda_centesimas = (52*100) + 15
pecho_centesimas = ((1*60)*100) + (2*100) + 75
mariposa_centesimas = (59*100) + 80
libre_centesimas = (48*100) + 15

total_centesimas = espalda_centesimas + pecho_centesimas + mariposa_centesimas + libre_centesimas

minutos = (total_centesimas // (60*100))
resto = (total_centesimas % (60*100))
segundos = resto // 100
centesimas = resto % 100

print('Tiempo total equipo ganador: ' + str(minutos) + ':' + str(segundos) + ':' + str(centesimas))