from django.http import HttpResponse
from django.template import loader
from .models import Team
# Create your views here.


def players(request):
    myplayers = Team.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myplayers':myplayers,
    }
    return HttpResponse(template.render(context, request))


def detalils(request, id):
    myplayers = players.objects.get(id=id)
    templete = loader.get_template('details.html')
    context = {
        'myplayers':myplayers,
    }
    return HttpResponse(templete.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())