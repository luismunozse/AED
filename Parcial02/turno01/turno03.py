def es_digito(car):
    return car in '0123456789'


def es_minuscula(car):
    return car in 'abcdefghijklmnñopqrstuvwxyz'


def es_consonante(car):
    return car in 'bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ'

def principal():

    archivo = open('entrada.txt')
    texto = archivo.read()
    archivo.close()

    r1 = r3 = r4 = 0
    r2 = None
    cl = cp = 0
    cd = cmin = cont_a = cont_n = 0
    es_s = vino_se = False
    anterior = ''
    for car in texto:
        if car == ' ' or car == '.':
            if cl > 0:
                cp += 1

            if cd == 1 and cmin == cl - 1:
                r1 += 1

            if cd >= 1:
                if r2 is None or cl < r2:
                    r2 = cl

            if cont_n == 2 and cont_a >= 1:
                r3 += 1

            if vino_se and es_consonante(anterior):
                r4 += 1

            cl = 0
            cd = cmin = cont_a = cont_n = 0
            es_s = vino_se = False
            anterior = ''
        else:
            cl += 1

            if es_digito(car):
                cd += 1
            if es_minuscula(car):
                cmin += 1

            if car in 'nN':
                cont_n += 1
            if cl <= 4 and car in 'aAáÁ':
                cont_a += 1

            if cl <= 2:
                if car in 'sS':
                    es_s = True
                else:
                    if es_s and car in 'eEéÉ':
                        vino_se = True
                    es_s = False
            anterior = car



    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()