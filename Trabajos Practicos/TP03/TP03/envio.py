class Envio:
    def __init__(self, cp, dire, tipo, pago):
        self.codigo_postal = cp
        self.direccion = dire
        self.tipo_envio = tipo
        self.forma_pago = pago

    def __str__(self):
        return 'Código Postal: ' + self.codigo_postal + \
            'Dirección: ' + self.direccion + \
            'Tipo de Envío: ' + str(self.tipo_envio) + \
            'Forma de Pago: ' + str(self.forma_pago)


# def crear_envio():
#     cp = input('Ingrese código postal: ')
#     dire = input('Ingrese dirección: ')
#     tipo = int(input('Ingrese el tipo de envío: '))
#     pago = int(input('Ingrese el tipo de pago: '))
#     return Envio(cp, dire, tipo, pago)


def crear_envio():
    cp = input('Ingrese código postal: ')
    dire = input('Ingrese dirección: ')
    tipo = int(input('Ingrese el tipo de envío: '))
    while tipo not in [0, 1, 2, 3, 4, 5, 6]:
        print("Ingrese un número entre 0 y 6:")
        tipo = int(input('Ingrese el tipo de envío: '))
    pago = int(input('Ingrese el tipo de pago: '))
    while pago not in [1, 2]:
        print("Ingrese 1 o 2 (efectivo o tarjeta):")
        pago = int(input('Ingrese el tipo de envío: '))
    return Envio(cp, dire, tipo, pago)


def crear_envio_from_txt(linea):
    cp = linea[0:9].strip()
    dire = linea[9:29].strip()
    tipo = int(linea[29].strip())
    pago = int(linea[30].strip())
    return Envio(cp,dire,tipo,pago)


def obtener_pais(cp):
    n = len(cp)
    if n < 4 or n > 9:
        return 'Otro'
    if n == 8:
        if cp[0].isalpha() and cp[0] not in 'IO' and cp[1:5].isdigit() and cp[5:8].isalpha():
            return 'Argentina'
        return 'Otro'
    if n == 9:
        if cp[0:5].isdigit() and cp[5] == '-' and cp[6:9].isdigit():
            return 'Brasil'
        return 'Otro'
    if cp.isdigit():
        if n == 4:
            return 'Bolivia'
        elif n == 7:
            return 'Chile'
        elif n == 6:
            return 'Paraguay'
        elif n == 5:
            return 'Uruguay'
    return 'Otro'


def calcular_precio_envio(cp,pais,tipo,pago):
    importes = [1100,1800,2450,8300,10900,14300,17900]
    precio = importes[tipo]
    if pais == 'Argentina':
        precio_final = precio
    else:
        if pais == 'Bolivia' or pais == 'Paraguay' or (pais == 'Uruguay' and cp[0] == '1'):
            precio_final = int(precio * 1.2)
        elif pais == 'Chile' or (pais == 'Uruguay' and cp[0] != '1'):
            precio_final = int(precio * 1.25)
        elif pais == 'Brasil':
            if cp[0] == '8' or cp[0] == '9':
                precio_final = int(precio * 1.2)
            else:
                if cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
                    precio_final = int(precio * 1.25)
                else:
                    precio_final = int(precio * 1.3)
        else:
            precio_final = int(precio * 1.5)
    if pago == 1:
        precio_final = int(precio_final - (precio_final * 0.1))
    elif pago == 2:
        precio_final = int(precio_final)
    return precio_final


def validar_direccion(direccion):
    cl = cd = 0
    td = False
    ant = " "
    for car in direccion:
        if car in " .":
            if cl == cd:
                td = True
            cl = cd = 0
            ant = " "
        else:
            cl += 1
            if not car.isdigit() and not car.isalpha():
                return False
            if ant.isupper() and car.isupper():
                return False
            if car.isdigit():
                cd += 1
            ant = car

    return td