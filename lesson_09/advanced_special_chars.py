import re

# Save grouping
email = 'Please contact us at: support@area51.com'
match = re.search(r'([\w.-]+)@([\w.-]+)', email) # two groups defined
print(match.group())
print(match.group(1))
print(match.group(2))

# Greedy
heading = r'<h1>TITLE</h1>'
print(re.search(r'<.+>', heading).group()) # Greedy
print(re.search(r'<.+?>', heading).group()) # Non greedy

