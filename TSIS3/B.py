a = [int(i) for i in input().split()]

res = 1e9
for num in a:
	if num > 0:
		res = min(res, num)

print(res)		