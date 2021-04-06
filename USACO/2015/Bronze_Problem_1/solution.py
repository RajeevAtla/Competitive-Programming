a, b = map(int, input().split())
c, d = map(int, input().split())

paint_arr = [0]*100

for i in range(a, b):
    paint_arr[i] = 1

for i in range(c, d):
    paint_arr[i] = 1

painted = 0

for i in paint_arr:
    painted += i

print(painted)