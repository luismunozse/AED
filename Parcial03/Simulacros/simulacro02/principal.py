from ticket import *
import random


def validar(n):
    n = int(input('Ingresar la cantidad de tickets a generar: '))
    while n <= 0:
        n = int(input('Incorrecto. Ingrese un numero valido: '))

def cargar_tickets():
    n = validar(0)
    tickets = [None] * n
    nombres = ('LT', 'AA', 'FB', 'JS', 'GOL')
    for i in range(n):
        cod = random.choice(nombres) + '00' + str(i)


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
            pass
        if opcion == 2:
            pass


if __name__ == '__main__':
    principal()