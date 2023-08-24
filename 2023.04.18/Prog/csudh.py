class Cim:
    def __init__(self, sor:str):
        data = sor.strip().split(";")
        self.domain = data[0]
        self.ip = data[1]

cimek:list[Cim] = []

f = open("csudh.txt", "r", encoding="utf-8")
f.readline()
for sor in f:
    cimek.append(Cim(sor))
f.close

print(f"3. feladat: Domainek száma: {len(cimek)}")


def domain(domain:str, level:int):
    data = domain.split(".")
    for i in range(level):
        if data[level] == None:
            return "nincs"
        else:
            return data[level]
