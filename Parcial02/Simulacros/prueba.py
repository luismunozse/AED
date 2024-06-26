# def es_vocal(car):
#     if car in 'aeiouAEIOU':
#         return True
#     return False
#
#
# def es_numero(car):
#     if car in '0123456789':
#         return True
#     return False
#
#
# def es_consonante(car):
#     if (car >='a' and car <= 'z') or (car >='A' and car <= 'Z'):
#         if not es_vocal(car) and not es_numero(car):
#             return True
#         return False
#
#
# def calcular_porcentaje(cant,total):
#     if total == 0:
#         return 0
#     return cant * 100 / total
#
#
# def principal():
#     print('Procesamiento de Texto')
#     texto = input('Ingrese texto(termina con punto para indicar fin de la frase):')
#     segunda_cons = es_pv = tiene_ga = False
#     menor_palabra_cons2 = None
#     vocales = letras_palabra = cont_palabras34 = palabras_vp_na = palabras_ga = total_palabras = 0 # contador de vocales
#     anterior = ''
#     for car in texto:
#         if car == ' ' or car == '.':
#             if letras_palabra > 0:
#                 total_palabras += 1
#         #
#         # por lo menos 3 vocales y mas de 4 letras
#             if vocales >= 3 and letras_palabra > 4:
#                 cont_palabras34 += 1
#         # verificar si tenia consonante en la segunda posicion
#             if segunda_cons:
#                 if menor_palabra_cons2 is None or letras_palabra < menor_palabra_cons2:
#                     menor_palabra_cons2 = letras_palabra
#             # preguntar si empieza con p o v y termina con n o a
#             if anterior in 'aAnN' and es_pv:
#                 palabras_vp_na += 1
#             if tiene_ga:
#                 palabras_ga += 1
#         # reiniciar contador de palabras
#             letras_palabra = vocales = 0
#             segunda_cons = es_pv = tiene_ga = False
#         else:
#             # contar letras de la palabra
#             letras_palabra += 1
#             # contar vocales
#             if es_vocal(car):
#                 vocales += 1
#             #  detectar consonante en la segunda posicion
#             if es_consonante(car) and letras_palabra == 2:
#                 segunda_cons = True
#             # comienza con p o v
#             if (car in 'pPvV') and letras_palabra == 1:
#                 es_pv = True
#             if (car == 'a' or car == 'A') and (anterior == 'g' or anterior == 'G'):
#                 tiene_ga = True
#         anterior = car
#     print(f'Palabras que tienen al menos 3 vocales y mas de 4 letras: {cont_palabras34}')
#     if menor_palabra_cons2 is not None:
#         print(f'Longitud de la palabra mas corta de entre las que contenian una consonante en la segunda posicion: {menor_palabra_cons2}')
#     else:
#         print('No se encuentran palabras con consonante en la segunda posicion')
#     print(f'Palabras que empiezan con V o P y terminan con N y A: {palabras_vp_na}')
#     print(f'Porcentajes de palabras con la expresion ga sobre el total de palabras del texto: {calcular_porcentaje(palabras_ga,total_palabras)}%')
#
# if __name__ == '__main__':
#     principal()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
