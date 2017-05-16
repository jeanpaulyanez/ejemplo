from django.http import HttpResponse
from django.template import Context, loader
from hola.models import TIPO_ORIGEN,WEB_GEO

def index2(request):
    return HttpResponse("hola mundo")

def index3(request):
    tipolist = TIPO_ORIGEN.objects.all()
    tmpl = loader.get_template("hola/index.html")
    cont = Context({'param': geolist})
    return HttpResponse(tmpl.render(cont))

def index(request):
    geolist = WEB_GEO.objects.all()
    tipolist = TIPO_ORIGEN.objects.all()
    tmpl = loader.get_template("hola/index.html")
    cont = Context({'param': geolist, 'param2':tipolist, 'param3':'hola'})
    