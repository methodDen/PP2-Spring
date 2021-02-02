a = []
n = int(input())

i = 1
while i * i <= n:
	a.append(i * i)
	i+=1

print(*a, sep = ' ')	