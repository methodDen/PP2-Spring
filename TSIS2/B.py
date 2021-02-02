def numIdenticalPairs(li):
	cnt = 0
	for i in range (0, len(li)):
		for j in range (i + 1, len(li)):
			if (li[i] == li[j]):
				cnt += 1

	return cnt
	
n = int(input())

a = list(map(int, input().strip().split()))[:n]
print(numIdenticalPairs(a))				