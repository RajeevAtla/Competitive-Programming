n = int(input())
S = input()

x, y = 0, 0

cost = 0

for i in range(n):
    x0, y0 = x, y

    if S[i] == 'U': y += 1
    else: x += 1

    if x0 == y0 and S[i] == 'U' and S[i-1] == 'U': cost += 1
    elif x0 == y0 and S[i] == 'R' and S[i-1] == 'R': cost += 1

print(cost)