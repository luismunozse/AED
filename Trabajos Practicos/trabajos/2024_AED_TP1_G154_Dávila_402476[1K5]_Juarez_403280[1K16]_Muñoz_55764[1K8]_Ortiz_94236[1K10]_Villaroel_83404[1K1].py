cp = input('Ingrese el CP de destino: ')
direccion = input('Ingrese la direccion fisica de destino: ')
tipo = int(input('Tipo de envio (entre 0 y 6): '))
pago = int(input('Forma de pago (1-Efectivo 2-Tarjeta): '))

provincia = 'No aplica'
importe_inicial = 0
importe_final = 0
montevideo = False

if len(cp) == 8 and (cp[0].isalpha() and cp[0] != 'I' and cp[0] != 'O') and cp[1:5].isdigit() and cp[5:8].isalpha():
    pais = 'Argentina'
    if cp[0] == 'A':
        provincia = 'Salta'
    elif cp[0] == 'B':
        provincia = 'Provincia de Buenos Aires'
    elif cp[0] == 'C':
        provincia = 'Ciudad Autónoma de Buenos Aires'
    elif cp[0] == 'D':
        provincia = 'San Luis'
    elif cp[0] == 'E':
        provincia = 'Entre Ríos'
    elif cp[0] == 'F':
        provincia = 'La Rioja'
    elif cp[0] == 'G':
        provincia = 'Santiago del Estero'
    elif cp[0] == 'H':
        provincia = 'Chaco'
    elif cp[0] == 'J':
        provincia = 'San Juan'
    elif cp[0] == 'K':
        provincia = 'Catamarca'
    elif cp[0] == 'L':
        provincia = 'La Pampa'
    elif cp[0] == 'M':
        provincia = 'Mendoza'
    elif cp[0] == 'N':
        provincia = 'Misiones'
    elif cp[0] == 'P':
        provincia = 'Formosa'
    elif cp[0] == 'Q':
        provincia = 'Neuquén'
    elif cp[0] == 'R':
        provincia = 'Rio Negro'
    elif cp[0] == 'S':
        provincia = 'Santa Fe'
    elif cp[0] == 'T':
        provincia = 'Tucuman'
    elif cp[0] == 'U':
        provincia = 'Chubut'
    elif cp[0] == 'V':
        provincia = 'Tierra del Fuego'
    elif cp[0] == 'W':
        provincia = 'Corrientes'
    elif cp[0] == 'X':
        provincia = 'Córdoba'
    elif cp[0] == 'Y':
        provincia = 'Jujuy'
    elif cp[0] == 'Z':
        provincia = 'Santa Cruz'
elif len(cp) == 4 and cp.isdigit():
    pais = 'Bolivia'
elif len(cp) == 9 and cp[0:5].isdigit() and cp[5] == '-' and cp[6:9]:
    pais = 'Brasil'
elif len(cp) == 7 and cp.isdigit():
    pais = 'Chile'
elif len(cp) == 6 and cp.isdigit():
    pais = 'Paraguay'
elif len(cp) == 5 and cp.isdigit():
    pais = 'Uruguay'
    if cp[0] == '1':
        montevideo = True
else:
    pais = 'Otro'


if tipo == 0:
    importe_inicial = 1100
elif tipo == 1:
    importe_inicial = 1800
elif tipo == 2:
    importe_inicial = 2450
elif tipo == 3:
    importe_inicial = 8300
elif tipo == 4:
    importe_inicial = 10900
elif tipo == 5:
    importe_inicial = 14300
elif tipo == 6:
    importe_inicial = 17900

if pais == 'Argentina':
    importe_inicial += 0
elif pais == 'Bolivia' or pais == 'Paraguay' or (pais == 'Uruguay' and montevideo == True):
    importe_inicial *= 1.2
elif pais == 'Chile' or (pais == 'Uruguay' and montevideo == False):
    importe_inicial *= 1.25
elif pais == 'Brasil' and (cp[0] == '8' or cp[0] == '9'):
    importe_inicial *= 1.2
elif pais == 'Brasil' and (cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3'):
    importe_inicial *= 1.25
elif pais == 'Brasil' and (cp[0] == '4' or cp[0] == '5' or cp[0] == '6' or cp[0] == '7'):
    importe_inicial *= 1.3
elif pais == 'Otro':
    importe_inicial *= 1.5

if pago == 1:
    importe_final = importe_inicial - (importe_inicial * 0.1)
elif pago == 2:
    importe_final = importe_inicial


print('Pais de destino: ' + pais)
print('Provincia: ' + provincia)
print('Importe inicial a pagar: ' + str(int(importe_inicial)))
print('Importe final a pagar: ' + str(int(importe_final)))


