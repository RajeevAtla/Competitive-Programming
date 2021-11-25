n = int(input())
deck = list(map(int, input().split()))
s, d = 0, 0

for i in range(n):
    if i % 2 == 0:
        s += max(deck[0], deck[-1])
        deck.remove(max(deck[0], deck[-1]))
    else:
        d += max(deck[0], deck[-1])
        deck.remove(max(deck[0], deck[-1]))
    
r = str(s) + " " + str(d)
print(r)