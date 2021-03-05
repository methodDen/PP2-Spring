import re
f = open('./data.txt', 'r', encoding='utf8')
data = f.read()
# findall = multiple search'es
name = re.search(r'Филиал\sТОО\s\w+\s\w+', data)
BIN = re.search(r'БИН\s\d{12}', data)
items = re.findall(r'\d+\.\n(.*)', data)
cnt = re.findall(r'(\d),\d{3}', data)
price = re.findall(r'x\s([\d\s]+,\d+)', data)
location = re.findall(r'г\.\s[\w\-]+\,\w+\,\s[\w+\s]+\,\d+\,\s\w+\-\d', data)
date = re.findall(r'Время:(\s\d{2}\.\d{2}\.\d{4}\s\d{2}\:\d{2}\:\d{2})', data)
#[\d\s]+ - множество символов, в котором могут быть числа или пробелы, которые встречаются от 0 и больше раз
# С помощью скобок отделяем нужную для вывода информацию
tot_price = re.findall(r'Стоимость\n(.*)', data)
# (.*) => any character appearing from zero and more times
print(f'1.Name of the company: {name.group()}')
print(f'2.BIN: {BIN.group()}')
for i in range(len(items)):
	print(f'1. Title: {items[i]}')
	print(f'2. Count: {cnt[i]}')
	print(f'3. Unit price: {price[i]}')
	print(f'4. Total price: {tot_price[i]}')
	print("Следующий товар")

print(f'Date: {date[0]}')
print(f'Address: {location[0]}')
#г. Нур-султан,Казахстан, Мангилик Ел,19, нп-5
#Время: 18.04.2019 11:13:58
