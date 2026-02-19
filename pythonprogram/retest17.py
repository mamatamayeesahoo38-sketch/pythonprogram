import re
txt = "The meeting times are 09, 25, and 59."
matches = re.findall("[0-5][0-9]", txt)
print(matches) 