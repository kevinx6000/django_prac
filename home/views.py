from django.shortcuts import render_to_response

def home(req):
    return render_to_response('home.html', {'hello':'Hello', 'world':'world!'})
