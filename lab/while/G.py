x = int(input())
p = int(input())
y = int(input())

cnt = 0
p = float(p / 100)

while x < y:
	x += (x * p)
	x = int(x)
	cnt += 1

print(cnt)	