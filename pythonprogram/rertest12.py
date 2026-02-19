import re
txt = "rain in Spain"
matches = re.findall("[arn]", txt)
print(matches)  