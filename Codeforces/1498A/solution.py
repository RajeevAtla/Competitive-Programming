def gcdSum(x):
    x_copy = x
    sum_digits = 0

    while(x_copy != 0):
        sum_digits += x_copy % 10
        x_copy = int(x_copy/10)
    
    return gcd(x, sum_digits)

def gcd(x, y):

    while(y):
        x, y = y, x % y

    return x

n = int(input())

for i in range(n): print(gcdSum(int(input())))
