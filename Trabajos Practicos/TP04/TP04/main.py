import envio
import os.path
import pickle


def generar_archivo_binario(origen, destino):
    if not os.path.exists(origen):
        print(f'El archivo {origen} no existe')
        return

    if os.path.exists(destino):
        respuesta = input('El archivo ya existe. Deseas eliminarlo y crear uno nuevo? (s/n): ')
        if respuesta.lower() == 's':
            print('Eliminando archivo y creando uno nuevo ... ')
            os.remove(destino)
        else:
            return

    datos = open(origen, 'rt')

    salida = open(destino, 'wb')

    for linea in datos:
        d = linea.split(',')
        cp = d[0]
        dire = d[1]
        tipo = int(d[2])
        pago = int(d[3])
        env = envio.Envio(cp, dire, tipo, pago)
        pickle.dump(env, salida)

    datos.close()
    salida.close()


def mostrar_archivo_binario(destino):
    if not os.path.exists(destino):
        print(f'EL archivo {destino} no existe')
        return
    print('Listado general de envios.....')
    c = 0
    m = open(destino, 'rb')
    t = os.path.getsize(destino)
    while m.tell() < t:
        env = pickle.load(m)
        print(env)
        c += 1
    m.close()
    print('Se listaron ', c, ' registros...')


def principal():
    origen = 'envios-tp4.csv'
    destino = 'envios-tp4.dat'
    generar_archivo_binario(origen, destino)
    print('Terminado...')
    mostrar_archivo_binario(destino)


if __name__ == '__main__':
    principal()
