import re

pattern = r'Cookie'
sequence = 'The CookieS are genial'
match = re.search(pattern, sequence)
print(match.group(), match.start(), match.end())

sequence = 'The cOOKIEs are genial'
match = re.search(pattern, sequence, flags=re.IGNORECASE)
print(match.group(), match.start(), match.end())

