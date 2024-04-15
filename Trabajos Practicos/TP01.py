print('*****************************Datos de envio*****************************: ')

cp = input('Ingrese el CP de destino: ')
dir = input('Ingrese la direccion fisica de destino: ')
tipo = int(input('Tipo de envio (entre 0 y 6): '))
pago = int(input('Forma de pago (1-Efectivo 2-Tarjeta): '))

pais = ''

provincia = ('Salta', 'Buenos Aires', 'Capital Federal', 'San Luis', 'Entre Rios', 'La Rioja', 'Santiago del Estero', 'Chaco', 'San Juan','Catamarca', 'La Pampa', 'Mendoza', 'Misiones', 'Formosa', 'Neuquen', 'Rio Negro', 'Santa Fe', 'Tucuman', 'Chubut', 'Tierra del Fuego', 'Corrientes','Cordoba', 'Jujuy', 'Santa Cruz')

(A,B,C,D,E,F,G,H,J,K,L,M,N,P,Q,R,S,T,U,V,W,X,Y,Z) = provincia

if(len(cp)==8):
    pais = 'Argentina'
    if(tipo==0):
        precio = 1100
    else:
        if(tipo==1):
            precio = 1800
        else:
            if(tipo==2):
                precio = 2450
            else:
                if(tipo==3):
                    precio = 8300
                else:
                    if(tipo==4):
                        precio = 10900
                    else:
                        if(tipo==5):
                            precio = 14300
                        else:
                            if(tipo==6):
                                precio = 17900
else:
    if(len(cp)==4):
        pais = 'Bolivia'
    else:
        if(len(cp)==9 and cp[5]=='-'):
            pais = 'Brasil'
        else:
            if(len(cp)==7):
                pais='Chile'
            else:
                if(len(cp)==6):
                    pais = 'Paraguay'
                else:
                    if(len(cp)==5):
                        pais = 'Uruguay'
                    else: 
                        pais = 'Otros'


