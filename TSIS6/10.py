def evs(a):
	res = []
	for i in a:
		if int(i) % 2 == 0:
			res.append(i)

	return res
	
li = [int(i) for i in input().split()]		
print(*evs(li))	