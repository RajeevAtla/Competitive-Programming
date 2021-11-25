for i in range(int(input())):
    s = list(map(int, input().split()))  

    s1 = s[0]
    s2 = s[1]
    s3 = s[2]
    s4 = s[3]

    s = sorted(s)[::-1]

    m1 = max(s1, s2)
    m2 = max(s3, s4)

    if(max(m1, m2) == s[0] and min(m1, m2) == s[1]):
        print('YES')
    else:
        print('NO')