import re
result = re.sub(r'\d+', 'Y', 'abc123def456')
print(result)  # Output: abcXdefX

