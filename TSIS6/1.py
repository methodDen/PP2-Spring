def maxi(a, b, c):
  res = max(max(a, b), c)
  return res
  
a, b, c = map(int, input().split())
print(maxi(a, b, c))