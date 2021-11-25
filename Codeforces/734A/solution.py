n = int(input())
s = list(input())
score = 0
for i in s:
    if i == 'A': score += 1
    elif i == 'D': score -= 1

if score > 0: print('Anton')
elif score < 0: print('Danik')
else: print('Friendship')