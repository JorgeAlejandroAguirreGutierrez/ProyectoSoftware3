# Create your views here.

from Proyeccion.models import Usuario
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import json
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



            
            
        

        
    
    