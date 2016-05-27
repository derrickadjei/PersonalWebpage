from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template('aboutMe/index.html')
    return HttpResponse(template.render(request))


def resume(request):
    template = loader.get_template('aboutMe/resume.html')
    return HttpResponse(template.render(request))

