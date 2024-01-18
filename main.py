from eredmenyek import *
import math

betolt('ub2017egyeni.txt')
print(f'3.2 feladat: Futók száma: {len(eredmenyek)}')
print(f'3.3 feladat: Célba érkező női sportolók: {versenyzok_szama_celban("Noi")} fő')
print('3.4 feladat: A leghosszabb nevű futó:')
leghosszabb_nevu_futó = leghosszabb_nevu()
print(f'\tNév: {leghosszabb_nevu_futó.Versenyzo}')
print(f'\tRajtszám: {leghosszabb_nevu_futó.Rajtszam}')
print(f'\tEredmény: {leghosszabb_nevu_futó.Versenyido}')

atlag = atlag_ido("Ferfi")
ora = math.floor(atlag)
perc = math.floor((atlag - ora) * 60)
mperc = math.floor((((atlag - ora) * 60) - perc) * 60)

atlag_mp = math.floor(atlag * 3600)
print(f'3.5 feladat: Férfi sportolók átlagos ideje: {atlag} óra ({atlag_mp} mp.)')
print(f'3.5 feladat: Férfi sportolók átlagos ideje: {ora}:{perc}:{mperc}')

mperc = str(atlag_mp % 60).zfill(2)
#perc = math.floor(atlag_mp / 60) % 60
#perc = int(atlag_mp / 60) % 60
perc = str((atlag_mp // 60) % 60).zfill(2)
ora = str(atlag_mp // 3600).rjust(2, '0')

print(f'{ora}:{perc}:{mperc}')
