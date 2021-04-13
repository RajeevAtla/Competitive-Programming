def sum_divisors(num):
    return lambda k:sum(i*(k%i<1)for i in range(1,1+k))

t = int(input())

for i in range(t):
    c = int(input())
    min = 1
    min_found = False
    while not min_found:
        if sum_divisors(min) == c:
            min_found = True
            print(min)
            break
        else:
            min += 1
    if not min_found:
        print(-1)