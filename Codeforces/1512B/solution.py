t = int(input())

for i in range(t):
    n = int(input())
    rows, cols = (n, n)
    arr = [['']*cols]*rows
    for j in range(n):
        arr[j] = list(input())
    
    pos1 = [0]*2
    pos2 = pos1
    counter = 0
    for j in range(len(arr)):
        for k in range(len(arr[j])):
            if arr[j][k] == "*":
                if counter == 0:
                    pos1 = [j, k]
                else:
                    pos2 = [j, k]
    
    if pos1[0] == pos2[0]:
        
    