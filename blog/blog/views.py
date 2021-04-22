from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hello(request):
    hello = "<html><body>Seja bem-vindo meus amigos!"
    return HttpResponse(hello)