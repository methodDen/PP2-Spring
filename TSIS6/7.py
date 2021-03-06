def low_and_caps(a):
	low = 0
	caps = 0
	for ch in a:
		if ch >= 'a' and ch <= 'z':
			low+=1
		if ch >= 'A' and ch <= 'Z':
			caps+=1	
	return (low, caps)	


s = input()
print("Lows: " + str(low_and_caps(s)[0]))
print("Caps: " + str(low_and_caps(s)[1]))		