from django.http import HttpResponse

def home(req):
    return HttpResponse('安安')
