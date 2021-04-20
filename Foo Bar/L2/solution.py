def algo(n, b):
    # n is input string with 2 <= length <= 9
    # b is base 2 <= b <= 9
    k, n_1 = len(n), list(n)
    y = sorted(n_l)
    x = y[::-1]
    z = []
    for i in range(k):
        if x[i] < y[i]:
            x[i] = x[i] + b
            x[i+1] = x[i+1] - 1
        z[i] = x[i] - y[i]
    return ''.join(z)


def solution(n, b): 
    arr = [n]
    stop = False
    while not stop:
        n = algo(n, b)
        arr.append(n)
        if n in arr:
            stop = True
    return len(arr) - 1

print()
