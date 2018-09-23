from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import View
import requests
from apps.organization.models import Organizations
from apps.repository.models import Repositories
from apps.organization.forms import SearchForm



class OrganizationView(TemplateView):

    template_name = 'organization/search.html'

    auth = ('Chaoslecion123', '4df9e3ea01b510525e8f2b4f28a16b72a89ba575')

    def get(self,request):

        data_login = False
        name_login = ''
        errors = []
        if 'organization' in request.GET:
            name_login = request.GET['organization']

            try:
                data_login = Organizations.objects.get(login=name_login)

            except Organizations.DoesNotExist:
                request_organization = requests.get('https://api.github.com/orgs/' + name_login,  auth=self.auth)

                if request_organization.status_code == 200:

                    data_login = request_organization.json()

                else:

                    errors.append('El Nombre no Coincide')

        return render(request,'organization/search.html', {'form': SearchForm({'organization': name_login}),
                                                           'errors': errors,
                                                           'data_login': data_login,
                                                           })


class InfoView(View):

    template_name = 'repositories/listing.html'
    auth = ('Chaoslecion123', '4df9e3ea01b510525e8f2b4f28a16b72a89ba575')
    repositories = []

    def get(self, request, name_login=False):

        try:
            data = Organizations.objects.get(login=name_login)
            return HttpResponseRedirect(reverse('repository:index', args=[name_login]))

        except Organizations.DoesNotExist:

            data_request_url = 'https://api.github.com/orgs/' + name_login
            data_request = requests.get(url=data_request_url, auth=self.auth)
            data = data_request.json()

            data = self.saveOrganization(data)

            self.saveRepositories(data)

            return HttpResponseRedirect(reverse('repository:index', args=[data.login]))


    @staticmethod
    def saveOrganization(data):

        organization = Organizations.objects.create(
            login=data['login'],
            name=data['name'],
            description=data['description'],
            avatar_url=data['avatar_url'],
            blog=data['blog'],
            email=data['email'],
            public_repos=data['public_repos'],
        )

        return organization


    def saveRepositories(self , data):

        if data.public_repos > 0:

            self.getAllrepositories('https://api.github.com/orgs/' + data.login + '/repos?type=public')

            repositorioCompleto = []

            for repo in self.repositories:

                repositorioCompleto.append(Repositories(
                    name=repo['name'],
                    html_url=repo['html_url'],
                    description=repo['description'],
                    language=repo['language'],
                    stargazers_count=repo['stargazers_count'],
                    forks_count=repo['forks_count'],
                    created_at=repo['created_at'],
                    updated_at=repo['updated_at'],
                    organization=data,
                )
                )

            Repositories.objects.bulk_create(repositorioCompleto)



    def getAllrepositories(self, request_repositories_url):

        request_repositories = requests.get(request_repositories_url, auth=self.auth)

        request_links = request_repositories.links

        if 'next' in request_links.keys():

            self.getAllrepositories(request_links['next']['url'])

        self.repositories += request_repositories.json()






