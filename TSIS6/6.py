def is_in_Range(a, l, r):
	if int(a) in range(int(l), int(r)):
		return True
	else:
		return False

a, l, r = map(int, input().split())

if is_in_Range(a, l, r):
	print("Ya")
else:
	print("Nah")	
