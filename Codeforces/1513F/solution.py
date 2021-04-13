def value(x, y):
    return sum([abs(x[i] - y[i]) for i in range(len(x))])

def swap(x, y):
    temp = b_copy[x]
    b_copy[x] = b_copy[y]
    b_copy[y] = temp

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if value(a, b) == 0:
    print(0)
    exit()

val = value(a, b)
b_copy = b
min = val

for i in range(n):
    for j in range(1, n-1):
        swap(i, j)
        val = value(a, b)
        if val < min: min = val
        b_copy = b

print(min)