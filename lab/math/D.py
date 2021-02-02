deg = int(input())
hours = deg // 30
minutes = deg % 30 // 0.5
minutes = int(minutes)
print(f"It is {hours} hours {minutes} minutes.")