num = 0

for i in range(int(input())):
    s = input().split()
    s = list(map(int, s))
    if sum(s) >= 2: num += 1

print(num)