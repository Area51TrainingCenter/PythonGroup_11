from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render
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

