t = int(input())




for i in range(t):
    y, x = map(int, input().split())

    if y == 1 and x == 1:
        print(1)
    else:
        n = x - 1
        if n % 2 == 0:
            print(n**2 - y + 1)
        else: 
            print(n**2 + x - 1)
