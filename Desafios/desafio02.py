
n = int(input('Ingrese un número: '))

orbita = 0
longitud = 1
mayor = None
suma_prom = n

if n > 0:
    print(n)
    while n != 1:
        if n % 2 != 0:
            orbita = (3*n) + 1
            n = orbita
        else:
            orbita = n // 2
            n = orbita
        if mayor is None or n > mayor:
            mayor = n
        suma_prom += n
        longitud += 1
        print(n)

    print(f'Longitud: {longitud}')
    promedio = suma_prom / longitud
    print(f'Promedio sin redondeo: {promedio}')
    print(f'Promedio: {round(promedio,1)}')
    print(f'Mayor: {mayor}')

else:
    print('No se aceptan números negativos')

