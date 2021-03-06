n = int(input())
f = open('./doc.txt', 'r')
for i in range(n):
	print(f.readline())
f.close()