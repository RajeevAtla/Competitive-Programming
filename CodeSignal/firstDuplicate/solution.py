def firstDuplicate(a):
    temp = []
    for i in a:
        if i in temp:
            return i
        temp.append(i)
    return -1