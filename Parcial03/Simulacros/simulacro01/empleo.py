class Empleo:
    def __init__(self, id, desc, tipo, sueldo):
        self.identificador = id
        self.descripcion = desc
        self.tipo = tipo
        self.sueldo = sueldo

    def __str__(self):
        return 'Id Empleo: ' + str(self.identificador) + \
            ' Descripcion: ' + self.descripcion + \
            ' Tipo: ' + str(self.tipo) + \
            ' Sueldo: $' + str(self.sueldo)



