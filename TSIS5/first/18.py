with open('./doc.txt', 'r') as file:
	data = file.read()
	data.replace(",", " ")
	print(len(data.split(' ')))