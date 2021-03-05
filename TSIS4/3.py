import re
reg_pattern = r"\.|,"

print("\n".join(re.split(reg_pattern, input())))