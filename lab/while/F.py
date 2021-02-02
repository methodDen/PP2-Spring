x = int(input())
y = int(input())

cnt = 0

while x < y:
	x += x * 0.1
	cnt += 1

print(cnt + 1)	