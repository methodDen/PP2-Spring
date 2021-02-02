a = int(input())
b = int(input())

while a > b:
	if a // 2 < b:
		break
	if a % 2 == 1:
		a -= 1
		print("-1")
	else:
		a //= 2
		print(":2")	

while a != b:
	a -= 1
	print("-1")