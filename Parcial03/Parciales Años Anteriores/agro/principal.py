from trabajo import *
import random


def validar():
    n = int(input('Ingrese la cantidad de elementos: '))
    while n <= 0:
        n = int(input('Ingrese un valor correcto: '))
    return n


def cargar(n, t):
    for i in range(n):
        id = random.randint(1, 1000)
        desc = 'Trabajo ' + str(id)
        tipo = random.randint(0, 19)
        imp = round(random.uniform(10000, 100000), 2)
        cant = random.randint(1, 5)
        trabajo = Trabajo(id, desc, tipo, imp, cant)
        t.append(trabajo)


def ordenar(t):
    n = len(t)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if t[i].identificador < t[j].identificador:
                t[i], t[j] = t[j], t[i]


def mostrar(t):
    suma = 0
    ordenar(t)
    for trabajo in t:
        if trabajo.cantidad > 3:
            suma += trabajo.importe
            print(trabajo)
    print(f'La suma de los importes es: ${round(suma, 2)}')


def mostrar_trabajos_tipo(t):
    cont = [0] * 20
    for i in range(len(t)):
        pos = t[i].tipo
        cont[pos] += 1
    for i in range(20):
        if cont[i] > 0:
            print(f'Tipo: {i} | Cantidad: {cont[i]}')

def promedio(t):
    suma = prom = 0
    cant = len(t)
    for trabajo in t:
        suma += trabajo.importe
    if cant != 0:
        prom = suma/cant
    return prom


def mostrar_trabajo_promedio(t):
    prom = promedio(t)
    for trabajo in t:
        if trabajo.importe > prom:
            print(trabajo)


def buscar_trabajo(t):
    n = len(t)
    res = None
    num = int(input('Ingrese el numero de identificación: '))
    tipo = int(input('Ingrese el tipo: '))
    for i in range(n):
        if t[i].identificador == num and t[i].tipo == tipo:
            res = i
            break
    return res




def principal():
    trabajos = []
    op = -1
    while op != 6:
        print('Menu de Opciones')
        print('*****************')
        print('1 - Cargar datos')
        print('2 - Mostrar datos')
        print('3 - Mostrar trabajos por tipo')
        print('4 - Mostrar trabajos con importe mayor al promedio')
        print('5 - Buscar trabajo por id')
        print('6 - Salir')
        op = int(input('Ingrese su opción: '))
        if op == 1:
            n = validar()
            cargar(n, trabajos)
        if op == 2:
            if not trabajos:
                print('No se encuentran trabajos cargados')
            else:
                mostrar(trabajos)
        if op == 3:
            mostrar_trabajos_tipo(trabajos)
        if op == 4:
            mostrar_trabajo_promedio(trabajos)
        if op == 5:
            res = buscar_trabajo(trabajos)
            if res == None:
                print ('No se han encontrado coincidencias')
            else:
                print(f'Trabajo encontrado: {trabajos[res]}')
        if op == 6:
            print('Decir Adios! ... es crecer ...')


if __name__ == '__main__':
    principal()
