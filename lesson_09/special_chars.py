import re

# Matches of characteres
sequence = 'Cookie'
match = re.search(r'C.ok.e', sequence)
print(match.group())

print(re.match(r'Eat\wCake', 'Eat_Cake').group()) # letter, digit or underscore
print(re.match(r'Eat\sCake', 'Eat Cake').group()) # space, tab, return or newline
print(re.match(r'Eat\dCake', 'Eat0Cake').group()) # digit

# Start and End
print(re.search(r'^Eat', 'Eat Cake, Eat Cookies').group())
print(re.search(r'ke$', 'Cake').group())
print(re.search(r'ke$', 'Cake '))

# Grouping
print(re.match(r'Number: [abc]', 'Number: c').group()) # matches with a, b or c
print(re.match(r'Number: [0-9]', 'Number: 5').group()) # is equivalent to \d
print(re.match(r'Number: [a-zA-Z]', 'Number: M').group()) # matches with all letters

# Repetitions
print(re.search(r'C.+kies', 'Cooookies').group()) # 1 or more
print(re.search(r'C.*kies', 'Ckies').group()) # 0 or more
print(re.search(r'C.?kies', 'Cakies').group()) # 0 or 1

print(re.search(r'[789]\d{8}$', '912345678').group()) # 8 exactly
print(re.search(r'[789]\d{8,}', '912345678000').group()) # 8 or more
print(re.search(r'[789]\d{8,10}$', '91234567800').group()) # 8 to 10

