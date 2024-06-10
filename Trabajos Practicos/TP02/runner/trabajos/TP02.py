ARCHIVO = 'envios100HC.txt'


def linea_sin_final(linea):
    if linea[-1] == '\n':
        linea = linea[:-1]
    return linea


def get_tipo_control(linea):
    if 'HC' in linea:
        return 'Hard Control'
    elif 'SC' in linea:
        return 'Soft Control'

def validar_palabra(direccion):
    es_numero = False
    for char in direccion:
        if char.isdigit():
            es_numero = True
        elif char == ' ' or char == '.':
            if es_numero:
                return True
            continue
    return False

def validar_direccion(direccion):
    # print(direccion)
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


def extraer_datos(linea):
    cp = linea[0:9].strip()
    direccion = linea[9:29].strip()
    tipo = int(linea[29].strip())
    pago = int(linea[30].strip())
    return (cp, direccion, tipo, pago)

def obtener_pais(cp):
    provincia = ''
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
            provincia = 'Montevideo'
    else:
        pais = 'Otro'

    return pais, provincia


def tipo_envio(tipo):
    costo_envio = 0
    if tipo == 0:
        costo_envio = 1100
    elif tipo == 1:
        costo_envio = 1800
    elif tipo == 2:
        costo_envio = 2450
    elif tipo == 3:
        costo_envio = 8300
    elif tipo == 4:
        costo_envio = 10900
    elif tipo == 5:
        costo_envio = 14300
    elif tipo == 6:
        costo_envio = 17900
    return int(costo_envio)

def tipo_carta(tipo):
    if tipo == 0 or tipo == 1 or tipo == 2:
        return 'Carta Simple'
    if tipo == 3 or tipo == 4:
        return 'Carta Certificada'
    if tipo == 5 or tipo == 6:
        return 'Carta Expresa'

def calcular_precio(cp, tipo, pago):
    importe_final = 0
    costo_tipo = tipo_envio(tipo)
    (pais,provincia) = obtener_pais(cp)
    if pais == 'Argentina':
        importe_final = costo_tipo
    elif pais == 'Bolivia' or pais == 'Paraguay' or (pais == 'Uruguay' and provincia == 'Montevideo'):
        importe_final = int(costo_tipo * 1.2)
    elif pais == 'Chile' or (pais == 'Uruguay' and provincia != 'Montevideo'):
        importe_final = int(costo_tipo * 1.25)
    elif pais == 'Brasil' and (cp[0] == '8' or cp[0] == '9'):
        importe_final = int(costo_tipo * 1.2)
    elif pais == 'Brasil' and (cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3'):
        importe_final = int(costo_tipo * 1.25)
    elif pais == 'Brasil' and (cp[0] == '4' or cp[0] == '5' or cp[0] == '6' or cp[0] == '7'):
        importe_final = int(costo_tipo * 1.3)
    elif pais == 'Otro':
        importe_final = int(costo_tipo * 1.5)
    if pago == 1:
        importe_final = int(importe_final - (importe_final * 0.1))
    elif pago == 2:
        importe_final = int(importe_final)
    # Print de Control
    # print(f'Importe final: ${int(importe_final)}')
    return int(importe_final)


def principal():
    # Acceso al archivo
    archivo = open(ARCHIVO)
    cont_env_ext = cont_env = suma_precio_envio = cont_prov_bs_as = 0
    r2 = r3 = r4 = r5 = r6 = r7 = r10 = r13 = 0
    r8 = r12 = ''
    r11 = None
    # Lectura primer linea
    linea = archivo.readline()
    # Quitando el salto de linea
    linea_sin_final(linea)
    # Asignamos a r1 la funcion que determina el tipo de control
    r1 = get_tipo_control(linea)
    # Respuesta 1
    print(f'(r1) - Tipo de Control de direcciones: {r1}')
    # Leemos la segunda linea
    linea = archivo.readline()
    # Extraccion de datos de la 1er linea de envios
    linea_1 = extraer_datos(linea)
    # Extraer datos devuelve una tupla, y la posicion 0 corresponde al cp
    r9 = linea_1[0]
    # Recorremos linea por linea el archivo
    while linea != '':
        # Quitamos el salto de linea por cada linea recorrida
        linea_sin_final(linea)
        (cp, direccion, tipo, pago) = extraer_datos(linea)
        pais, provincia = obtener_pais(cp)
        precio_envio = calcular_precio(cp,tipo,pago)
        # print(f'Código Postal: {cp} | Dirección: {direccion} | Tipo de Envío: {tipo} | Forma de Pago: {pago}')
        # print(f'País: {pais} | Provincia: {provincia}')
        if cp == r9:
            r10 += 1
        if r1 == 'Hard Control':
            if validar_direccion(direccion):
                r2 += 1
                r4 += precio_envio
                # Contador de tipos de carta
                if tipo_carta(tipo) == 'Carta Simple':
                    r5 += 1
                elif tipo_carta(tipo) == 'Carta Certificada':
                    r6 += 1
                elif tipo_carta(tipo) == 'Carta Expresa':
                    r7 += 1
                if pais != 'Argentina':
                    cont_env_ext += 1
                if provincia == 'Provincia de Buenos Aires':
                    cont_prov_bs_as += 1
                    suma_precio_envio += precio_envio
            else:
                # print(f'Dirección Inválida: {direccion}')
                r3 += 1
        if r1 == 'Soft Control':
            r2 += 1
            r4 += precio_envio
            if tipo_carta(tipo) == 'Carta Simple':
                r5 += 1
            elif tipo_carta(tipo) == 'Carta Certificada':
                r6 += 1
            elif tipo_carta(tipo) == 'Carta Expresa':
                r7 += 1
            if pais != 'Argentina':
                cont_env_ext += 1
            if provincia == 'Provincia de Buenos Aires':
                suma_precio_envio += precio_envio
                cont_prov_bs_as += 1


        if pais == 'Brasil':
            # defino el menor importe pagado para envios a Brasil
            if r11 is None or precio_envio < r11:
                r11 = precio_envio
        # r12
        if precio_envio == r11:
            r12 = cp
        cont_env += 1
        linea = archivo.readline()
    # Defino el tipo de carta con mayor envio
    if r5 > r6 and r5 > r7:
        r8 = 'Carta Simple'
    elif r6 > r5 and r6 > r7:
        r8 = 'Carta Certificada'
    elif r7 > r5 and r7 > r6:
        r8 = 'Carta Expresa'
    r13 = (cont_env_ext * 100) // cont_env
    r14 = int(suma_precio_envio / cont_prov_bs_as)
    print(f'(r2) - Cantidad de envíos con dirección válida: {r2}')
    print(f'(r3) - Cantidad de envíos con dirección no válida: {r3}')
    print(f'(r4) - Total acumulado de importes finales: {r4}')
    print(f'(r5) - Cantidad de Cartas Simples: {r5}')
    print(f'(r6) - Cantidad de Cartas Certificadas: {r6}')
    print(f'(r7) - Cantidad de Cartas Expresas: {r7}')
    print(f'(r8) - Tipo de carta con mayor cantidad de envios: {r8}')
    print(f'(r9) - Código Postal del primer envío del archivo: {r9}')
    print(f'(r10) - Cantidad de veces que entró ese primero: {r10}')
    print(f'(r11) - Importe menor pagado por envios a Brasil: {r11}')
    print(f'(r12) - Código Postal del Envio a Brasil con importe menor: {r12}')
    print(f'(r13) - Porcentaje de envios al exterior sobre el total: {r13}')
    print(f'(r14) - Importe final promedio de los envios a Buenos Aires: {r14}')

principal()
