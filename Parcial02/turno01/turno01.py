ARCHIVO = 'entrada.txt'


def es_vocal(car):
    return car in 'aeiouAEIOUáéíóúÁÉÍÓÚ'


def es_digito(car):
    return car in '0123456789'


def promedio(cant,total):
    if total > 0:
        return cant // total
    return 0


def principal():
    archivo = open(ARCHIVO)
    texto = archivo.read()
    archivo.close()

    r1 = r2 = r3 = r4 = 0
    cont_letras = cont_palabras = 0
    cont_vocales = cont_digitos = 0
    cont_r = cont_e = cont_car_r2 = cont_pal_r2 =0
    vino_f = vino_fi = False
    cont_n = cont_t = 0
    anterior = primera = ''
    for car in texto:
        if car == ' ' or car == '.':
            if cont_letras > 0:
                cont_palabras += 1

                if cont_letras == 6 and (1 <= cont_vocales <= 2) and cont_digitos >= 1:
                    r1 += 1

                if cont_r == 1 and cont_e >= 2:
                    cont_car_r2 += cont_letras
                    cont_pal_r2 += 1

                if primera.lower() != anterior.lower() and es_vocal(primera) and es_vocal(anterior):
                    r3 += 1

                if vino_fi and (cont_n == 1 or cont_t == 1):
                    r4 += 1

            cont_letras = 0
            cont_vocales = cont_digitos = 0
            cont_r = cont_e = 0
            vino_f = vino_fi = False
            cont_n = cont_t = 0
            primera = ''
        else:
            cont_letras += 1

            if es_vocal(car):
                cont_vocales += 1
            if es_digito(car):
                cont_digitos += 1

            if car in 'rR':
                cont_r += 1
            if car in 'eEéÉ':
                cont_e += 1

            if cont_letras == 1:
                primera = car

            if car in 'fF':
                vino_f = True
            else:
                if vino_f and car in 'iIíÍ':
                    vino_fi = True
                vino_f = False
            if car in 'nN':
                cont_n += 1
            elif car in 'tT':
                cont_t += 1

            anterior = car

    r2 = promedio(cont_car_r2,cont_pal_r2)
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()