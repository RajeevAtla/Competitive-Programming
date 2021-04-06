def g(x):
    result = 1
    for i in range(1, x):
        if not(x % i == 0):
            result *= i
    return result

def G(n):
    result = 1
    for i in range(1, n + 1):
        result *= g(i)
    return result

print(g(10))