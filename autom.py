from Auto import Auto


def fajl_beolvas():
    autok = []
    fajl = open("auto.txt", "r", encoding="utf-8")
    fajl.readline()
    lista = fajl.readlines()
    fajl.close()

    for i in range(0, len(lista), 1):
        sor_lista = lista[i].strip()
        sor_lista = sor_lista.split("$")

        auto = Auto(str(sor_lista[0]), int(sor_lista[1]))
        autok.append(auto)

    return autok


def tabla(lista, i):
    print("III/Tabla:")
    nev = lista[i - 1].nev
    return f"\t{nev}: {len(nev)} hosszú"


def kiiras(szoveg):
    fajl = open("kiir.txt", "w", encoding="utf-8")
    fajl.write("ki.txt\n")
    fajl.write(szoveg)
    fajl.close()


def flotta(lista):
    print("III/Flotta:")
    print(f"\tAutók száma: {len(lista)}")


def ertekes(lista):
    print("III/Értékes")
    hely = 0
    for i in range(1, len(lista), 1):
        if lista[i].datum > lista[hely].datum:
            hely = i

    print(f"\tA legfiatalabb autó: {lista[hely].nev}({lista[hely].datum})")
