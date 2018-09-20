import re

pattern = r'Cookie'
sequence = 'CookieS are genial CokieSS'
print(re.match(pattern, sequence))

sequence = 'the CookieS are genial'
print(re.match(pattern, sequence))

