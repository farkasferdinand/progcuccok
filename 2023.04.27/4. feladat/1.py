print("1. feladat: Kisebb-nagyobb meghatározása")
elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem a második számot: "))

nagyobb=0
kisebb=0
if elso > masodik:
    nagyobb=elso
    kisebb=masodik
else:
    kisebb=elso
    nagyobb=masodik

print(f"A nagyobb szám {nagyobb}, a kisebb {kisebb}")
