from epulet import Epulet

epuletek : list[Epulet] = []

def beolvas(filename):
    file = open(filename, 'r', encoding='utf8')
    file.readline()
    for sor in file:
        epuletek.append(Epulet(sor.strip()))
    file.close()

#Milyen magas a legmagasabb épület? egyetlen szám az eredmény.
def legmagasabb():
    maximum_magassag = epuletek[0].magassag
    for e in epuletek:
        if e.magassag > maximum_magassag:
            maximum_magassag = e.magassag
    return maximum_magassag

#Melyik épület a legmagasabb? Írjuk ki több adatát is!
#V1 vagy az Epulet osztálypéldányt adok vissza
def legmagasabb_epulet() -> Epulet:
    legmagasabb = epuletek[0]
    for e in epuletek:
        if e.magassag > legmagasabb.magassag:
            legmagasabb = e
    return legmagasabb
#V2 vagy egy indexet adok vissza: az epulet sorszamat a listaban
def legmagasabb_epulet_index():
    legmagasabb_epulet_indexe = 0
    for index, e in  enumerate(epuletek):
        if epuletek[index].magassag > epuletek[legmagasabb_epulet_indexe].magassag:
            legmagasabb_epulet_indexe = index
    return legmagasabb_epulet_indexe


#Ha több legmagasabb is lehetséges
def legmagasabbak():
    legmagasabbak_listaja = []
    for e in epuletek:
        if e.magassag == legmagasabb():
            legmagasabbak_listaja.append(e)
    return legmagasabbak_listaja

#Ha nem az összes épületet kell vizsgálni
#Pl. Melyik a legmagasabb francia épület?
#nem tehetem bele az első elemet a max változómba!
def legmagasabb_epulet_adott_orszagban(orszag):
    legnagyobb_magassag = -10
    legmagasabb_epulet = None
    for e in epuletek:
        if e.orszag == orszag and e.magassag > legnagyobb_magassag:
            legnagyobb_magassag = e.magassag
            legmagasabb_epulet = e
    return legmagasabb_epulet