list = []
start = ord('a') - 1

for i in range(4):
    a = []
    for j in range(4):
        if(i == 0):
            if(j == 0):
                j = '*'
        else:
            if(j == 0):
                j = chr(start)
            else:
                j = 'x'
        a.append(str(j))
    start += 1
    list.append(a)

for i in list:
    print(' '.join(i))