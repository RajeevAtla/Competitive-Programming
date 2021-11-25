def op(a):
    m = sum(a)/len(a)
    a = [i for i in a if i <= m]

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    min_count = a.count(min(a))

    print(len(a) - min_count)
