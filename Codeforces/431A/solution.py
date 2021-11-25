a = list(map(int, input().split()))
s = list(input())
s = list(map(int, s))

cals = 0

for i in s:
    if i == 1:
        cals += a[0]
    elif i == 2:
        cals += a[1]
    elif i == 3:
        cals += a[2]
    elif i == 4:
        cals += a[3]

print(cals)