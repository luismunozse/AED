import envio as objEnvio


def cargar_envios_archivo(file, envios):
    m = open(file,'rt')
    nro_linea = 0
    for linea in m:
        nro_linea += 1
        if nro_linea == 1:
            continue
        if linea[-1] == '\n':
            linea = linea[:-1]
        if linea != '':
            envio = objEnvio.crear_envio_from_txt(linea)
            envios.append(envio)
    m.close()
    print('Envios cargados.....')


def generar_envios():
    envios = []
    n = int(input('Ingrese la cantidad de envios a generar: '))
    for i in range(n):
        envio = objEnvio.crear_envio()
        envios.append(envio)
    print('Envios generados.....')
    return envios

def principal():

    envios = []
    opcion = -1

    while opcion != 7:

        print('Menú de Opciones: ')
        print('************************')
        print('1 - Crear arreglo de envios a partir de un archivo de texto')
        print('2 - Cargar por teclado los datos de un envio')
        print('3 - Mostrar envios por código postal')
        print('4 - Buscar por dirección y tipo de envío')
        print('5 - Buscar por codigo postal')
        print('6 - Envíos según el tipo de control de direcciones (HC o SC)')
        print('7 - Salir')
        print()

        opcion = int(input('Ingrese su opción: '))

        if opcion == 1:
            file = input('Cargar el nombre del archivo: ')
            cargar_envios_archivo(file,envios)
        elif opcion == 2:
            envios = generar_envios()
        elif opcion == 3:



if __name__ == '__main__':
    principal()