def dist(x):
    if x == 2: return 0
    elif x == 1 or x == 3: return 1
    elif x == 0 or x == 4: return 2

a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
a4 = list(map(int, input().split()))
a5 = list(map(int, input().split()))

a = [a1, a2, a3, a4, a5]

for i in range(5):
    if 1 in a[i]:
        row = i
        column = a[i].index(1)
        break

print(dist(row) + dist(column))