from publicacion import *
import random

def validar():
    n = int(input('Ingrese la cantidad de publicaciones: '))
    while n <= 0:
        n = int(input('Ingrese un numero valido: '))
    return n


def cargar():
    n = validar()
    p = [None] * n
    titulos = ('Inflacion', 'Elecciones', 'Robos', 'Futbol', 'Formula 1')
    for i in range(n):
        id = 'PUB' + '0' + str(i)
        titulo = random.choice(titulos)
        tipo = random.randint(1,30)
        costo = round(random.uniform(0,1000),2)
        p[i] = Publicacion(id, titulo, tipo, costo)
    print('Publicaciones cargadas')
    return p

def ordenar(p):
    n = len(p)
    for i in range(n-1):
        for j in range(i+1, n):
            if p[i].id > p[j].id:
                p[i], p[j] = p[j], p[i]


def mostrar(p):
    n = len(p)
    cont = 0
    ordenar(p)
    cos = float(input('Ingrese el costo: '))
    for i in range(n):
        if p[i].costo > cos:
            print(p[i])
            cont += 1
    print(f'Se muestran {cont} registros')


def contar(p):
    n = len(p)
    cont = [0] * 30
    x = int(input('Ingrese un numero: '))
    for i in range(n):
        ind = p[i].tipo - 1
        cont[ind] += 1
    for j in range(30):
        if cont[j] > x:
            print(f'Tipo: {j+1} --- Cantidad: {cont[j]}')


def buscar(p):
    n = len(p)
    nom = input('Ingrese un titulo: ')
    t = int(input('Ingrese un tipo: '))
    for i in range(n):
        if p[i].titulo == nom and p[i].tipo == t:
            print('Registro encontrado')
            print()
            print(p[i])
            return
    print('No se encuentran coincidencias con la busqueda')


def principal():
    publicaciones = []
    opcion = -1
    while opcion != 5:
        print('Menu de Opciones')
        print('*****************')
        print('1 - Cargar publicaciones')
        print('2 - Mostrar pulicaciones')
        print('3 - Contar publicaciones')
        print('4 - Buscar publicacion')
        print('5 - Salir')
        opcion = int(input('Ingrese una opcion: '))
        if opcion == 1:
            publicaciones = cargar()
        if opcion == 2:
            mostrar(publicaciones)
        if opcion == 3:
            contar(publicaciones)
        if opcion == 4:
            buscar(publicaciones)
        if opcion == 5:
            print('Adios')


if __name__ == '__main__':
    principal()
