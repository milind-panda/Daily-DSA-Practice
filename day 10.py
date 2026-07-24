n = 3

for i in range(1, n + 1):
    for j in range(i):
        if (i + j) % 2 == 1:
            print("0", end="")
        else:
            print("1", end="")
    print()







n = 5
num = 1

for i in range(0, n):
    for j in range(0, i + 1):
        print(num, end=" ")
        num += 1
    print()
