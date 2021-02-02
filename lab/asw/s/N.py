n = int(input())

hours = n // 60
hours %= 24
mins = n % 60
print(hours, mins, sep = ' ')