class Juicio:

    def __init__(self,cod,desc,tipo,cte,hono):
        self.codigo = cod
        self.descripcion = desc
        self.tipo = tipo
        self.cliente = cte
        self.honorarios = hono

    def __str__(self):
        return 'Codigo de Expediente: ' + str(self.codigo) + \
            ' --- Descripcion: ' + self.descripcion + \
            ' --- Tipo: ' + str(self.tipo) + \
            ' --- Cliente: ' + self.cliente + \
            ' --- Honorarios: $' + str(self.honorarios)