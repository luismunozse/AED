class Servicio:
    def __init__(self, codigo, cliente, tipo, importe):
        self.codigo = codigo
        self.cliente = cliente
        self.tipo = tipo
        self.importe = importe


    def __str__(self):
        return 'Código Identificatorio: ' + str(self.codigo) + \
            ' | Nombre del Cliente: ' + self.cliente + \
            ' | Tipo de Servicio Prestado: ' + str(self.tipo) + \
            ' | Importe mensual: $' + str(self.importe)