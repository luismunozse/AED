# def es_digito_impar(car):
#     return car in '13579'
#
#
# def es_consonante_mayuscula(car):
#     return car in 'BCDFGHJKLMNÑPQRSTVWXYZ'
#
#
# def es_vocal(car):
#     return car.lower() in 'aeiouáéíóúü'
#
#
# def porcentaje(total,parcial):
#     if total != 0:
#         return (parcial * 100) // total
#
#
# def principal():
#     r1 = r3 = r4 = 0
#     cl = cdi = ccm = cla = cle = cp = cpae = csdi = 0
#     inivoc = sd = False
#     r2 = None
#     anterior = ''
#     # archivo = open('entrada.txt')
#     # texto = archivo.read()
#     # archivo.close()
#     # TEXTO PUNTO 1
#     # texto = 'El lugar marcado como X31F57 es conocido tambien como X23A54.'
#     # TEXTO PUNTO 2
#     # texto = 'Antes de esa esperada circunstancia era imposible.'
#     # TEXTO PUNTO 3
#     # texto = 'Las esperas nunca acaban.'
#     # TEXTO PUNTO 4
#     texto = 'Didide didida dijo el cantor.'
#
#     for car in texto:
#         if car == ' ' or car == '.':
#             # fin de palabra
#             # procesar la palabra solo si el contador de letras era mayor a cero
#             if cl > 0:
#                 # contar palabras
#                 cp += 1
#                 # Resultado r1
#                 if cl == cdi + ccm:
#                     r1 += 1
#                 # Resultado r2
#                 if inivoc:
#                     if r2 is None or cl < r2:
#                         r2 = cl
#                 # Resultado r3
#                 if cla > cle:
#                     cpae += 1
#                 # Resultado r4
#                 if csdi >= 2 and es_vocal(anterior):
#                     r4 += 1
#             # Resetear contadores y banderas
#             cl = 0
#             # contadores para r1
#             cdi = ccm = 0
#             # banderas para r2
#             inivoc = False
#             # contadores para r3
#             cla = cle = 0
#             # contadores para r3
#             sd = False
#             csdi = 0
#         else:
#             # dentro de la palabra
#             # contar todos los caracteres de la palabra actual
#             cl += 1
#
#             # Resultado r1
#             if es_digito_impar(car):
#                 cdi += 1
#             elif es_consonante_mayuscula(car):
#                 ccm += 1
#
#             # Resultado r2
#             if cl == 1 and es_vocal(car):
#                 inivoc = True
#
#             # Resultado r3
#             if car in 'aáAÁ':
#                 cla += 1
#             elif car in 'eéEÉ':
#                 cle += 1
#
#             # Resultado r4
#             if car in 'dD':
#                 sd = True
#             else:
#                 if sd and car in 'iíIÍ':
#                     csdi += 1
#                 sd = False
#             anterior = car
#     r3 = porcentaje(cp,cpae)
#     print("Primer resultado:", r1)
#     print("Segundo resultado:", r2)
#     print("Tercer resultado:", r3)
#     print("Cuarto resultado:", r4)
#
#
# if __name__ == '__main__':
#     principal()