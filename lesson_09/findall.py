import re

emails = 'Please contact us at: support@area51.com renzo@whiz.pe'
print(re.findall(r'[\w.-]+@[\w.-]+', emails))
print(re.findall(r'([\w.-]+)@([\w.-]+)', emails))

# Replace
new_email = re.sub(r'[\w.-]+@[\w.-]+', r'admin@area51.com', emails)
print(new_email)

# Compile is more efficient
pattern = re.compile(r'cookie')
sequence = 'Cake and cookie'
print(pattern.search(sequence).group()) # is equivalente to re.search(pattern, sequence)

