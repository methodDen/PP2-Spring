def func(n):
	prod = 1
	sum = 0
	cop = n
	while n != 0:
		prod *= n % 10
		n //= 10

	while cop != 0:
		sum += cop % 10
		cop //= 10

	return prod - sum
	
n = int(input())

print(func(n))		