def belepes():
    fh_nev: str = str(input("Adja meg a felhasználónevét! "))
    jsz: str = str(input("Adja meg a jelszavát! "))

    while fh_nev != "bori99" and jsz != "Szivecske>3":
        print("Belépés megtagadva.")
        fh_nev: str = str(input("Adja meg a felhasználónevét! "))
        jsz: str = str(input("Adja meg a jelszavát! "))

    print("Belépés engedélyezve")
        

