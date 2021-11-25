n = int(input())

sum = int(n * (n+1)/2)
if sum % 2 != 0 or n <= 2:
    print("NO")
    exit()

print("YES")

if n % 2 == 0:
    odds, evens = [], []
    s_odd, s_even = "", ""
    for i in range(1, n+1):
        if i % 2 == 1:
            s_odd += i
            s_odd += " "
        else:
            s_odd += i
            s_odd += " "
    print(len(s_odd.split()))
    print(s_odd.rstrip())
    print(len(s_even.split()))
    print(s_even.rstrip())
    exit()

r = sum/2
s1, s2 = "", ""
for i in range(1, n+1)[::-1]:
    if r > i:
        s1 += i
        s1 += " "
        r -= 1
    else:
        s2 += i
        s2 += " "

print(len(s1.split()))
print(s1.rstrip())
print(len(s2.split()))
print(s2.rstrip())