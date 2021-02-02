k, n = map(int, input().split())

page = n // k + 1
left = n - ((page - 1) * k)

if left == 0:
	left += 1

print(page, left, sep = ' ')