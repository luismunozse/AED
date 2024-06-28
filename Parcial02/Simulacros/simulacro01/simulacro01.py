def es_impar(car):
    return car in '13579'


def es_vocal(car):
    return car in 'aeiouAEIOU'


def es_consonante(car):
    return car in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'


def es_minuscula(car):
    return car in 'abcdefghijklmnopqrstuvwxyz'


def promedio(cant, total):
    if total != 0:
        return cant // total
    return 0


def principal():
    r1 = r3 = r4 = 0
    r2 = None
    cont_letras = cont_palabras = 0
    es_letra_minuscula = comienza_impar = comienza_vocal = existe_b = False
    cont_vocal = cont_consonante = cont_car_r3 = cont_pal_r3 = 0
    vino_m = vino_a = False
    archivo = open('entrada.txt')
    texto = archivo.read()
    archivo.close()

    for car in texto:
        if car == ' ' or car == '.':
            if cont_letras >= 1:
                cont_palabras += 1
                if comienza_impar and es_letra_minuscula:
                    r1 = cont_palabras
                if comienza_vocal and existe_b:
                    if r2 is None or cont_letras > r2:
                        r2 = cont_letras
                if cont_consonante > cont_vocal and not vino_a and not vino_m:
                    cont_pal_r3 += 1
                    cont_car_r3 += cont_letras

            cont_letras = cont_palabras = 0
            es_letra_minuscula = comienza_impar = False
            comienza_vocal = existe_b = vino_a = vino_m = False
            cont_pal_r3 = cont_car_r3 = 0
        else:
            cont_letras += 1
            if cont_letras == 1 and es_impar(car):
                comienza_impar = True
            elif cont_letras >= 2 and es_minuscula(car):
                es_letra_minuscula = True

            if cont_letras == 1 and es_vocal(car):
                comienza_vocal = True
            elif cont_letras >= 2 and car in 'bB':
                existe_b = True

            if es_vocal(car):
                cont_vocal += 1
                if car in 'aA':
                    vino_a = True
            else:
                if es_consonante(car):
                    cont_consonante += 1
                    if car in 'mM':
                        vino_m = True

    r3 = promedio(cont_car_r3, cont_pal_r3)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()
