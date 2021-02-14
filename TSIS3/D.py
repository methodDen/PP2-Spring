a = [int(i) for i in input().split()]
cnt = 0

for num in a:
	if num != 0:
		a[cnt] = num
		cnt += 1

while cnt < len(a):
	a[cnt] = 0
	cnt += 1

print(*a, sep = ' ')			