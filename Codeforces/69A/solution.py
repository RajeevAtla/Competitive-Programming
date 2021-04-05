n = int(input())
arr = [0] * 3
for i in range(n):
    s = [int(x) for x in input().split()]
    for j in range(3): arr[j] += s[j]

ans = True

for x in arr:
    if x != 0: 
        ans = False
        break

print("YES" if ans else "NO")