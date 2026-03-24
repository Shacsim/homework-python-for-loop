start = int(input("Boshlang'ich qiymatni kiriting: "))
stop = int(input("Tugash qiymatini kiriting: "))

if start > stop:
    for i in range(start, stop - 1, -1):
        print(i)
else:
    for i in range(start, stop + 1):
        print(i)
