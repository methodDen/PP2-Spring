def summ(a):
  res = 0
  for i in a:
    res += int(i)
  return res
  
a = [int(i) for i in input().split()]
print(summ(a))