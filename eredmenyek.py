from eredmeny import Eredmény

eredmenyek : list[Eredmény] = []

def betolt(fajlnev: str) -> None:
    file = open(fajlnev, 'r', encoding='utf-8')
    file.readline()
    for sor in file:
        eredmenyek.append(Eredmény(sor.strip()))
    file.close()

def versenyzok_szama_celban(kategoria: str) -> int:
    darab = 0
    for e in eredmenyek:
        if e.Kategoria == kategoria and e.TavSzazalek == 100:
            darab += 1
    return darab

def leghosszabb_nevu() -> Eredmény:
    leghosszabb = eredmenyek[0]
    for e in eredmenyek:
        if len(e.Versenyzo) > len(leghosszabb.Versenyzo):
            leghosszabb = e
    return leghosszabb

def atlag_ido(kategoria: str) -> float:
    osszeg = 0
    darab = 0
    for e in eredmenyek:
        if e.Kategoria == kategoria and e.TavSzazalek == 100:
            osszeg += e.Ido_oraban
            darab += 1
    return osszeg / darab
    