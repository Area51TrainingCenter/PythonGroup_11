import re

pattern = r'Cookie'
sequence = 'CookieS are genial'
print(re.match(pattern, sequence))

sequence = 'The CookieS are genial'
print(re.match(pattern, sequence))

