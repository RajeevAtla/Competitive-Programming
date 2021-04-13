t = sorted([x for x in input() if x != '+'])
w = ""
for i in t: 
    w += i + '+'
print(w.rstrip('+'))