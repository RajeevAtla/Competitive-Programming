t = int(input())
for i in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    s = 0
    for i in range(n):
        if r[i] == 1: s += 1
        elif r[i] == 3: s += 1
    print(s)