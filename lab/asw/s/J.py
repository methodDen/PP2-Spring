def func(x):
	sum = 0
	while x != 0:
		sum += x % 10
		x //= 10

	return sum
	
n = int(input())
print(func(n))	