def search_2d(arr):
    for i in arr:
        for j in i:
            if j == 'B':
                return True
    return False


t = int(input())
for i in range(t):
    n, m, r, c = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    if not search_2d(grid):
        print(-1)
    else:
        if grid[r-1][c-1] == 'B':
            print(0)
        else:
            if 'B' in grid[r-1]:
                print(1)
            elif 'B' in [i[c-1] for i in grid]:
                print(1)
            else:
                print(2)
