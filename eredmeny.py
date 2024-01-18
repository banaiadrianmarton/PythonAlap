class Eredmény:
    def __init__(self, sor) -> None:
        adatok = sor.split(';')
        
        self.Versenyzo = adatok[0]
        self.Rajtszam = int(adatok[1])
        self.Kategoria = adatok[2]
        self.Versenyido = adatok[3]
        self.TavSzazalek = int(adatok[4])

        ido_adatok = self.Versenyido.split(':')
        self.Ido_oraban = int(ido_adatok[0]) + int(ido_adatok[1])/60 + int(ido_adatok[2]) / 3600 