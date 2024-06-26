def es_digito_impar(car):
    return car in '13579'

def es_vocal(car):
    return car in 'aAeEiIoOuU'

def promedio(total,parcial):
    if total != 0:
        return (parcial * 100) // total
    return 0
def es_minuscula(car):
    return car.islower()

def es_consonante(car):
    return car in 'bcdfghjklmnñpqrstvwxyz'


def principal():
    r1 = r3 = r4 = 0
    cl = cp = cv = cc = ccvc = cpr3 = 0
    ini_impar = minuscula = es_b = inivoc = False
    r2 = None

    archivo = open('entrada.txt')
    texto = archivo.read()
    archivo.close()

    for car in texto:
        if car == ' ' or car == '.':
            # fuera de la palabra
            # r1
            if cl > 0:
                cp += 1
                if ini_impar and minuscula:
                    r1 += 1
            # r2
            if inivoc and es_b:
                if r2 is None or cl > r2:
                    r2 = cl
            # r3
            if cc > cv:
                cpr3 += 1
            cl = cc = cv = 0
            ini_impar = minuscula = es_b = False
        else:
            cl += 1
            # dentro de la palabra
            # r1
            if cl == 1 and es_digito_impar(car):
                ini_impar = True
            else:
                if cl > 1 and ini_impar and es_minuscula(car):
                    minuscula = True
                else:
                    minuscula = False
                    ini_impar = False
            # r2
            if cl == 1 and es_vocal(car):
                inivoc = True
            if car in 'bB':
                es_b = True
            #r3
            if es_consonante(car) and car != 'mM':
                cc += 1
            elif es_vocal(car) and car != 'aA':
                cv += 1
    r3 = promedio(cp,cpr3)
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()