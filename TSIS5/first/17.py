with open('./doc.txt', 'r') as file:
	flist = file.readlines()
	new_li = [s.rstrip('\n') for s in flist]
	print(new_li)