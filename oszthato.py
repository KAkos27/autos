import random


def szam_gen():
    szam_lista = []
    for i in range(0, 50, 1):
        szam = random.randint(1, 101)
        szam_lista.append(szam)
    print("A lista elemei:")
    print(szam_lista)
    return szam_lista


def ottel_oszthato(lista):
    ossz: int = 0
    for i in range(0, len(lista), 1):
        if lista[i] % 5 == 0:
            ossz += 1

    return ossz
