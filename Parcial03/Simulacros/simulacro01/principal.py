from empleo import *
import random


def validar(num):
    n = int(input('Ingrese un valor mayor a ' + str(num) + ' porfavor: '))
    while n <= num:
        n = int(input('Se pidió mayor a ' + str(num) + ' cargue de nuevo porfavor: '))
    return n


def cargar_empleos():
    n = validar(0)
    empleos = [None] * n
    nombres = ('Programador', 'Mecánico', 'Electricista', 'Electrónico', 'Operario')
    for i in range(n):
        id = random.randint(1, 1000)
        desc = random.choice(nombres) + ' ' + str(i)
        tipo = random.randint(0, 39)
        sueldo = round(random.uniform(275000, 980000),2)
        empleos[i] = Empleo(id, desc, tipo, sueldo)
    print('Empleos generados....')
    print()
    return empleos


def ordenar_empleos(empleos):
    n = len(empleos)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if empleos[i].descripcion > empleos[j].descripcion:
                empleos[i], empleos[j] = empleos[j], empleos[i]


def mostrar_empleos(empleos):
    print('Ordenando empleos...')
    ordenar_empleos(empleos)
    sum = 0
    n = len(empleos)
    for i in range(n):
        sum += empleos[i].sueldo
        print(empleos[i])
    print(f'Suma de todos los sueldos pagados: ${sum}')
    print()


def contar_empleos(empleos):
    n = len(empleos)
    cont = [0] * 40
    for i in range(n):
        cont[empleos[i].tipo] += 1
    print('Cantidad de empleos por tipo: ')
    for j in range(40):
        if cont[j] != 0:
            print(f'Tipo: {j} Cantidad: {cont[j]}')
    print()

def buscar_empleo_id(empleos):
    n = len(empleos)
    num = int(input('Ingrese el id del empleo a buscar: '))
    for i in range(n):
        if num == empleos[i].identificador:
            print('Encontrado...')
            print(f'Descripción del empleo: {empleos[i].descripcion} Sueldo a pagar: ${empleos[i].sueldo}')
            return
    print('No se encuentran coincidencias en la búsqueda...')



def principal():
    empleos = []
    op = -1
    while op != 5:
        print('Menú de Opciones')
        print('*****************')
        print('1 - Cargar empleos ')
        print('2 - Mostrar empleos')
        print('3 - Cantidad de empleos por tipo')
        print('4 - Buscar empleo por id')
        print('5 - Salir')
        op = int(input('Ingrese la opción: '))
        if op == 1:
            empleos = cargar_empleos()
        if op == 2:
            if empleos:
                mostrar_empleos(empleos)
            else:
                print('No existen empleos cargados.Seleccione la opción 1')
        if op == 3:
            contar_empleos(empleos)
        if op == 4:
            buscar_empleo_id(empleos)
        if op == 5:
            print('Gracias por utilizar nuestro software. Hasta pronto!')


if __name__ == '__main__':
    principal()
