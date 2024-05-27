# Desarrollar un programa en Python que permita cargar por teclado un texto
# completo (analizar dos opciones: una es cargar todo el texto en una variable de tipo cadena
# de caracteres y recorrerla con un for iterador; y la otra es cargar cada caracter uno por uno a
# través de un while). Siempre se supone que el usuario cargará un punto para indicar el final
# del texto, y que cada palabra de ese texto está separada de las demás por un espacio en
# blanco. El programa debe:
# a. Determinar cuántas palabras se cargaron.
# b. Determinar cuántas palabras comenzaron con la letra "p".
# c. Determinar cuántas palabras contuvieron una o más veces la expresión "ta"

# Contadores
cont_palabra = cont_palabra_p = cont_palabra_ta = cont_letra = 0

# Flags
es_t = False
es_a = False

# Cadena de texto
cadena = input('Ingrese un texto (termina con punto) : ')

# Iteracion de la cadena de caracteres (recorre un caracter o letra por vuelta)
for letra in cadena:
    # Contador de letras (suma uno cada vuelta)
    cont_letra += 1
    # Si en alguna de las vueltas letra es un espacio o un punto se indica el final de la palabra
    if letra == ' ' or letra == '.':
        # El final de la palabra indica que el contador de letras vuelva a 0
        cont_letra = 0
        # El final de la palabra indica que el contador de palabra incremente en 1 cada vez que eso se cumpla
        cont_palabra += 1
        #
        es_t = False
    else:
        # En la rama falsa buscamos la(s) palabra(s) que empiece(n) con p
        if letra == 'p' and cont_letra == 1:
            cont_palabra_p += 1
        # Si la palabra contiene la letra t y la bandera que indica que la letra a fue la ultima en recorrerse es falsa
        if letra == 't' and not es_a:
            # Habilitamos la bandera de t
            es_t = True
        else:
            # Si la letra recorrida es la "a" y la bandera de t esta activa
            if letra == 'a' and es_t:
                # Bandera de "a" se habilita ya que se encontro la letra "a"
                es_a = True
                # Contamos la silaba "ta" consecuencia de lo anterior
                cont_palabra_ta += 1
            # Establecemos en falso la bandera de "t" ya que estamos en la rama falsa
            es_t = False

# Salidas
print(f'Cantidad total de palabras: {cont_palabra}')
print(f'Palabras que empiezan con p: {cont_palabra_p}')
print(f'Palabras que contienen "ta": {cont_palabra_ta}')
