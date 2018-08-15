import requests
from bs4 import BeautifulSoup

req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = BeautifulSoup(req.text, "lxml")

# object BeatifulSoup
print('Tipo: {}\nEstructura: {}'.format(type(soup), dir(soup)))

print('Título en html: {}\nNombre del título: {}\nContenido del título: {}'.format(soup.title, soup.title.name, soup.title.string))

# object Tag
print(type(soup.h1))
print(soup.h1)
print(soup.h1.string)
print(soup.h1['class'])
print(soup.h1['id'])
print(soup.h1.attrs)

soup.h1['class'] = 'firstHeading, mainHeading'
soup.h1.string.replace_with("Python - Programming Language")
del soup.h1['lang']
del soup.h1['id']

print(soup.h1)

for h2 in soup.find_all('h2'):
    print(h2.text)

print(soup.p.a)
print(soup.p.find_all('a'))

print(soup.p.contents)
print(soup.p.contents[6])
print(soup.p.children)
for child in soup.p.children:
    print(child.name)

print(soup.p.a.previous_sibling)
print(soup.p.a)
print(soup.p.a.next_sibling)
