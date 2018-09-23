from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from apps.organization.models import Organizations
from apps.repository.forms import FormularioRepo

class Repository(TemplateView):

    template_name = 'repositories/listing.html'

    def get(self, request, name_login=False):


        try:
            organization = Organizations.objects.get(login=name_login)

            fil = request.GET.get('fil', '')

            repositories = organization.repositories_set.filter(name__contains=fil)



        except Organizations.DoesNotExist:

            return HttpResponseRedirect(reverse('organization:index'))


        return render(request,'repositories/listing.html', {'repositories': repositories,'data': organization,
                                                            'form': FormularioRepo({'fil': fil})})