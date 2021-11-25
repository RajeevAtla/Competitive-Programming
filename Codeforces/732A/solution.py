k, r = map(int, input().split())
n = 1

#k = price of shovel
#r = price of non-10 denomination
#we're trying to find minimum n such that nk = ar+10b for integer n, a, b
#or minimize k * x = r (mod 10) or k * x = 0 (mod 10)

while(True):
    num = k * n
    if num % 10 == r or num % 10 == 0:
        print(n)
        break
    else:
        n += 1