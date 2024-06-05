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


def obtener_direccion(linea):
    _,direccion,_,_ = extraer_datos(linea)
    return direccion



def validar_direccion_hc(direccion):
    print(direccion)
    for car in direccion:
        if not (car.isalpha() or car.isdigit() or car == ' ' or car == '.'):
            return False
    return True

def principal():
    archivo = open(ARCHIVO, encoding='UTF-8')
    r2 = r3 = 0
    linea = archivo.readline()
    linea = linea_sin_final(linea)
    tipo_control = get_tipo_control(linea)
    print(tipo_control)
    linea = archivo.readline()
    while linea != '':

        linea_sin_final(linea)
        (cp, direccion, tipo, pago) = extraer_datos(linea)
        print(f'Código Postal: {cp} | Dirección: {direccion} | Tipo de Envío: {tipo} | Forma de Pago: {pago}')

        if validar_direccion_hc(direccion):
            r2 += 1
        else:
            print(f'Dirección inválida: {direccion}')
            r3 += 1
        linea = archivo.readline()
    print(r2,r3)

principal()