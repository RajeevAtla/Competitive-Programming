def algo(num):
    num = [str((int(x) + 1)) for x in num]

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    n = str(n)
    for i in range(m): algo(n)
    print(n)
