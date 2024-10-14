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


def validar_archivo_binario(fb):
    if not os.path.exists(fb):
        print(f'El archivo {fb} no existe')
        print('Controle y vuelva por aqui')
        return


def mostrar_archivo_binario(fb):
    validar_archivo_binario(fb)

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
    validar_archivo_binario(fb)
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
    validar_archivo_binario(fb)
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
    validar_archivo_binario(fb)

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
    validar_archivo_binario(fb)

    tipo, pago = 7, 2
    matriz_conteo = [[0]*pago for f in range(tipo)]

    m = open(fb, 'rb')

    while m.tell() < os.path.getsize(fb):
        env = pickle.load(m)
        tipo = int(env.tipo_envio)
        pago = int(env.forma_pago) - 1
        matriz_conteo[tipo][pago] += 1

    m.close()
    return matriz_conteo


def mostrar_conteo_combinado(matriz_conteo):
    for pago in range(2):
        print(f'Forma de Pago {pago + 1}')
        if pago == 0:
            print('***(Pagos en efectivo)***')
        if pago == 1:
            print('***(Pagos con tarjeta)***')
        for tipo in range(7):
            if matriz_conteo[tipo][pago] > 0:
                print(f'Tipo de Envío: {tipo} | Cantidad: {matriz_conteo[tipo][pago]} envíos')
        print()


def total_por_tipo_envio(matriz_conteo):
    print('Total de envíos por tipo de envio: ')
    for tipo in range(7):
        total = 0
        for pago in range(2):
            total += matriz_conteo[tipo][pago]
            if pago == 1:
                print(f'Tipo de Envío: {tipo} - Total: {total} envíos')
            if pago == 2:
                print(f'Tipo de Envío: {tipo} - Total: {total} envíos')


def total_por_forma_pago(matriz_conteo):
    print('Total de envíos por forma de pago: ')
    for pago in range(2):
        total = 0
        for tipo in range(7):
            total += matriz_conteo[tipo][pago]
        print(f'Forma de Pago: {pago + 1} - Total: {total} envíos')


def calcular_promedio(fb):
    validar_archivo_binario(fb)
    m = open(fb, 'rb')
    importe_total = 0
    cantidad_envios = 0
    while m.tell() < os.path.getsize(fb):
        env = pickle.load(m)
        pais = obtener_pais(env.codigo_postal)
        precio = calcular_precio_envio(env.codigo_postal, pais, int(env.tipo_envio), int(env.forma_pago))
        importe_total += precio
        cantidad_envios += 1
    m.close()
    if cantidad_envios == 0:
        print('No hay envios para calcular el promedio')
        return
    promedio = importe_total / cantidad_envios
    print(f'El importe promedio entre todos los envios es: {round(promedio,2)}')
    return promedio


def generar_arreglo(fb, promedio):
    validar_archivo_binario(fb)
    envios = []
    m = open(fb, 'rb')
    while m.tell() < os.path.getsize(fb):
        env = pickle.load(m)
        pais = obtener_pais(env.codigo_postal)
        precio = calcular_precio_envio(env.codigo_postal, pais, int(env.tipo_envio), int(env.forma_pago))
        if precio > promedio:
            envios.append(env)
    return envios


def principal():
    ft = 'envios-tp4.csv'
    fb = 'envios-tp4.dat'
    matriz_conteo = contar_envios_por_tipo_pago(fb)

    opcion = -1

    while opcion != 9:

        print('Sistema de Gestión de Envíos por Correo v4.0')
        print('¡Bienvenido!')
        print('Seleccione una opción: ')
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
            mostrar_conteo_combinado(matriz_conteo)
        elif opcion == 7:
            total_por_forma_pago(matriz_conteo)
            total_por_tipo_envio(matriz_conteo)
        elif opcion == 8:
            calcular_promedio(fb)
        elif opcion == 9:
            print('Gracias por utilizar nuestro software. Vuelva pronto')


if __name__ == '__main__':
    principal()
