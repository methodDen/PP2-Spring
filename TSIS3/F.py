from collections import Counter as mset

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

inters = list(mset(a) & mset(b))
print(len(inters))