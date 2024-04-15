''' Desafio01-CHATGPT'''

def segundos_a_tiempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    if horas <= 24:
        print(f"El tiempo transcurrido fue de {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
    else:
        print("Excedido")

def tiempo_a_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

# Prueba de la conversión de segundos a tiempo
for i in range(4):
    segundos = int(input("Ingrese la cantidad de segundos: "))
    segundos_a_tiempo(segundos)

# Prueba de la conversión de tiempo a segundos
horas = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))
total_segundos = tiempo_a_segundos(horas, minutos, segundos)
print(f"La cantidad total de segundos es: {total_segundos}")

