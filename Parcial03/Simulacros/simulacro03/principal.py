from servicio import *
import random

def validar():
    n = int(input('Ingrese la cantidad de servicios a generar: '))
    while n <= 0:
        n = int(input('Incorrecto. Ingrese un numero válido: '))
    return n


def cargar_servicios():
    n = validar()
    servicios = [None] * n
    nombres = ('Juan', 'Pedro', 'Pablo', 'Luis', 'Jorge')
    for i in range(n):
        cod = random.randint(1,1000)
        nom = random.choice(nombres)
        tipo = random.randint(1,10)
        imp = round(random.uniform(0,100000),2)
        servicios[i] = Servicio(cod, nom, tipo, imp)
    print('Servicios Cargados...')
    return servicios


def ordenar(servicios):
    n = len(servicios)
    for i in range(n-1):
        for j in range(i+1, n):
            if servicios[i].codigo > servicios[j].codigo:
                servicios[i], servicios[j] = servicios[j], servicios[i]


def mostrar_servicios(servicios):
    n = len(servicios)
    ordenar(servicios)
    i1 = float(input('Importe 1: '))
    i2 = float(input('Importe 2: '))
    for i in range(n):
        if i1 <= servicios[i].importe <= i2:
            print(servicios[i])
    print('No existen envios para mostrar')


def contar_servicios(servicios):
    n = len(servicios)
    cont = [0] * 10
    for i in range(n):
        cont[servicios[i].tipo] += 1
    for j in range(10):
        if cont[j] != 0:
            print(f'Servicio: Tipo: {j} Cantidad: {cont[j]}')


def buscar_servicio(servicios):
    n = len(servicios)
    nom = input('Ingrese el nombre del cliente a buscar: ')
    for i in range(n):
        if servicios[i].cliente == nom:
            servicios[i].importe += 2000
            print(servicios[i])
            return
    print('No se encontraron coincidencias')


def principal():
    servicios = []
    opcion = -1
    while opcion != 5:
        print('Menú de Opciones')
        print('****************')
        print('1 - Cargar servicio')
        print('2 - Mostrar servicio')
        print('3 - Contar servicios por tipo')
        print('4 - Buscar servicio por nombre de cliente')
        print('5 - Salir')
        opcion = int(input('Ingrese una opción: '))
        if opcion == 1:
            servicios = cargar_servicios()
        if opcion == 2:
            if servicios:
                mostrar_servicios(servicios)
            else:
                print('No existen envios para mostrar')
        if opcion == 3:
            contar_servicios(servicios)
        if opcion == 4:
            buscar_servicio(servicios)
        if opcion == 5:
            print('Hasta pronto!')


if __name__ == '__main__':
    principal()
