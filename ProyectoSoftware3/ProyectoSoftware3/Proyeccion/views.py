from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models import Usuario
from django.core.urlresolvers import reverse_lazy
import json
from django.views.generic import TemplateView

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


def inicio (request):
    return render(request, 'inicio/login.html', {})
class logear(TemplateView):
    
    def get(self, request, * args, ** kwargs):
        
        usuario = request.GET['usuario']
        clave = request.GET['clave']    
        try:  
            user = Usuario.objects.get(cedula=usuario, clave=clave)            
            #data = serializers.serialize('json', user, fields=('nombre'))
            response_data = {}
            response_data['respuesta'] = 'existe'  
            request.session['cedula'] = user.cedula
        except Usuario.DoesNotExist:
            response_data = {}
            response_data['respuesta'] = 'noExiste'
          
        return HttpResponse(json.dumps(response_data), content_type='application/json')