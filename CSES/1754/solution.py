t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print("YES" if (a+b)%3==0 else "NO")