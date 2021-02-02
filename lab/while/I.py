a = [0] * 10005

a[0] = 1
a[1] = 1
def find(li, x):
	l = 0
	r = len(li) - 1
	while r >= l:
		m = (l + r) // 2
		if li[m] == x:
			return True
		if li[m] < x:
			l = m + 1
		if li[m] > x:
			r = m - 1

	return False				

def indo(li, x):
	indexx = 0
	l = 0
	r = len(li) - 1
	while r >= l:
		m = (l + r) // 2
		if li[m] == x:
			indexx = m + 1
			return indexx
		if li[m] < x:
			l = m + 1
		if li[m] > x:
			r = m - 1

	return 0				



n = int(input())

for i in range(2, 10001):
	a[i] = a[i - 1] + a[i - 2]

flag = find(a, n)
if flag == False:
	print(-1)
else:
	print(indo(a, n))