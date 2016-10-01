from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import View
import json
from models import InformacionDescriptiva
from models import Usuario
from forms import ProyectoForm

# Create your views here.
def docente(request):
    if "cedula" in request.session:
        cedula = request.session["cedula"]
        usuario = Usuario.objects.get(cedula=cedula)
        
        return render(request, "Proyeccion/docente.html", {'nombre':usuario.nombre})
    else:
        return HttpResponseRedirect("/")
    
def proyectos(request):
    if "cedula" in request.session:
        cedula = request.session["cedula"]
        usuario = Usuario.objects.get(cedula=cedula)     
        return render(request, "Proyeccion/proyectos.html", {'nombre':usuario.nombre})
    else:
        return HttpResponseRedirect("/")
    
def cerrarSession(request):
    try:
        del request.session['cedula']
    except KeyError:
        pass
    return HttpResponseRedirect("/")

class Logear(View):
    def get(self, request, * args, ** kwargs):
        return render(request, 'inicio/login.html', {})
    def post(self, request, * args, ** kwargs):
        usuario = request.POST['usuario']
        clave = request.POST['clave']    
        try:  
            user = Usuario.objects.get(cedula=usuario, clave=clave)            
            #data = serializers.serialize('json', user, fields=('nombre'))
            response_data = {}
            response_data['respuesta'] = 'existe'  
            request.session['cedula'] = user.cedula
            request.session['identificador'] = user.id
        except Usuario.DoesNotExist:
            response_data = {}
            response_data['respuesta'] = 'noExiste'          
        return HttpResponse(json.dumps(response_data), content_type='application/json')

    
class CrearProyecto(CreateView):
    template_name = 'Proyeccion/crearProyecto.html'
    model = InformacionDescriptiva
    user = ""
    form_class = ProyectoForm
    success_url = reverse_lazy('listarProyectos')
    #fields = ['modalidad_id']
#    def post(self, request, *args, **kwargs):
#		self.object = self.get_object
#		form = self.form_class(request.POST)
#		form2 = self.second_form_class(request.POST)
#		if form.is_valid() and form2.is_valid():
#			solicitud = form.save(commit=False)
#			solicitud.persona = form2.save()
#			solicitud.save()
#			return HttpResponseRedirect(self.get_success_url())
#		else:
#			return self.render_to_response(self.get_context_data(form=form, form2=form2))
    
    def get_context_data(self, ** kwargs):
	context = super(CrearProyecto, self).get_context_data(** kwargs)
        return context

class ConsultarProyectos(View):
#    template_name='Proyeccion/consultarProyectos.html'
#    context_object_name = 'informacion_list'
#    datos=None
#    model=InformacionDescriptiva
    def get(self, request, * args, ** kwargs):
        informacion_list=InformacionDescriptiva.objects.filter(coordinador_id=request.session['identificador'])
        return render(request, "Proyeccion/consultarProyectos.html", {'informacion_list':informacion_list})
    
#    def get_queryset(self):
#        return InformacionDescriptiva.objects.filter(coordinador_id=self.datos['cedula'])
    
#    def get_context_data(self, **kwargs):
#        context = super(ArticleListView, self).get_context_data(**kwargs)
#        return context

class ModificarProyecto(UpdateView):
    template_name='Proyeccion/modificarProyecto.html'
    model=InformacionDescriptiva
    form_class = ProyectoForm
    success_url=reverse_lazy('ConsultarProyectos')
#    fields='__all__'