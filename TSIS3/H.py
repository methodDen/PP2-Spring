n, m = map(int, input().split())
a = set()
b = set()

while n != 0:
	num = int(input())
	a.add(num)
	n -= 1

while m != 0:
	num = int(input())
	b.add(num)
	m -= 1	

same = a & b

print(len(same))
same_but_list = list(same)
same_but_list.sort()

for num in same_but_list:
	print(num, end = ' ')

print()
not_sameA = a - b
print(len(not_sameA))
not_sameA_but_list = list(not_sameA)
for num in not_sameA_but_list:
	print(num, end = ' ')

print()
not_sameB = b - a
print(len(not_sameB))
not_sameB_but_list = list(not_sameB)
for num in not_sameB_but_list:
	print(num)

