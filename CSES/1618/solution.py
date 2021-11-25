n = int(input())
z = 0
num_2 = 0
num_5 = 0

for i in range(2, n+1)[::-1]:
    if i % 10 == 0:
        z += 1
    elif i % 2 == 0:
        num_2 += 1
    elif i % 5 == 0:
        num_5 += 1

print(z + max(num_2, num_5))