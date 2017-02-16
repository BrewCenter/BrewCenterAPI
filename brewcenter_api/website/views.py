from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import UserForm

def home(request):
    """
    The mostly static index view for the rest framework
    """
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def register(request):
    """
    Displays the login form
    """
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            user = uf.save()
            template = loader.get_template('registration/login.html')      
            render(request, 'registration/login.html', dict(registered=True))
            return HttpResponse(template.render({'registered': True}, request))
        print(uf.errors)
    else:
        uf = UserForm()
    return render(request, 'registration/register.html', {'userform':uf, 'errors': uf.errors})
            