def is_perf(a):
	a = int(a)
	summ = 0
	for i in range(1, a):
		if a % i == 0:
			summ += i

	if summ != a:
		return False

	summ += a
	if summ / 2 != a:
		return False

	return True


num = int(input())
print(is_perf(num))
