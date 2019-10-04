from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import (
    render_to_response
)

# Create your views here.
def index(request):
    title = "Ramza | Young Developer"
    return render(request, 'index.html', {"title": title })

def about(request):
    title = " Ramza | About"
    return render(request, 'about.html', {"title": title})

def projects(request):
    title = 'Ramza | Projects'
    return render(request, 'projects.html', {"title": title})


# HTTP Error 400
def error_404(request):
        data = {}
        return render(request, 'fourOwfour.html', data)


def error_500(request):
        data = {}
        return render(request, 'fourOwfour.html', data)

# end of error views

def photos(request):
    title = 'Photos | Ramza'
    return render(request, 'photos2.html', {"title": title})
