class Ticket:
    def __init__(self, cod: object, id: object, dest: object, but: object, imp: object):
        self.codigo_vuelo = cod
        self.identificador_pasajero = id
        self.pais_destino = dest
        self.nro_asiento = but
        self.importe = imp

    def __str__(self):
        return 'Codigo de vuelo: ' + self.codigo_vuelo + \
            ' Id de pasajero: ' + str(self.identificador_pasajero) + \
            ' Pais de destino: ' + str(self.pais_destino) + \
            ' Nro de asiento: ' + str(self.nro_asiento) + \
            ' Importe Pagado: $' + str(self.importe)
