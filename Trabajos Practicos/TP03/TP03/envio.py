class Envio:
    def __init__(self, cp, dir, tipo, pago):
        self.codigo_postal = cp
        self.direccion = dir
        self.tipo_envio = tipo
        self.forma_pago = pago

    def __str__(self):
        return 'Código Postal: ' + self.codigo_postal + \
            'Dirección: ' + self.direccion + \
            'Tipo de Envío: ' + str(self.tipo_envio) + \
            'Forma de Pago: ' + str(self.forma_pago)

def crear_envio():
    cp = input('Ingrese código postal: ')
    dir = input('Ingrese dirección: ')
    tipo = int(input('Ingrese el tipo de envío: '))
    pago = int(input('Ingrese el tipo de pago: '))
    return Envio(cp, dir, tipo, pago)


def crear_envio_from_txt(linea):
    cp = linea[0:9].strip()
    dir = linea[9:29].strip()
    tipo = int(linea[29].strip())
    pago = int(linea[30].strip())
    return Envio(cp,dir,tipo,pago)