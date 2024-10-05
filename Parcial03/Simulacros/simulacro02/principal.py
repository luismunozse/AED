from ticket import *
import random


def validar():
    n = int(input('Ingresar la cantidad de tickets a generar: '))
    while n <= 0:
        n = int(input('Incorrecto. Ingrese un numero valido: '))
    return n


def cargar_tickets():
    n = validar()
    tickets = [None] * n
    for i in range(n):
        cod = 'Codigo: ' + str(i)
        id = random.randint(1, 1000)
        pais = random.randint(1, 20)
        but = random.randint(1, 100)
        imp = round(random.uniform(0, 100000),2)
        tickets[i] = Ticket(cod, id, pais, but, imp)
    print('Tickets generados...')
    return tickets


def ordenar_tickets(tickets):
    n = len(tickets)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if tickets[i].codigo_vuelo > tickets[j].codigo_vuelo:
                tickets[i], tickets[j] = tickets[j], tickets[i]


def mostrar_tickets(tickets):
    num = int(input('Ingrese un numero: '))
    ordenar_tickets(tickets)
    print(ordenar_tickets(tickets))
    for ticket in tickets:
        if ticket.nro_asiento > num:
            print(ticket)
    print('No existen nros de asientos mayores al numero ingresado')


def importe_acumulado(tickets):
    t = int(input('Ingrese un numero (entre 1 y 20): '))
    n = len(tickets)
    cont = [0] * 20
    acu = 0
    for i in range(n):
        pos = tickets[i].pais_destino - 1
        cont[pos] += tickets[i].importe
    for j in range(20):
        if cont[j] > t:
            print(f'Pais de destino: {j+1} Importe acumulado: ${cont[j]}')


def buscar_ticket(tickets):
    n = len(tickets)
    id = int(input('Ingrese el numero de identificacion: '))
    for i in range(n):
        if tickets[i].identificador_pasajero == id:
            print(f'Ticket encontrado: {tickets[i]}')
            return
    print('No se encuentran coincidencias con la busqueda')


def principal():
    tickets = []
    opcion = -1
    while opcion != 5:
        print('Menu de opciones')
        print('*****************')
        print('1 - Cargar tickets')
        print('2 - Mostrar tickets')
        print('3 - Calcular importe acumulado por pais')
        print('4 - Buscar ticket por id de pasajero')
        print('5 - Salir ')
        opcion = int(input('Seleccione una opcion: '))
        if opcion == 1:
            tickets = cargar_tickets()
        if opcion == 2:
            mostrar_tickets(tickets)
        if opcion == 3:
            importe_acumulado(tickets)
        if opcion == 4:
            buscar_ticket(tickets)
        if opcion == 5:
            print('Gracias por usar el programa')

if __name__ == '__main__':
    principal()
