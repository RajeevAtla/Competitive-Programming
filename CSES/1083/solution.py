def triangle(x):
    return int(x * (x+1)/2)

n = int(input())

ideal_val = triangle(n)
arr = list(map(int, input().split()))
for i in arr:
    ideal_val = ideal_val - i

print(ideal_val)