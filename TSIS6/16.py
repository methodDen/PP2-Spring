def func():
	li = list()
	for i in range(1, 31):
		li.append(i ** 2)

	print(*li)

func()		