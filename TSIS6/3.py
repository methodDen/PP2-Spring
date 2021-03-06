def mult(a):
  res = int(a[0])
  for i in range(1, len(a)):
    res *= int(a[i])
  return res
  
a = [int(i) for i in input().split()]
print(mult(a))