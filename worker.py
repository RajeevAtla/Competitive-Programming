import os

folders = [x[0] for x in os.walk('.')]

for i in folders:
    if 'git' in i:
        folders.remove(i)

#folders = list(map(lambda x: x.replace('\\', '').replace('.\\', '').replace('.', ''), folders))

for i in folders:
    if 'gitobjects' in i:
        folders.remove(i)

for i in folders:
    if '.git' in i:
        folders.remove(i)

print(folders)
