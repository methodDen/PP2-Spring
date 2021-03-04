a = [int(i) for i in input().split()]
k = int(input())
k = k % len(a)
print(*a[-k:] + a[:-k])	