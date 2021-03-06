with open('./doc.txt', 'r') as file:
	data = file.read().split()
	max_len = len(max(data, key = len))
	li = [word for word in data if len(word) == max_len]
	print(li)