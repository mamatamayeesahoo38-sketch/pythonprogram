import re
result = re.search(r'\d+', 'abc123de56f')
print(result.group())  # Output: 123

