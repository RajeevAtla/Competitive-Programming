s = input()

if(len(s) < 7): 
    print("NO")
    exit()

def dangerous(x):
    for i in range(len(x) - 1):
        if x[i] != x[i+1] and i > 7:
            return "YES"
        elif x[i] != x[i+1]:
            return dangerous(x[i+1:])
    
    return "NO"

print(dangerous(s))