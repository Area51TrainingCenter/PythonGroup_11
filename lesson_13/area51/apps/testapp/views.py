from django.http import HttpResponse
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
