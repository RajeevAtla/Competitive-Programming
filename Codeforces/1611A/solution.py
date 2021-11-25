t = int(input())
for i in range(t):
    n = input()
    if int(n) % 2 == 0:
        print(0)
    elif int(n[0]) % 2 == 0:
        print(1)
    else:
        num = [int(j) % 2 == 0 for j in n]
        if any(num):
            print(2)
        else:
            print(-1)
