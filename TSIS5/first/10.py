with open('./doc.txt', 'r') as file:
	words = file.read().split()
	print(len(words))