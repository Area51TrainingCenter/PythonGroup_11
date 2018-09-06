from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
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
            <h1>TEST: Hora Actual</h1>
            <h3>{}</h3>
        </body>
    </html>
    '''.format(now)

    return HttpResponse(html)


def time_ahead(request, ahead):
    now = datetime.datetime.now()
    time = now + datetime.timedelta(hours=int(ahead))
    html = '''
    <html>
        <body>
            <h1>TEST: Agregar {} hora(s)</h1>
            <h3>{}</h3>
        </body>
    </html>
    '''.format(ahead, time)
    return HttpResponse(html)


def create_dev(request, username):
    lastname = username[::-1]
    email = '{}@area51.pe'.format(username)
    #dev = Developer.objects.create(name=username, lastname=lastname, email=email)
    dev = Developer(name=username, lastname=lastname, email=email)
    dev.save()
    return HttpResponse('Created Developer')


def create_dev_improved(request):
    errors = []
    name = request.POST.get('name', '')
    lastname = request.POST.get('lastname', '')
    email = request.POST.get('email', '')
    if request.method == 'POST' :
        if not name:
            errors.append('Por favor introduce un nombre.')
        if not lastname:
            errors.append('Por favor introduce un apellido.')
        if not email or '@' not in email:
            errors.append('Por favor introduce una dirección de email válida.')
        if not errors:
            dev = Developer.objects.create(name=name, lastname=lastname, email=email)
            return HttpResponseRedirect('/test/thanks/?name=' + name)
    return render(request, 'test/form-dev.html', {
        'errors': errors,
        'name': name,
        'lastname': lastname,
        'email' : email,
    })


def thanks(request):
    name = request.GET.get('name', '')
    return render(request, 'test/thanks.html', {'name': name})


def delete_dev(request, id):
    deleted = Developer.objects.filter(id=id).delete()
    return HttpResponse(deleted)


def update_dev(request, id):
    dev = Developer.objects.get(id=id)
    dev.email = 'changed@gmail.com'
    dev.save()
    return HttpResponse('Updated Developer')


def get_dev(request, id):
    #dev = Developer.objects.get(id=id)
    devs = Developer.objects.filter(id=id)
    if devs:
        s = devs[0].name
    else:
        s = 'No existe'
    return HttpResponse(s)


def filter_devs(request, name):
    devs = Developer.objects.filter(name=name)
    s = ''
    for dev in devs:
        s += '{} '.format(dev.name)
    return HttpResponse(s)


def filter_devs_for_domain(request, domain):
    devs = Developer.objects.filter(email__contains=domain)
    s = ''
    for dev in devs:
        s += '{} {}<br>'.format(dev.name, dev.email)
    return HttpResponse(s)


def devs(request):
    devs = Developer.objects.all()
    s = ''
    for dev in devs:
        s += '{} '.format(dev.name)
    return HttpResponse(s)


def devs_template(request):
    devs = Developer.objects.all()
    context = {'devs': devs}
    return render(request, 'test/testapp.html', context)

