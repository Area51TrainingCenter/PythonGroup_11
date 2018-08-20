# -*- coding: utf-8 -*-

import requests
import re
import json


date = '25/12/2017'
body = {
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

url_1 = 'https://civil.pjud.cl/CIVILPORWEB/AtPublicoDAction.do'
url_2 = 'https://civil.pjud.cl'

sess = requests.Session()
y = sess.get('https://civil.pjud.cl/CIVILPORWEB/')
r = sess.get('https://civil.pjud.cl/CIVILPORWEB/AtPublicoViewAccion.do?tipoMenuATP=1')
#cookies = dict(y.cookies)
#print(cookies)

#r = sess.post(url_1, data=body, cookies=cookies)
r = sess.post(url_1, data=body)

print(r)
print(r.history)
print(r.status_code)
print(dir(r))

html_1 = r.text
#print(html_1)

links = re.findall("<a href='(/CIVIL.+)'", html_1)

print(links[:1])

fields = []
for link in links[:1]:
    html_2 = requests.get(url_2 + link).text
    data = re.search('ROL :[ ]*([a-zA-Z0-9\-]+).+F\. Ing :[ ]*([0-9/]+).+Tribunal :[ ]*([a-zA-Z0-9º\- ]+)', html_2, re.DOTALL)
    rol, date, judge = data.groups()
    litigants_data = re.findall('76">([^<]+).+?90">([^<]+).+?84">([^<]+).+?320">([^<]+)', html_2, re.DOTALL)
    litigants = []
    for l in litigants_data:
        litigant = {'participante': l[0], 'rut': l[1].split('-')[0], 'dv': l[1].split('-')[1], 'persona': l[2], 'nombre': l[3]}
        litigants.append(litigant)
    d = {'rol': rol, 'tribunal': judge, 'fecha_ingreso': date, 'litigantes': litigants}
    fields.append(d)

print(fields)
