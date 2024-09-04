class Obra:
    def __init__(self, nro, nom, hono, tipo):
        self.numero = nro
        self.nombre = nom
        self.honorarios = hono
        self.tipo = tipo

    def __str__(self):
        return 'Registro N°: ' + str(self.numero) + \
            'Nombre del Cliente: ' + self.nombre + \
            'Honorarios: ' + str(self.honorarios) + \
            'Tipo: ' + str(self.tipo)