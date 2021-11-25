def check(seq):
    for i in range(len(seq)):
        if seq[i] > i:
            return False

    return True

t = int(input())

for k in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    counter = 0
    while not check(a):
        a.insert(counter, counter + 1)
        counter += 1
    print(counter)
