s = list(map(int, input().split()))
s = sorted(s)
a = s.pop(0)
b = s.pop(0)
c = s.pop() - a - b
print(a, b, c)