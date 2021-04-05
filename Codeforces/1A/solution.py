s = list(map(int, input().split()))
n = s[0]
m = s[1]
a = s[2]

n, m = n + a - 1, m + a - 1

print(int((n*m)/(a**2)))