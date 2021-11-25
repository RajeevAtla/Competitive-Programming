t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    if n == 1:
        print(0)
    elif k == 1:
        print(n-1)
    else:
        current = 1
        count = 0
        while current < n:
            if current <= k:
                current += current
            else:
                current += k
            count += 1
        print(count)
    
