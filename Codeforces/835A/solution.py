s, v1, v2, t1, t2 = map(int, input().split())

time1 = s * v1 + 2 * t1
time2 = s * v2 + 2 * t2

if time1 > time2:
    print("Second")
elif time2 > time1:
    print("First")
else:
    print("Friendship")