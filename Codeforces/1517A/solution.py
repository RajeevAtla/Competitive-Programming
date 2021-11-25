def k(x):
    for i in range(1, 15):
        if x < 2050 * 10 ** i:
            return i-1

T = int(input())

for i in range(T):
    n = int(input())
    ans = 0
    if n in [2050 * 10 ** k for k in range(0, 15)]:
        print(1)
    else:
        while(n > 0):
            n -= 2050 * 10 ** k(n)
            ans += 1

        if n == 0:
            print(ans)
        else:
            print(-1)