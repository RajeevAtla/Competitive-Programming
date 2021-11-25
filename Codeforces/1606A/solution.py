def AB(s):
    return s.count('ab')

def BA(s):
    return s.count('ba')

def shift(s, i):
    s[i] = 'a' if s[i] == 'b' else s[i] = 'b'

t = int(input())
for i in range(t):
    s = ''.join(input().split())
    
    if AB(s) == BA(s):
        print(s)
    elif AB(s) > BA(s):
        
