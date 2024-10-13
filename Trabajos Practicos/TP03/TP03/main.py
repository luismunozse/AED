import envio as objEnvio

file = 'envios-tp3.txt'


def mostrar_envios(envios):
    if len(envios) == 0:
        print('No hay envios cargados')
    else:
        for envio in envios:
            print(envio)


def tipo_control():
    m = open(file, 'rt')
    linea = m.readline().strip()
    if 'HC' in linea:
        return 'HC'
    elif 'SC' in linea:
        return 'SC'
    return 'HC'


def cargar_envios_archivo(file, envios):
    if len(envios) > 0:
        confirmacion = input(
            'Ya existen envios cargados. ¿Desea eliminar los datos actuales y cargar nuevos envios? (s/n)')
        if confirmacion == 's':
            envios.clear()
        elif confirmacion == 'n':
            print('Operacion cancelada.')
            return
        else:
            print('Elija s o n porfavor.')
            return
    m = open(file, 'rt')
    nro_linea = 0
    for linea in m:
        nro_linea += 1
        if nro_linea == 1:
            continue
        if linea[-1] == '\n':
            linea = linea[:-1]
        if linea != '':
            envio = objEnvio.crear_envio_from_txt(linea)
            envios.append(envio)
    m.close()
    print('Envios cargados.....')


def generar_envios(envios):
    n = int(input('Ingrese la cantidad de envios a generar: '))
    for i in range(n):
        envio = objEnvio.crear_envio()
        if envio:
            envios.append(envio)
    print('Envios generados.....')


def ordenar_envios(envios):
    n = len(envios)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if envios[i].codigo_postal > envios[j].codigo_postal:
                envios[i], envios[j] = envios[j], envios[i]


def mostrar_envios_ordenados(envios):
    ordenar_envios(envios)
    if len(envios) == 0:
        print('No hay envios cargados')
    else:
        mostrar_todos = input('¿Desea mostrar todos los envios? (s/n): ')
        if mostrar_todos == 'n':
            m = int(input('Ingrese la cantidad de envios que desea mostrar: '))
            envios_a_mostrar = envios[:m]
        else:
            envios_a_mostrar = envios
        for envio in envios_a_mostrar:
            pais = objEnvio.obtener_pais(envio.codigo_postal)
            print(f'Codigo Postal: {envio.codigo_postal}, Dirección: {envio.direccion},'
                  f'Tipo de Envio: {envio.tipo_envio}, Forma de Pago: {envio.forma_pago}, Pais: {pais}')


def buscar_envios_d_e(envios):
    d = input('Ingrese la direccion a buscar: ').strip().lower()
    e = int(input('Ingrese el tipo de envio a buscar: '))
    n = len(envios)
    for i in range(n):
        if envios[i].direccion.strip().lower() == d and envios[i].tipo_envio == e:
            return i
    return -1


def buscar_envios_cp(envios):
    cp = input('Ingrese el codigo postal a buscar: ')
    n = len(envios)
    for i in range(n):
        if envios[i].codigo_postal == cp:
            return i
    return -1


def contar_envios_por_tipo(envios):
    conteo_tipos = [0] * 7
    control = tipo_control()
    for envio in envios:
        if control == 'HC' and objEnvio.validar_direccion(envio.direccion):
            conteo_tipos[envio.tipo_envio] += 1
        elif control == 'SC':
            conteo_tipos[envio.tipo_envio] += 1
    for i in range(len(conteo_tipos)):
        print(f'Cantidad de envios de tipo {i}: {conteo_tipos[i]}')


def contar_importes_finales(envios):
    conteo_importes_finales = [0] * 7
    control = tipo_control()
    for envio in envios:
        pais = objEnvio.obtener_pais(envio.codigo_postal)
        precio_envio = objEnvio.calcular_precio_envio(envio.codigo_postal, pais, envio.tipo_envio, envio.forma_pago)
        if control == 'HC' and objEnvio.validar_direccion(envio.direccion):
            conteo_importes_finales[envio.tipo_envio] += precio_envio
        elif control == 'SC':
            conteo_importes_finales[envio.tipo_envio] += precio_envio
    for i in range(len(conteo_importes_finales)):
        print(f'Importe acumulado para el tipo de envio {i}: ${conteo_importes_finales[i]}')
    return conteo_importes_finales


def mostrar_tipo_envio_mayor_importe(conteo_importes_finales):
    if not conteo_importes_finales:
        print('No se ha calculado el importe final acumulado. Primero ejecuta la opción 7')
        return
    total_importe = 0
    for importe in conteo_importes_finales:
        total_importe += importe
    if total_importe == 0:
        print('No hay importes acumulados')
        return
    mayor_importe = conteo_importes_finales[0]
    tipo_mayor = 0
    for i in range(1, len(conteo_importes_finales)):
        if conteo_importes_finales[i] > mayor_importe:
            mayor_importe = conteo_importes_finales[i]
            tipo_mayor = i
    porcentaje = (mayor_importe/total_importe) * 100
    porcentaje = round(porcentaje,2)
    print(f'Tipo de envio con mayor importe acumulado: {tipo_mayor}')
    print(f'Importe final acumulado: ${mayor_importe}')
    print(f'Porcentaje sobre el monto total: {porcentaje}%')



def mostrar_importe_final_promedio(envios):
    if not envios:
        print('Cargue envios porfavor')
        return
    total_importe = 0
    cont_importes_menores = 0
    for envio in envios:
        pais = objEnvio.obtener_pais(envio.codigo_postal)
        precio_envio = objEnvio.calcular_precio_envio(envio.codigo_postal, pais, envio.tipo_envio, envio.forma_pago)
        total_importe += precio_envio
    cantidad_envios = len(envios)
    importe_promedio = total_importe/cantidad_envios
    for envio in envios:
        pais = objEnvio.obtener_pais(envio.codigo_postal)
        precio_envio = objEnvio.calcular_precio_envio(envio.codigo_postal, pais, envio.tipo_envio, envio.forma_pago)
        if precio_envio < importe_promedio:
            cont_importes_menores +=1
    print(f'Importe final promedio: ${importe_promedio}')
    print(f'Cantidad de envios con importes menores al promedio: {cont_importes_menores}')

def principal():

    envios = []
    conteo_importes_finales = []
    opcion = -1

    while opcion != 10:

        print('Menú de Opciones: ')
        print('************************')
        print('1 - Crear arreglo de envios a partir de un archivo de texto')
        print('2 - Cargar por teclado los datos de un envio')
        print('3 - Mostrar envios por código postal')
        print('4 - Buscar por dirección y tipo de envío')
        print('5 - Buscar por codigo postal')
        print('6 - Contar envios según el tipo de control de direcciones (HC o SC)')
        print('7 - Contar importes finales acumulados segun el tipo de control ')
        print('8 - Mostrar el tipo de envio con mayor importe final acumulado')
        print('9 - Mostrar el importe final promedio de todos los envios')
        print('10 - Salir')
        print()

        opcion = int(input('Ingrese su opción: '))

        if opcion == 1:
            cargar_envios_archivo(file, envios)
        elif opcion == 2:
            generar_envios(envios)
        elif opcion == 3:
            mostrar_envios_ordenados(envios)
        elif opcion == 4:
            pos4 = buscar_envios_d_e(envios)
            if pos4 != -1:
                print('Envio encontrado...')
                print(envios[pos4])
            else:
                print('No se encuentran envios para la búsqueda')
        elif opcion == 5:
            pos5 = buscar_envios_cp(envios)
            if pos5 != -1:
                print('Envio encontrado...')
                if envios[pos5].forma_pago == 1:
                    envios[pos5].forma_pago = 2
                elif envios[pos5].forma_pago == 2:
                    envios[pos5].forma_pago = 1
                print('Registro Modificado ...')
                print(envios[pos5])
            else:
                print('No se encuentran envios para la búsqueda')
        elif opcion == 6:
            contar_envios_por_tipo(envios)
        elif opcion == 7:
            conteo_importes_finales = contar_importes_finales(envios)
        elif opcion == 8:
            print(conteo_importes_finales)
            mostrar_tipo_envio_mayor_importe(conteo_importes_finales)
        elif opcion == 9:
            mostrar_importe_final_promedio(envios)
        elif opcion == 10:
            print('Gracias por usar nuestro software')


if __name__ == '__main__':
    principal()
