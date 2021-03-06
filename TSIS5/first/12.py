with open('./doc.txt', 'w') as file:
	li = [word for word in input().split()]
	for word in li:
		file.write(word)

with open('./doc.txt', 'r') as file:
	print(file.read())	