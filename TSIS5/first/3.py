f = open('./doc.txt', 'a')
s = input()
f.write(s)
f.close()

f = open('./doc.txt', 'r')
print(f.read())
f.close()
