n = int(input())

while n != 0:
	if n == 1:
		print("YES")
		exit()
	n /= 2

print("NO")
