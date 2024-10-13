from envio import *
import os.path
import pickle


def crear_archivo_binario(ft, fb):
    if os.path.exists(ft):
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
        print('El archivo', fb, 'no existe')
        print('Controle y vuelva por aqui')
        return

    print('Listado General de envios...')




def principal():
    pass


if __name__ == '__main__':
    principal()
