class Orszag:
    def __init__(self, sor:str):
        adatok = sor.strip().split(";")
        self.orszag = adatok[0]
        self.csatlakozas = adatok[1]

orszagok:list[Orszag] = []

f = open("EUcsatlakozas.txt", "r", encoding="UTF-8")
for sor in f:
    orszagok.append(Orszag(sor))
f.close()

print(f"3.feladat: tagállam: {len(orszagok)} db")

csatlakozott= 0
for item in orszagok:
    datum = item.csatlakozas.split(".")
    if datum[0] == "2007":
        csatlakozott += 1

print(f"4.feladat: 2007-ben {csatlakozott} ország csatlakozott")

for item in orszagok:
    if item.orszag == "Magyarország":
        print(f"5.feladat: Magyarország csatlakozása: {item.csatlakozas}")
        break

volte = False
for item in orszagok:
    datum = item.csatlakozas.split(".")
    if datum[1] == "05":
        volte = True

if volte == True:
    print(f"6.feladat: Májusban volt csatlakozás!")
else:
    print(f"6.feladat: Nem volt májusban csatlakozás!")

stat = {}
for item in orszagok:
    datum = item.csatlakozas.split(".")
    if datum[0] in stat.keys():
        stat[datum[0]] += 1
    else:
        stat[datum[0]] = 1

print("8. feladat: Statisztika")
for key, value in stat.items():
    print(f"\t{key} - {value} ország")