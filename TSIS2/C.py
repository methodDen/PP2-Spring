import re

def defang(address):
	return address.replace(".", "[.]")

s = str(input())

print(defang(s))
