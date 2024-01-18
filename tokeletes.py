def tokeletese(szam) -> bool:
    osszeg = 0
    for i in range(1, szam):
        if szam % i == 0:
            osszeg += i
    # if osszeg == szam:
    #     return True
    # else:
    #     return False
    return osszeg == szam

print('2. feladat: Tökéletes számok')
tól = int(input('tól = '))
ig = int(input('ig = '))

print(f'Tökéletes számok {tól} és {ig} között:')
# volt_tokeletes = False
# for i in range(tól, ig+1):
#     if tokeletese(i):
#         print(i, end='; ')
#         volt_tokeletes = True
# if not volt_tokeletes:
#     print('A megadott tartományban nincsen tökéletes szám!')

tokeletes_szamok = []
for i in range(tól, ig+1):
    if tokeletese(i):
        tokeletes_szamok.append(i)
if len(tokeletes_szamok) == 0:
    print('A megadott tartományban nincsen tökéletes szám!')
else:
    print(tokeletes_szamok)
