k, n, w = map(int, input().split())
amt = int((k * ((w * (w + 1))/2)) - n)
if amt > 0: print(amt)
else: print(0)