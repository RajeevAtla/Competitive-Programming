s1 = list(input().lower())
s2 = list(input().lower())

def compare(a, b):
    assert len(a) == len(b)
    for i in range(len(a)):
        if ord(a[i]) < ord(b[i]):
            return -1
        elif ord(a[i]) > ord(b[i]):
            return 1
    return 0

print(compare(s1, s2))