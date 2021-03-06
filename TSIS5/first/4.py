n = int(input())
with open('./doc.txt', 'r') as file:
	lines = file.readlines()
	last_lines = lines[-n:]

for line in last_lines:
	print(line)
