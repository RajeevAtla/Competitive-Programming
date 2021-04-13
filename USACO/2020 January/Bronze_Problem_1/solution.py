n, k = map(int, input().split())
s = input().split()

current = 0
total = False
str = ""
while current < n:
    while len(str) > k:
        str += s[current]
        str += " "
        current += 1
    print(str[:-1])