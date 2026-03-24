stop = 15
n = int(input("Son kiriting: "))
if n > stop:
    print(f"{stop} gacha son kiriting")
else:
    for i in range(1, n + 1):
        print(i)