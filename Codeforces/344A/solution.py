n, g, p = int(input()), 0, input()
for i in range(n-1):
    c = input()
    if c != p: g += 1
    p = c
print(g+1)