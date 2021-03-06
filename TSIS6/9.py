def is_prime(a):
	a = int(a)
	if a == 1:
		return False
	elif a == 2:
		return True
	cnt = 0
	for i in range(1, a + 1):
		if a % i == 0:
			cnt+=1

	if cnt > 2:
		return False

	return True

num = int(input())
print(is_prime(num))				