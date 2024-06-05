ARCHIVO = 'envios25.txt'


def linea_sin_final(linea):
    if linea[-1] == '\n':
        linea = linea[:-1]
    return linea


def get_tipo_control(linea):
    if 'HC' in linea:
        return 'Hard Control'
    elif 'SC' in linea:
        return 'Soft Control'


def extraer_datos(linea):
    cp = linea[0:9].strip()
    direccion = linea[9:29].strip()
    tipo = int(linea[29].strip())
    pago = int(linea[30].strip())
    return (cp, direccion, tipo, pago)


def obtener_cp(linea):
    cp, _, _, _ = extraer_datos(linea)
    return cp


def obtener_direccion(linea):
    _, direccion, _, _ = extraer_datos(linea)
    return direccion


def obtener_tipo_pago(linea):
    _, _, tipo, pago = extraer_datos(linea)
    return tipo, pago


def obtener_pais_cp(cp):
    provincia = pais = ''
    if (len(cp) == 8
            and
            (cp[0].isalpha())
            and
            (cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[4].isdigit())
            and
            cp[5].isalpha() and cp[6].isalpha() and cp[7].isalpha()):
        pais = 'Argentina'
        if cp[0] == 'A':
            provincia = 'Salta'
        elif cp[0] == 'B':
            provincia = 'Provincia de Buenos Aires'
        elif cp[0] == 'C':
            provincia = 'Ciudad Autónoma de Buenos Aires'
        elif cp[0] == 'D':
            provincia = 'San Luis'
        elif cp[0] == 'E':
            provincia = 'Entre Ríos'
        elif cp[0] == 'F':
            provincia = 'La Rioja'
        elif cp[0] == 'G':
            provincia = 'Santiago del Estero'
        elif cp[0] == 'H':
            provincia = 'Chaco'
        elif cp[0] == 'J':
            provincia = 'San Juan'
        elif cp[0] == 'K':
            provincia = 'Catamarca'
        elif cp[0] == 'L':
            provincia = 'La Pampa'
        elif cp[0] == 'M':
            provincia = 'Mendoza'
        elif cp[0] == 'N':
            provincia = 'Misiones'
        elif cp[0] == 'P':
            provincia = 'Formosa'
        elif cp[0] == 'Q':
            provincia = 'Neuquén'
        elif cp[0] == 'R':
            provincia = 'Rio Negro'
        elif cp[0] == 'S':
            provincia = 'Santa Fe'
        elif cp[0] == 'T':
            provincia = 'Tucuman'
        elif cp[0] == 'U':
            provincia = 'Chubut'
        elif cp[0] == 'V':
            provincia = 'Tierra del Fuego'
        elif cp[0] == 'W':
            provincia = 'Corrientes'
        elif cp[0] == 'X':
            provincia = 'Córdoba'
        elif cp[0] == 'Y':
            provincia = 'Jujuy'
        elif cp[0] == 'Z':
            provincia = 'Santa Cruz'
    elif len(cp) == 4 and cp[0].isdigit() and cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit():
        pais = 'Bolivia'
    elif len(cp) == 9 and cp[0].isdigit() and cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[
        4].isdigit() \
            and cp[5] == '-' \
            and cp[6].isdigit() and cp[7].isdigit() and cp[8].isdigit():
        pais = 'Brasil'
    elif len(cp) == 7 and cp[0].isdigit() and cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[
        4].isdigit() and cp[5].isdigit() and cp[6].isdigit():
        pais = 'Chile'
    elif len(cp) == 6 and cp[0].isdigit() and cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[
        4].isdigit() and cp[5].isdigit():
        pais = 'Paraguay'
    elif len(cp) == 5 and cp[0].isdigit() and cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[
        4].isdigit():
        pais = 'Uruguay'
        if cp[0] == '1':
            montevideo = True
    else:
        pais = 'Otro'

    return provincia, pais


def calcular_pago(tipo, pago, pais, montevideo, cp):
    if tipo == 0:
        importe_inicial = 1100
    elif tipo == 1:
        importe_inicial = 1800
    elif tipo == 2:
        importe_inicial = 2450
    elif tipo == 3:
        importe_inicial = 8300
    elif tipo == 4:
        importe_inicial = 10900
    elif tipo == 5:
        importe_inicial = 14300
    elif tipo == 6:
        importe_inicial = 17900
    if pais == 'Argentina':
        importe_inicial += 0
    elif pais == 'Bolivia' or pais == 'Paraguay' or (pais == 'Uruguay' and montevideo == True):
        importe_inicial *= 1.2
    elif pais == 'Chile' or (pais == 'Uruguay' and montevideo == False):
        importe_inicial *= 1.25
    elif pais == 'Brasil' and (cp[0] == '8' or cp[0] == '9'):
        importe_inicial *= 1.2
    elif pais == 'Brasil' and (cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3'):
        importe_inicial *= 1.25
    elif pais == 'Brasil' and (cp[0] == '4' or cp[0] == '5' or cp[0] == '6' or cp[0] == '7'):
        importe_inicial *= 1.3
    elif pais == 'Otro':
        importe_inicial *= 1.5

    if pago == 1:
        importe_final = importe_inicial - (importe_inicial * 0.1)
    elif pago == 2:
        importe_final = importe_inicial

    return importe_final


def validar_direccion_hc(direccion):
    print(direccion)
    vino_mayus = False
    for car in direccion:
        if not (car.isalpha() or car.isdigit() or car == ' ' or car == '.'):
            return False
        if car.isupper():
            if vino_mayus:
                return False
            vino_mayus = True
        else:
            vino_mayus = False
    return validar_palabra(direccion)


def validar_palabra(direccion):
    esnumero = False
    for char in direccion:
        if char.isdigit():
            esnumero = True
        elif char == ' ' or char == '.':
            if esnumero:
                return True
            continue
    return False


def principal():
    archivo = open(ARCHIVO, encoding='UTF-8')
    r2 = r3 = r4 = 0
    linea = archivo.readline()
    linea_sin_final(linea)
    tipo_control = get_tipo_control(linea)
    print(tipo_control)

    linea = archivo.readline()
    while linea != '':

        linea_sin_final(linea)
        (cp, direccion, tipo, pago) = extraer_datos(linea)
        pais = obtener_pais_cp(cp)
        print(f'Código Postal: {cp} | Dirección: {direccion} | Tipo de Envío: {tipo} | Forma de Pago: {pago}')
        if tipo_control == 'Hard Control':
            if validar_direccion_hc(direccion):
                r2 += 1
                r4 += calcular_pago(tipo, pago, pais, False, cp)
            else:
                print(f'Dirección inválida: {direccion}')
                r3 += 1
        if tipo_control == 'Soft Control':
            r2 += 1
            r4 += calcular_pago(tipo, pago, pais, True, cp)
        linea = archivo.readline()
    print(f'Cantidad de direcciones válidas: {r2}')
    print(f'Cantidad de direcciones inválidas: {r3}')
    print(f'Total acumulado de importes finales: {r4}')


principal()
