t = int(input())
for i in range(t):
    n = list(input())
    n = list(map(int, n))
    print(min(n) if len(n) > 2 else n[-1])
