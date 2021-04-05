def subtract(x):
    if(x % 10 == 0): return int(x/10)
    else: return x-1

n, k = map(int, input().split())

for i in range(k):
    n = subtract(n)

print(n)