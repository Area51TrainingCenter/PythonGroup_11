from django.shortcuts import render
from apps.tests.models import Organization, Repository
import requests
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect

'''
def created(request):
    if 'q' in request.GET:
        q = ''.join(list(map(str, request.GET['q'].split())))
        url = 'https://api.github.com/orgs/{}/repos'.format(q)
        re = requests.get(url, auth=('Chaoslecion123', '0366aa32ea8364c04b793eb28c5f8e380825e751'))
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

    return render(request, 'tests/interfaz.html')
'''
def created(request):

    errors = []

    if 'q' in request.GET:
        q = ''.join(list(map(str, request.GET['q'].split())))
        p = q.lower()

        try:

            Organization.objects.get(name=p)

        except Organization.DoesNotExist:

            url = 'https://api.github.com/orgs/{}'.format(p)
            re = requests.get(url, auth=('Chaoslecion123', '0366aa32ea8364c04b793eb28c5f8e380825e751'))
            if re.status_code == 200:
                data = re.json()
                organization = Organization.objects.create(name=data['login'])

                url_repo_organization = 'https://api.github.com/orgs/' + data['login'] + '/repos'
                url_repo = requests.get(url_repo_organization,
                                        auth=('Chaoslecion123', '0366aa32ea8364c04b793eb28c5f8e380825e751')).json()

                for repo in url_repo:
                    last_commit_url = repo['commits_url'][:-6] + '/master'
                    last_commit = requests.get(last_commit_url,
                                               auth=('Chaoslecion123', '0366aa32ea8364c04b793eb28c5f8e380825e751')).json()

                    Repository.objects.create(
                        organization=organization,
                        name=repo['name'],
                        fecha=repo['created_at'],
                        update=repo['updated_at']

                    )

                org = Organization.objects.get(name=data['login'])
                w = org.repository_set.all()
                return render(request, 'tests/listado.html', {'w': w})
            else:
                errors.append('No se encontro la organizacion enviada')
        else:
            org = Organization.objects.get(name=p)
            w = org.repository_set.all()

            return render(request, 'tests/listado.html', {'w': w})

    return render(request, 'tests/interfaz.html', {'errors': errors})

