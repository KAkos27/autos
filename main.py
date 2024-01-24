import jelszo
import oszthato
import autom

jelszo.belepes()

lista = oszthato.szam_gen()
ottel_oszt = oszthato.ottel_oszthato(lista)
print(f"A listában {ottel_oszt}db öttel osztható szám van")

auto_lista = autom.fajl_beolvas()
szoveg = autom.tabla(auto_lista, 2)
print(szoveg)
autom.kiiras(szoveg)
autom.flotta(auto_lista)
autom.ertekes(auto_lista)