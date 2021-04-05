def update(a, b): return 3*a, 2*b

a, b = map(int, input().split())

if(a == b):
    print(1)
    exit()

counter = 0
while(a <= b):
    a, b = update(a, b)
    counter += 1

print(counter)