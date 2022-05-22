"""
Codeforces 1613A
"""
t = int(input())
for i in range(t):
    x1, p1 = map(int, input().split())
    x2, p2 = map(int, input().split())
    p1, p2 = p1 - min(p1, p2), p2 - min(p1, p2)
    diff = x1 * (10**p1) - x2 * (10**p2)
    if diff > 0:
        print('>')
    elif diff < 0:
        print('<')
    else:
        print('=')
