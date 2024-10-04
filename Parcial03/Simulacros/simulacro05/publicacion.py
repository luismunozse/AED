class Publicacion:
    def __init__(self, id, titulo, tipo, costo):
        self.id = id
        self.titulo = titulo
        self.tipo = tipo
        self.costo = costo

    def __str__(self):
        return 'Cod Id: ' + self.id + \
            ' --- Titulo: ' + self.titulo + \
            ' --- Tipo: ' + str(self.tipo) + \
            ' --- Costo: $' + str(self.costo)