
t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    evens, odds = [], []
    for i in arr:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    s = ""
    for i in evens + odds:
        s += str(i)
        s += " "
    print(s.rstrip())
    

