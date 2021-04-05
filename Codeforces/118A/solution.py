s = input()

str = "aeiouyAEIOUY"

for i in str:
    s = s.replace(i, "")

s = s.lower()

s_new = "."

for i in range(len(s)):
    s_new += s[i]
    if i != len(s)-1: s_new += "."

print(s_new)