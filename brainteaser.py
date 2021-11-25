A = list(range(1, 9))
N = A.copy()

L = list(range(9))
O = L.copy()
N = L.copy()
E = L.copy()
T = L.copy()
I = L.copy()
G = L.copy()
H = L.copy()

ans = [[]]

for a in A:
    for n in N:
        for l in L:
            for o in O:
                for e in E:
                    for t in T:
                        for i in I:
                            for g in G:
                                for h in H:
                                    if 81*a + 9*l + l + 6561*a + 729*l + 81*o + 9*a + t == 6561*n + 729*i + 81*g + 9*h + t:
                                        ans.append([a, l, o, n, e, t, i, g, h])


for i in ans:
    i = list(set(i))

ans = [i for i in ans if len(i) == 9]

print(ans)
