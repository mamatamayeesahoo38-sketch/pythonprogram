import re
txt = "The rain in Spain"
matches = re.findall("[a-n]", txt)
print(matches)