def intrpt (com):
	gen = ""
	for i in range(0, len(com)):
		if com[i] == 'G':
			gen += 'G'
		elif com[i] == '(' and com[i + 1] == ')':
			gen += 'o'
		elif com[i] =='a' and com[i + 1] == 'l':
			gen += "al"
	return gen

command = str(input())
print(intrpt(command))
