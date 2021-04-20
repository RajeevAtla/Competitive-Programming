x = int(input())
if x < 5: 
    print(1)
    exit()
r1, x = x//5, x % 5
if x == 0:
    print(r1)
else:
    print(r1+1)