n = int(input())
num = 2 ** n
big = (10 ** 9) + 7
while num > big:
    num -= big
print(num)