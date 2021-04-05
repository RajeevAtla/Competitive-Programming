def lcm(x, y):
    least_num = 1
    lcm_found = False
    while not lcm_found:
        if(least_num % x == 0 and least_num % y == 0): return least_num
        else: least_num = least_num + 1

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    a = [1]*k
    if(sum(a) )