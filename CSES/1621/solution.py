n = int(input())
x = list(map(int, input().split()))

s = set()
for i in x:
    s.add(i)

print(len(s))