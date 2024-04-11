'''
4. Duración de un vuelo
Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo (hora y minutos),
determine cuál es su duración en minutos. Si el viajero necesita luego 45 minutos más para ir del
aeropuerto al hotel que ha reservado, ¿a qué hora llegara al mismo?
'''


partida = input('Ingrese el horario de partida (hh:mm): ')
hora_partida = int(partida[0:2])
minuto_partida = int(partida[3:5])
llegada = input('Ingrese el horario de llegada (hh:mm): ')
hora_llegada = int(llegada[0:2])
minuto_llegada = int(llegada[3:5])
dur_vuelo = ((hora_llegada - hora_partida) * 60) + (minuto_llegada - minuto_partida)
print('El vuelo tiene una duracion de: ' , dur_vuelo, ' minutos')

# Llegar hasta el hotel le toma 45 minutos más, entonces:

hora_llegada_hotel = ((hora_llegada * 60) + minuto_llegada + 45) // 60
minuto_llegada_hotel = (minuto_llegada + 45) % 60
print('Llegará al hotel a las: ' , hora_llegada_hotel , ':' , minuto_llegada_hotel)
