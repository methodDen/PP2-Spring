import random
with open('doc.txt', 'r') as file:
	lines = file.read().splitlines()
	print(random.choice(lines))