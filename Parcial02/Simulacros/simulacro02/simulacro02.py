def es_digito(car):
    return car in '0123456789'


def es_par(num):
    return num % 2 == 0


def es_consonante(car):
    return car in 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'


def es_vocal(car):
    return car in 'aeiouAEIOUáéíóúÁÉÍÓÚ'


def promedio(cant,total):
    if total != 0:
        return cant // total
    return 0


def principal():

    archivo = open('entrada.txt')
    texto = archivo.read()
    archivo.close()

    r1 = r3 = r4 = 0
    r2 = None
    cl = cp = 0
    cv = cc = cd = p = cs = cr3 = pr3 = cv12 = 0
    vino_r = vino_ra = False
    for car in texto:
        if car == ' ' or car == '.':
            if cl > 0:
                cp += 1

            if cl == cv + cc:
                if cv == cc and es_par(cl):
                    r1 += 1

            if cd >= 1 and p == 0:
                if r2 is None or cl > r2:
                    r2 = cl

            if cl > 2 and cs >= 1:
                cr3 += cl
                pr3 += 1

            if vino_ra and cv12 >= 1:
                r4 += 1

            cl = 0
            cv = cc = cd = p = cs = cv12 = 0
            vino_r = vino_ra = False
        else:
            cl += 1
            if es_vocal(car):
                cv += 1
            elif es_consonante(car):
                cc += 1
            if es_digito(car):
                cd += 1
            if car in 'pP':
                p += 1
            if car in 'sS':
                cs += 1
            if car in 'rR':
                vino_r = True
            else:
                if vino_r and car in 'aAáÁ':
                    vino_ra = True
                vino_r = False
            if cl <= 2 and es_vocal(car):
                cv12 += 1

    r3 = promedio(cr3,pr3)
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()