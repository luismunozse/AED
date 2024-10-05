import soporte


def contar(v):
    num = []
    cont = []
    for x in v:
        if x in num:
            i = num.index(x)
            cont[i] += 1
        else:
            num.append(x)
            cont.append(1)
    print(f'Cantidad de numeros diferentes: {len(num)}')
    return cont, num


def principal():
    v = soporte.vector_unknown_range(300000)
    contar(v)


if __name__ == '__main__':
    principal()
