s = list(map(int, input().split()))
n = s[0]
k = s[1]

scores = list(map(int, input().split()))
num = 0
for i in range(n): 
    if(scores[i] > scores[k]): 
        num += 1

print(num)