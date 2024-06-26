ARCHIVO = 'envios.txt'

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

    arg_provs = ('Salta',
                'Provincia de Buenos Aires',
                'Ciudad Autónoma de Buenos Aires',
                'San Luis',
                'Entre Ríos',
                'La Rioja',
                'Santiago del Estero',
                'Chaco',
                'San Juan',
                'Catamarca',
                'La Pampa',
                'Mendoza',
                'Misiones',
                'Formosa',
                'Neuquén',
                'Rio Negro',
                'Santa Fe',
                'Tucuman',
                'Chubut',
                'Tierra del Fuego',
                'Corrientes',
                'Córdoba',
                'Jujuy',
                'Santa Cruz')

    abecedario = ('A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'J',
                'K',
                'L',
                'M',
                'N',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z')


    if (len(cp) == 8
            and
            (cp[0].isalpha() and cp[0].lower() not in {'i', 'o'})
            and
            (cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[4].isdigit())
            and
            cp[5].isalpha() and cp[6].isalpha() and cp[7].isalpha()):
        pais = 'Argentina'

        for i in range(len(abecedario)):
            letra = abecedario[i]
            if cp[0] == letra:
                provincia = arg_provs[i]
                break

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
    return int(importe_final)

def porc_envios_exteriores(cont_env_ext, cont_env):
    if cont_env != 0:
        porc = int((cont_env_ext * 100) / cont_env)
        return porc
    return 0

def prom_envios_bs_as(suma, cont_bs_as):
    if cont_bs_as != 0:
        prom = int(suma / cont_bs_as)
        return prom
    return 0

def principal():
    # Acceso al archivo
    archivo = open(ARCHIVO, encoding='windows-1252')
    cont_env_ext = cont_env = suma_precio_envio = cont_prov_bs_as = 0
    cedvalid = cedinvalid = imp_acu_total = ccs = ccc = cce = cant_primer_cp = porc = 0
    tipo_mayor = mencp = ''
    menimp = None
    # Lectura primer linea
    linea = archivo.readline()
    # Quitando el salto de linea
    linea_sin_final(linea)
    # Asignamos a r1 la funcion que determina el tipo de control
    control = get_tipo_control(linea)
    # Leemos la segunda linea
    linea = archivo.readline()
    # Extraccion de datos de la 1er linea de envios(segunda linea)
    linea_1 = extraer_datos(linea)
    # Extraer datos devuelve una tupla, y la posicion 0 corresponde al cp
    primer_cp = linea_1[0]
    # Recorremos linea por linea el archivo
    while linea != '':
        # Quitamos el salto de linea por cada linea recorrida
        linea_sin_final(linea)
        (cp, direccion, tipo, pago) = extraer_datos(linea)
        pais, provincia = obtener_pais(cp)
        precio_envio = calcular_precio(cp,tipo,pago)
        cont_env += 1
        if cp == primer_cp:
            cant_primer_cp += 1
        if control == 'Hard Control':
            if validar_direccion(direccion):
                cedvalid += 1
                imp_acu_total += precio_envio
                # Contador de tipos de carta
                if tipo_carta(tipo) == 'Carta Simple':
                    ccs += 1
                elif tipo_carta(tipo) == 'Carta Certificada':
                    ccc += 1
                elif tipo_carta(tipo) == 'Carta Expresa':
                    cce += 1
                if pais != 'Argentina':
                    cont_env_ext += 1
                if provincia == 'Provincia de Buenos Aires':
                    cont_prov_bs_as += 1
                    suma_precio_envio += precio_envio
            else:
                cedinvalid += 1
        if control == 'Soft Control':
            cedvalid += 1
            imp_acu_total += precio_envio
            if tipo_carta(tipo) == 'Carta Simple':
                ccs += 1
            elif tipo_carta(tipo) == 'Carta Certificada':
                ccc += 1
            elif tipo_carta(tipo) == 'Carta Expresa':
                cce += 1
            if pais != 'Argentina':
                cont_env_ext += 1
            if provincia == 'Provincia de Buenos Aires':
                cont_prov_bs_as += 1
                suma_precio_envio += precio_envio

        if pais == 'Brasil':
            # defino el menor importe pagado para envios a Brasil
            if menimp is None or precio_envio < menimp:
                menimp = precio_envio
                # r12
                mencp = cp
        linea = archivo.readline()
    # Defino el tipo de carta con mayor envio
    if ccs > ccc and ccs > cce:
        tipo_mayor = 'Carta Simple'
    elif ccc > ccs and ccc > cce:
        tipo_mayor = 'Carta Certificada'
    elif cce > ccs and cce > ccc:
        tipo_mayor = 'Carta Expresa'

    porc = porc_envios_exteriores(cont_env_ext, cont_env)
    prom = prom_envios_bs_as(suma_precio_envio, cont_prov_bs_as)

    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
    print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
    print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
    print(' (r5) - Cantidad de cartas simples:', ccs)
    print(' (r6) - Cantidad de cartas certificadas:', ccc)
    print(' (r7) - Cantidad de cartas expresas:', cce)
    print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
    print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
    print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
    print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
    print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
    print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
    print('(r14) - Importe final promedio de los envios a Buenos Aires:', prom)

principal()