def uni(a):
	li_set = set()
	for i in a:
		li_set.add(int(i))

	return list(li_set)

samp = [int(i) for i in input().split()]
print(*uni(samp))		