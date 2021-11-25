n = int(input())

pass_ = [0]

for i in range(n):
    a, b = map(int, input().split())
    pass_.append(pass_[-1] - a)
    pass_.append(pass_[-1] + b)

print(max(pass_))
