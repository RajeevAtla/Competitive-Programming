t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a = list(input())

    a = list(map(int, a))


    for i in range(m):
        for i in range(1, n-1):
            if a[i] == 0:
                if(a[i-1] == 1 and a[i+1] == 0):
                    a[i] = 1
                elif(a[i-1] == 0 and a[i+1] == 1):
                    a[i] = 1
                    
    
    a = list(map(str, a))
    print(''.join(a))