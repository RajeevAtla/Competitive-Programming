n = int(input())
arr = list(map(int, input().split()))

score = 0

for i in range(1, len(arr)):
    if(arr[i] < arr[i-1]):
        temp = arr[i-1] - arr[i]
        arr[i] += temp
        score += temp

print(score)