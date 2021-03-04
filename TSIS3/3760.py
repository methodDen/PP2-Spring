n = int(input())
dic = {}
for i in range(n):
	a, b = map(str, input().split())
	dic[a] = b
	dic[b] = a
s = input()
print(dic[s])