from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render
from apps.testapp.models import Developer
import datetime


def root(request):
    # assert False  # Sirve para romper el flujo
    return HttpResponse('Area 51 Training Center')


def hello(request):
    return HttpResponse('Hello World!')


def current_time(request):
    print(dir(request))  # Muestra en consola
    now = datetime.datetime.now()

    html = '''
    <html>
        <body>
            <h1>PROOF: Hora Actual</h1>
            <h3>{{date}}</h3>
        </body>
    </html>
    '''
    t = Template(html)
    c = Context({'date': now})

    return HttpResponse(t.render(c))


def time_ahead(request, ahead):
    now = datetime.datetime.now()
    time = now + datetime.timedelta(hours=int(ahead))
    c = {'time': time, 'ahead': ahead}
    return render(request, 'proof/proof-time-ahead.html', c)


def find_form(request):
    return render(request, 'find_form.html')


def find(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET[ 'q']
        devs = Developer.objects.filter(name__icontains=q)
        return render(request, 'proof/found-devs.html', {'devs': devs, 'query': q})
    else:
        return render(request, 'proof/find-form.html', {'error': True})


def find_improved(request):
    error = False
    if 'q' in request.GET:
        q = request.GET[ 'q']
        if not q:
            error = True
        else:
            devs = Developer.objects.filter(name__icontains=q)
            return render(request, 'proof/found-devs.html', {'devs': devs, 'query': q})
    return render(request, 'proof/find-form.html', {'error': error})


def find_improved2(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET[ 'q']
        if not q:
            errors.append('Debes agregar un término de búsqueda.')
        elif len(q) > 5:
            errors.append('Debes agregar menos de 5 caracteres.')
        else:
            devs = Developer.objects.filter(name__icontains=q)
            return render(request, 'proof/found-devs.html', {'devs': devs, 'query': q})
    return render(request, 'proof/find-form.html', {'error': errors})

