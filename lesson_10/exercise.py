# Ejercicio #

## Scrapendo PJCL ##

Tenemos la web del Poder judicial de chile [pjcl](https://civil.pjud.cl/CIVILPORWEB/) y hemos realizado un web scraping usando
expresiones regulares y requests. La tarea de esta clase es realizar lo mismo, pero en lugar de usar expresiones regulares
debemos usar la librería Beautiful Soup.

import requests
from bs4 import BeautifulSoup
import  re

sess = requests.session()
r = sess.get('https://civil.pjud.cl/CIVILPORWEB/')
r2 = sess.get('https://civil.pjud.cl/CIVILPORWEB/AtPublicoViewAccion.do?tipoMenuATP=1')

date = '25/12/2017'
data = {
    'TIP_Consulta': '2',
    'TIP_Lengueta': 'tdDos',
    'TIP_Causa': 'C',
    'ROL_Causa': '',
    'ERA_Causa': '',
    'FEC_Desde': date,
    'FEC_Hasta': date,
    'RUT_Consulta': '',
    'RUT_DvConsulta': '',
    'NOM_Consulta': '',
    'APE_Paterno': '',
    'APE_Materno': '',
    'COD_Tribunal': '0',
    'irAccionAtPublico': 'Consulta'
}

response = sess.post('https://civil.pjud.cl/CIVILPORWEB/AtPublicoDAction.do' , data=data)
html = response.text

links = re.findall("<a href='(/CIVIL.+)'", html)

#print(links[:2])

for  i , link in enumerate(links ,start=1) :
    html2 = sess.get('https://civil.pjud.cl' + link).text
    soup = BeautifulSoup(html2 ,"html.parser")

for td in soup.find_all('td', {'class': 'texto'} , 'title'):

    print(td)