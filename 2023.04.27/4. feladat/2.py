first = int(input(f"Kérem az egyik évszámot: "))
second = int(input(f"Kérem a második évszámot: "))

years = []
for i in range(first, second + 1):
    if i % 400 == 0:
        years.append(i)
    elif i % 4 == 0 and not i % 100 == 0:    
        years.append(i) 
print(years)