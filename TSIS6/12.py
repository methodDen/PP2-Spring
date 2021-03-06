def is_pal(a):
	if a == a[::-1]:
		return True
	return False

s = input()
print(is_pal(s))		