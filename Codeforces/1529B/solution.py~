
def strange(a):
    for i in range(len(a)):
        for j in range(i):
            if abs(a[i] - a[j]) < max(a):
                return False

    return True

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if(strange(a)):
        print(len(a))
    else:
        while(not strange(a)):
            a.remove(max(a))

        print(len(a))
