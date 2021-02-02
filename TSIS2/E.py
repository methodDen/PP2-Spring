def largest(li):
	v = [0] * (len(li) + 1)
	maxi = v[0]
	for i in range (1, len(a) + 1):
		v[i] = v[i - 1] + li[i - 1]
		maxi = max(maxi, v[i])
	return maxi	
n = int(input())

a = list(map(int, input().strip().split()))[:n]

print(largest(a))		