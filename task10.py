n = int(input("Son kiriting: "))
fakt = 1
for i in range(1, n+1):
    fakt = fakt * i
    print(f"{i}! = {fakt}")