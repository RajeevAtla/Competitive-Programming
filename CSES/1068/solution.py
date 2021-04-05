def algo(x):
    if x % 2 == 0:
        return int(x/2)
    else:
        return 3*x+1

z = int(input())

z_arr = [z]

z_copy = z

while(z_copy != 1):
    z_copy = algo(z_copy)
    z_arr.append(z_copy)

s = ""

for i in range(len(z_arr)):
    s += str(z_arr[i])
    s += " "

print(s)