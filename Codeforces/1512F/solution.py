t = int(input())

for i in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    index, count, tugriks = 0, 1, 0
    
    while(tugriks < c):
            if(index < len(b)):
                if (tugriks >= b[index]):
                    tugriks -= b[index]
                    index += 1
            tugriks += a[index]
            count += 1

    print(count)
