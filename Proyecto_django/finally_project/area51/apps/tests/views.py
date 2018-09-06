from django.shortcuts import render
from apps.tests.models import Organization, Repository
import requests
from django.http import HttpResponse, HttpResponseRedirect


def created(request):
    if 'q' in request.GET:
        q = ''.join(list(map(str, request.GET['q'].split())))
        url = 'https://api.github.com/orgs/{}/repos'.format(q)
        re = requests.get(url, auth=('Chaoslecion123', '1c633bb69cec8ff96ec191bc47cfb48c12ab01c2'))
        data = re.json()

        for j in data:
            a = j["owner"]["login"]
        organization = Organization.objects.create(name=a)

        for i in data:
            rep = i['name']
            url_commit = 'https://api.github.com/repos/{}/{}/commits'.format(q, rep)
            # re2 = requests.get(url_commit)
            # data2 = re2.json()
            # commits = data2[0]['commit']['author']['date']
            Repository.objects.create(
                organization=organization,
                name=i['name'],
                fecha=i['created_at']
                # commits= data2[0]['commit']['author']['date']
                )
        repo = Repository.objects.all()
        context = {'repo': repo}
        return render(request, 'tests/listado.html', context)
    return render(request, 'tests/interfaz.html')



