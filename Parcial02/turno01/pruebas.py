def principal():

    archivo = open('entrada.txt')
    texto = archivo.read()
    archivo.close()

    r1 = r2 = r3 = r4 = 0

    for car in texto:
        if car == ' ' or car == '.':
            pass
        else:
            pass

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()