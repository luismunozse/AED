from juicio import *
import random


def validar():
    n = int(input('Ingrese la cantidad de juicios a generar: '))
    while n <= 0:
        n = int(input('Ingresa un numero valido: '))
    return n


def cargar():
    n = validar()
    juicios = [None] * n
    nombres = ('Cristina Kirchner', 'Amado Bodou', 'Alberto Fernandez', 'Lazaro Baez', 'Eduardo Belliboni')
    for i in range(n):
        cod = random.randint(1,50)
        desc = 'Juicio ' + str(i)
        tipo = random.randint(1,15)
        cte = random.choice(nombres)
        hono = round(random.uniform(0,10000),2)
        juicios[i] = Juicio(cod,desc,tipo,cte,hono)
    print('Juicios cargados')
    print()
    return juicios


def ordenar(juicios):
    n = len(juicios)
    for i in range(n-1):
        for j in range(i+1, n):
            if juicios[i].descripcion > juicios[j].descripcion:
                juicios[i], juicios[j] = juicios[j], juicios[i]


def mostrar(juicios):
    cant = 0
    n = len(juicios)
    ordenar(juicios)
    mon = float(input('Ingrese el monto: '))
    for i in range(n):
        if juicios[i].honorarios > mon:
            print(juicios[i])
            cant += 1
    print(f'Se muestran {cant} resultados')


def contar(juicios):
    n = len(juicios)
    cont = [0] * 15
    c = int(input('Ingrese una cantidad: '))
    for i in range(n):
        cont[juicios[i].tipo - 1] += 1
    for j in range(15):
        if cont[j] > c:
            print(f'Tipo: {j+1} --- Cantidad: {cont[j]}')


def buscar(juicios):
    n = len(juicios)
    cod = int(input('Ingrese el codigo de expediente: '))
    for i in range(n):
        if juicios[i].codigo == cod:
            print('Registro encontrado...')
            nm = int(input('Ingrese el nuevo monto: '))
            juicios[i].honorarios = nm
            print(juicios[i])
            return
    print('No se encuentran coincidencias')


def principal():
    juicios = []
    opcion = -1
    while opcion != 5:
        print('Sistema de procesamiento de juicios')
        print('************************************')
        print('1 - Cargar juicios')
        print('2 - Mostrar juicios')
        print('3 - Mostrar juicios por tipo')
        print('4 - Buscar juicio')
        print('5 - Salir')
        print()
        opcion = int(input('Ingrese una opcion: '))
        if opcion == 1:
            juicios = cargar()
        if opcion == 2:
            mostrar(juicios)
        if opcion == 3:
            contar(juicios)
        if opcion == 4:
            buscar(juicios)
        if opcion == 5:
            print('Gracias por utilizar nuestro software')


if __name__ == '__main__':
    principal()
