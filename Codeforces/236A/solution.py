s = input()

chars = []
for i in range(len(s)):
    if s[i] not in chars:
        chars.append(s[i])

print(chars)

print('IGNORE HIM!' if len(chars) %2 == 0 else 'CHAT WITH HER!')