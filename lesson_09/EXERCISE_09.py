import re
import requests

#Obteniendo Texto
url = "http://www.gutenberg.org/files/2638/2638-0.txt"
text = requests.get(url).text

#Acortando Texto
start = re.search(r'\*\*\* START OF THIS PROJECT GUTENBERG EBOOK THE IDIOT \*\*\*',text).end() #Start Text
end = re.search(r'II\.',text).start()   # End Text
text = text[start:end] 


### Tarea 4: Contar aparicion de comillas dobles ( " )
comp_4 = re.compile(r'[\“\”]')
count_4 = len(comp_4.findall(text) )


### Tarea 5: Contar palabras unidas por ( -- ) 
comp_5 = re.compile(r'(\w+--\w+)')
count_5 = len(comp_5.findall(text) )



### Tarea 1 : Solo minusculas digitos o dot(.)  . Remplazar el resto por espacios (" ")
comp_1 = re.compile(r'[^\w\.]') #Pattern
text = (comp_1.sub(' ',text)).lower() #Replace

### Tarea 2 : contar numero de apariciones de la palabra -->  " the "
comp_2 = re.compile(r'(\bthe\b)', re.IGNORECASE)
count_2 = len(comp_2.findall(text))


###Tarea 3 : Reemplazar las ' i ' por ' I ' cuando esten aisladas
comp_3 = re.compile(r'\bi\b')
text = comp_3.sub(' I ',text)

print(text)

print("2__ ** La Palabra ' the ' aparece {} veces".format(count_2))
print('4__ ** Comillas dobles aparece {} veces '.format(count_4))
print("5__ ** Hay {}  palabras unidas por '--' ".format(count_5))
