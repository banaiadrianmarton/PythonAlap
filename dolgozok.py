from dolgozo import Dolgozo

dolgozok_listaja: list[Dolgozo] = []

def beolvas(filename):
    file = open(filename, 'r', encoding='utf8')
    for sor in file:
        dolgozok_listaja.append(Dolgozo(sor.strip()))
    file.close

def ceges_mobiltelefon():
    return len(dolgozok_listaja)

def keres(munkakor):
    darab = 0
    for d in dolgozok_listaja:
        if d.munkakor == munkakor:
            darab += 1
    return darab

def legkisebb_es_legnagyobb():
    legkisebb = dolgozok_listaja[0]
    legnagyobb = dolgozok_listaja[0]
    for d in dolgozok_listaja:
        if d.mobil_koltseg > legnagyobb.mobil_koltseg:
            legnagyobb = d
        if d.mobil_koltseg < legkisebb.mobil_koltseg:
            legkisebb = d
    return legkisebb.mobil_koltseg, legnagyobb.mobil_koltseg

def munkakor_osszeg(munkakor):
    munkakor_lista = []
    for d in dolgozok_listaja:
        if d.munkakor == munkakor:
            munkakor_lista.append(d.mobil_koltseg)
    return sum(munkakor_lista)


def osztalyok() -> dict[str, int]:
    stat : dict[str, int] = {}
    for d in dolgozok_listaja:
        if d.munkakor in stat.keys():
            stat[d.munkakor] += 1
        else:
            stat[d.munkakor] = 1
    return stat

def koltseg_csv(filename):
    file = open(filename, 'w', encoding='utf8')
    for d in dolgozok_listaja:
        if d.tullepte == True:
            file.write(f'{d.nev};{d.mobil_koltseg - d.kategoria_koltseg}\n')
    file.close()