n = int(input())
a = map(int, input().split())

crimes, police = 0, 0

for i in a:
    if i == -1:
        if police > 0: police -= 1
        else: crimes += 1
    else: police += i

print(crimes)