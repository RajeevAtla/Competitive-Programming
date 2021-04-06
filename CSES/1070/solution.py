n = int(input())

if n == 1: 
    print(1)
    exit()
elif n == 2 or n ==3:
    print("NO SOLUTION")
    exit()
elif n == 4:
    print("3 1 4 2")
else:
    s = [*range(1, n + 1, 2), *range(2, n + 1, 2)]
    s1 = ""
    for i in s: 
        s1 += str(i) + " "
    s1.rstrip()
    print(s1)

