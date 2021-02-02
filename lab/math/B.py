n = int(input())

if n < 0:
	sum = ((-1 + n) // 2) * (-n) + 1
	print(sum)
elif n == 0:
	print(1)
else:
	print((1 + n) * n // 2)