n, q = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))
r = ""
for i in t:
    r += str(a.index(i)+1) + " "
    a.insert(0, a.pop(a.index(i)))
print(r.rstrip())