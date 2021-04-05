s1 = list(input().lower())
s2 = list(input().lower())

s1_int = []
for i in s1:
    s1_int.append(ord(i))

s2_int = []
for i in s2:
    s2_int.append(ord(i))

printed = False

for i in range(len(s1)):
    if s1[i] < s2[i]:
        print(-1)
        printed = True
        break
    elif s1[i] > s2[i]:
        print(1)
        printed = True
        break

if not printed: print(0)