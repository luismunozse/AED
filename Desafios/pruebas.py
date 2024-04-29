ok = True
num = int(input('Cargue el primer valor (con 0 corta): '))
anterior = num

while num != 0:
    if num < anterior:
        ok = False
    else:
        ok = True
    anterior = num
    num = int(input('Cargue el siguiente valor (con 0 corta): '))

if ok == True:
    print('La secuencia está ordenada...')
else:
    print('La secuencia no está ordenada')