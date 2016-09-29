from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models import Usuario
from django.core.urlresolvers import reverse_lazy


# Create your views here.
def docente(request):
    if "cedula" in request.session:
        cedula=request.session["cedula"]
        usuario=Usuario.objects.get(cedula=cedula)
        
        return render(request,"Proyeccion/docente.html",{'nombre':usuario.nombre})
    else:
        return HttpResponseRedirect("/")
def cerrarSession(request):
    try:
        del request.session['cedula']
    except KeyError:
        pass
    return HttpResponseRedirect("/")
    