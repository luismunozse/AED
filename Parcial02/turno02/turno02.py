def es_digito(car):
    return car in '0123456789'


def es_consonante(car):
    return car in 'bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ'


def porcentaje(cant,total):
    if total > 0:
        return (cant * 100) // total
    return 0


def es_vocal(car):
    return car in 'aeiouAEIOUáéíóúÁÉÍÓÚ'


def principal():
    r1 = r2 = r3 = r4 = 0
    cont_letras = cont_palabras = 0
    cont_consonante = cont_r3 = 0
    cont_r2 = cont_t = 0
    existe_digito23 = existe_vocal = es_d = vino_de = False
    anterior = ''

    archivo = open('../turno01/entrada.txt')
    texto = archivo.read()
    archivo.close()


    for car in texto:
        if car == ' ' or car == '.':
            if cont_letras > 0:
                cont_palabras += 1

                if existe_digito23 and cont_consonante >= 2:
                    r1 += 1

                if existe_vocal and es_digito(anterior):
                    cont_r2 += 1

                if cont_letras >= 4 and cont_r3 == 3:
                    r3 += 1

                if cont_t >= 1:
                    r4 += 1

            cont_letras = 0
            cont_consonante = 0
            existe_digito23 = existe_vocal = False
            cont_r3 = 0
            vino_de = False
            cont_t = 0
            anterior = ''
        else:
            cont_letras += 1

            if (cont_letras == 2 or cont_letras == 3) and es_digito(car):
                existe_digito23 = True
            if cont_letras >= 4 and es_consonante(car):
                cont_consonante += 1

            if es_vocal(car):
                existe_vocal = True

            if cont_letras <= 3 and es_vocal(car):
                cont_r3 += 1

            if car in 'dD':
                es_d = True
            else:
                if es_d and car in 'eEéÉ':
                    vino_de = True
                es_d = False

            if vino_de and car in 'tT':
                cont_t += 1

            anterior = car

    r2 = porcentaje(cont_r2, cont_palabras)
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()