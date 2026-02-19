import re
txt = "The year is 2024"
matches = re.findall("[0-9]", txt)
print(matches)