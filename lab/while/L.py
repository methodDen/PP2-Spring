maxi = -1e9

while True:
	n = int(input())
	maxi = max(maxi, n)
	if n == 0:
		break

print(maxi)		