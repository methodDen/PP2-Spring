import sys
def cmp(x):
    return (-x[0], x[1]) #sort by убывание number of appearance and lexigraphically the words

a = (str(sys.stdin.read()).split())
b = {}
for i in a:
    b[i] = b.get(i, 0) + 1 # get(key, value) + 1 -> return value of an item that do not exist
    #frequency of appearance is assigned
b = [(x, y) for y, x in b.items()] # b.items() - return the list with all dict keys with values
b.sort(key=cmp)
for i in range(len(b)):
    print(b[i][1])

# Ctrl + Z to see results    