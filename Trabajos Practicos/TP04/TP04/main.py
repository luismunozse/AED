from envio import *
import os.path
import pickle


def crear_archivo_binario(ft, fb):
    if not os.path.exists(ft):
        print('El archivo ', ft, 'no existe')
        print('Controle y vuelva por aqui')
        return

    datos = open(ft, 'rt')
    ts = datos.readline()
    hd = datos.readline()

    m = open(fb, 'wb')
    for linea in datos:
        d = linea.split(',')
        cp = d[0]
        df = d[1]
        te = d[2]
        fp = d[3]
        env = Envio(cp, df, te, fp)
        pickle.dump(env, m)

    datos.close()
    m.close()


def mostrar_archivo_binario(fb):
    if not os.path.exists(fb):
        print(f'El archivo {fb} no existe')
        print('Controle y vuelva por aqui')
        return

    print('Listado General de envios...')

    c = 0
    m = open(fb, 'rb')

    while m.tell() < os.path.getsize(fb):
        env = pickle.load(m)
        pais = obtener_pais(env.codigo_postal)
        print(f'{env} País: {pais}')
        c += 1
    m.close()
    print(f'Se listaron {c} registros')


def crear_envio(fb):
    if not os.path.exists(fb):
        print(f'El archivo {fb} no existe')
        print('Controle y vuelva por aqui')
        return
    cp = input('Ingrese el código postal: ')
    dire = input('Ingrese dirección: ')
    tipo = int(input('Ingrese el tipo de envío: '))
    while tipo not in [0, 1, 2, 3, 4, 5, 6]:
        tipo = int(input('Error. Ingrese un numero del 0 al 6'))
    pago = int(input('Ingrese el tipo de pago: '))
    while pago not in [1, 2]:
        pago = int(input('Error. Ingrese 1-Efectivo 2-Tarjeta: '))
    env = Envio(cp, dire, tipo, pago)

    m = open(fb, 'ab')
    pickle.dump(env, m)
    print('Envío Agregado...')


def buscar_cp(fb):
    if not os.path.exists(fb):
        print(f'El archivo {fb} no existe')
        print('Controle y vuelva por aqui')
        return
    cp = input('Ingrese el CP a buscar: ')
    c = 0
    m = open(fb, 'rb')

    while m.tell() < os.path.getsize(fb):
        env = pickle.load(m)
        if env.codigo_postal == cp:
            pais = obtener_pais(env.codigo_postal)
            print(f'{env} Pais: {pais}')
            c += 1

    m.close()

    print(f'Se encontraron {c} registros')


def buscar_direccion(fb):
    if not os.path.exists(fb):
        print(f'El archivo {fb} no existe')
        print('Controle y vuelva por aqui')
        return

    d = input('Ingrese la dirección a buscar: ')

    m = open(fb, 'rb')
    encontrado = False

    while m.tell() < os.path.getsize(fb):
        env = pickle.load(m)
        if env.direccion == d:
            pais = obtener_pais(env.codigo_postal)
            print(f'{env} Pais: {pais}')
            encontrado = True
            break

    m.close()

    if not encontrado:
        print('No se encontró ningún registro con esa dirección')


def contar_envios_por_tipo_pago(fb):
    if not os.path.exists(fb):
        print(f'El archivo {fb} no existe')
        print('Controle y vuelva por aqui')
        return

    tipo, pago = 7, 2
    matriz_conteo = [[0]*pago for f in range(tipo)]

    m = open(fb, 'rb')

    while m.tell() < os.path.getsize(fb):
        env = pickle.load(m)
        tipo = int(env.tipo_envio)
        pago = int(env.forma_pago) - 1
        matriz_conteo[tipo][pago] += 1

    m.close()

    print('Cantidad de envios por combinacion de tipo de envio y forma de pago: ')
    for tipo in range(7):
        for pago in range(2):
            if matriz_conteo[tipo][pago] > 0:
                print(f'Tipo de Envio: {tipo} | Forma de Pago: {pago + 1} | Cantidad: {matriz_conteo[tipo][pago]} envíos')


def principal():
    ft = 'envios-tp4.csv'
    fb = 'envios-tp4.dat'

    opcion = -1

    while opcion != 9:

        print('Menú de Opciones: ')
        print('************************')
        print('1 - Crear archivo binario')
        print('2 - Cargar por teclado los datos de un envio')
        print('3 - Mostrar todos los registros')
        print('4 - Buscar por Código Postal')
        print('5 - Buscar por Dirección')
        print('6 - Mostrar cantidad de envios por tipo de envio y forma de pago')
        print('7 -  ')
        print('8 - ')
        print('9 - Salir')
        print()

        opcion = int(input('Ingrese su opción: '))

        if opcion == 1:
            respuesta = input('Advertencia! Un nuevo archivo será creado desde cero, ¿Desea continuar? (s/n): ')
            if respuesta.lower() == 's':
                crear_archivo_binario(ft, fb)
                print('Terminado...')
            else:
                print('Operación cancelada')
                return
        elif opcion == 2:
            crear_envio(fb)
        elif opcion == 3:
            mostrar_archivo_binario(fb)
        elif opcion == 4:
            buscar_cp(fb)
        elif opcion == 5:
            buscar_direccion(fb)
        elif opcion == 6:
            contar_envios_por_tipo_pago(fb)


if __name__ == '__main__':
    principal()
