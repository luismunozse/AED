class Trabajo:
    def __init__(self, id, desc, tipo, imp, cant):
        self.identificador = id
        self. descripcion = desc
        self.tipo = tipo
        self.importe = imp
        self.cantidad = cant

    def __str__(self):
        return 'Identificador de Trabajo: ' + str(self.identificador) + \
            ' Descripcion: ' + self.descripcion + \
            ' Tipo de trabajo: ' + str(self.tipo) + \
            ' Importe a pagar: ' + str(self.importe) + \
            ' Cantidad de trabajadores: ' + str(self.cantidad)