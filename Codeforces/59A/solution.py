s = input()
n = 0

for i in s:
    if i.isupper: n += 1

if n >= len(s)//2:
    print(s.upper())
else:
    print(s.lower())

