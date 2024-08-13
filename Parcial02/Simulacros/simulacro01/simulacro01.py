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
    es_letra_minuscula = comienza_impar = comienza_vocal = existe_b = vino_d = vino_dv = False
    cont_vocal = cont_consonante = cont_car_r3 = cont_pal_r3 = cont_dv = 0
    cont_m = cont_a = 0
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
                if cont_consonante > cont_vocal and cont_m == 0 and cont_a == 0:
                    cont_pal_r3 += 1
                    cont_car_r3 += cont_letras
                if vino_dv and cont_dv >= 2:
                    r4 += 1

            cont_letras = cont_palabras = cont_m = cont_a = cont_consonante = cont_vocal = 0
            es_letra_minuscula = comienza_impar = False
            comienza_vocal = existe_b = False
            vino_dv = vino_d = False
            cont_dv = 0
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
            elif es_consonante(car):
                cont_consonante += 1

            if car in 'mM':
                cont_m += 1
            if car in 'aáAÁ':
                cont_a += 1

            if car in 'dD':
                vino_d = True
            else:
                if vino_d and es_vocal(car):
                    vino_dv = True
                    cont_dv += 1
                vino_d = False

    r3 = promedio(cont_car_r3, cont_pal_r3)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()
