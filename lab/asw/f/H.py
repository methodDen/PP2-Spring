import math

a = pow(179, 10)
s = str(a)
print(s)
s += s
print(s)
s += s
print(s)
s += s
a = int(s)
print(s)
print(pow(a, 1/10))