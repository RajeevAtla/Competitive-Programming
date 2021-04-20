n = int(input())

s = list(input())

r = 0
for i in range(n-1):
    if s[i] == s[i+1]:
        r += 1

print(r)