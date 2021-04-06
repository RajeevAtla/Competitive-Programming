import math

def choose(n, k):
    # nCr function
    num = math.factorial(n)
    denom = math.factorial(k) * math.factorial(n-k)
    return num // denom

def power(n):
    #returns (1 + \sqrt{7})^n = \sum \limits_{k = 0}^{n} \left (\sqrt{7} \right)^{k} = a + b \sqrt{7}
    a, b = 0, 0
    for k in range(n+1):
        if k % 2 == 0:
            a += choose(n, k) * 7 ** (int(k/2))
        else:
            b += choose(n, k) * 7 ** (int(k/2 - 1/2))
    return a, b

def g(x):
    if x == 3:
        return 0
    n_found = False
    n = 1
    while(not n_found):
        a, b = power(n)
        if a % x == 1 and b % x == 0:
            n_found = True
            break
        else:
            n += 1
    return n

def G(N):
    sum = 0
    for i in range(2, N+1):
        sum += g(i)
    return sum

print(G(10**6))