import re
#re.match() – Checks for a match only at the beginning of the string.
result = re.match(r'\W+', '$h123$5')
print(result.group())  # Output: 123
