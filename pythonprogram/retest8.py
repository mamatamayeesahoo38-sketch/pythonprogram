import re
# Check if a string starts with a letter followed by digits
pattern = r'^[A-Za-z]\d+'
text = "ABC"
match = re.match(pattern, text)
if match:
    print(f"Match found: {match.group()}")
else:
    print("No match found")
