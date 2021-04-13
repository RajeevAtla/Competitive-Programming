def most_frequent(List):
    return max(set(List), key = List.count)

t = int(input())

for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    m = most_frequent(s)
    for j in range(n):
        if s[j] != m:
            print(j+1)
            break