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
from forms import InformacionDescriptivaForm

# Create your views here.
#En esta vistas se valida el login de acceso a la aplicacion
def docente(request):
    if "cedula" in request.session:
        cedula = request.session["cedula"]
        usuario = Usuario.objects.get(cedula=cedula)
        return render(request, "Proyeccion/docente.html", {'nombre':usuario.nombre})
    else:
        return HttpResponseRedirect("/")
#     
def proyectos(request):
    if "cedula" in request.session:
        cedula = request.session["cedula"]
        usuario = Usuario.objects.get(cedula=cedula)     
        return render(request, "Proyeccion/proyectos.html", {'nombre':usuario.nombre})
    else:
        return HttpResponseRedirect("/")
#Este metodo nos cierra la session      
def cerrarSession(request):
    try:
        #Destruye las variable creada al logearse el usuario
        del request.session['cedula']
    except KeyError:
        pass
    return HttpResponseRedirect("/")

#Vista que nos renderiza al el home de la aplicacion y nos crea una variable 
#de Session para el control de sessiones 
class Logear(View):
    #Renderizo el template para el logeo
    def get(self, request, * args, ** kwargs):
        return render(request, 'inicio/login.html', {})
    #Se crea el inicion de seesion para el usuario validando la cedula 
    #con la password ingresada
    def post(self, request, * args, ** kwargs):
        usuario = request.POST['usuario']
        clave = request.POST['clave']    
<<<<<<< HEAD
        try:
            
            user = Usuario.objects.get(cedula=usuario, clave=clave)            
            #data = serializers.serialize('json', user, fields=('nombre'))
=======
        try:  
            user = Usuario.objects.get(cedula=usuario, clave=clave)
>>>>>>> refs/remotes/origin/rama-jorge2
            response_data = {}
            response_data['respuesta'] = 'existe'  
            request.session['cedula'] = user.cedula
            request.session['identificador'] = user.id
        except Usuario.DoesNotExist:
            response_data = {}
            response_data['respuesta'] = 'noExiste'          
        return HttpResponse(json.dumps(response_data), content_type='application/json')
#Vista crear Proyecto: Esta se basa en el modelo informacion descriptiva 
#Donde el usuario registra un proyecto que se va realizar    
class CrearProyecto(CreateView):
    template_name = 'Proyeccion/crearProyecto.html'
    model = InformacionDescriptiva
    form_class = InformacionDescriptivaForm
    nombre = ""
    success_url = reverse_lazy('listarProyectos')
<<<<<<< HEAD
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
    #Valido si hay una session existente o si no renderizo de nuevo a la pagina de 
    #Login
=======
>>>>>>> refs/remotes/origin/rama-jorge2
    def get(self,request, *args, **kwargs):
        #validamos la session
        if "cedula" in request.session:
            cedula = request.session["cedula"]
            usuario = Usuario.objects.get(cedula=cedula) 
            self.nombre=usuario.nombre
            return super(CrearProyecto, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/")
    #Utilizo para crear una variable en el contexto 
    #para asi poderla mandar al template a renderizar que seria el home de la 
    #aplicaciones
    def get_context_data(self, ** kwargs):
	context = super(CrearProyecto, self).get_context_data(** kwargs)
        context['nombre'] = self.nombre
        return context
#Vista Consultar Proyectos muestra los difentes proyectos que han sido
#registrados por parte de algun docente coordinador
class ConsultarProyectos(View):
<<<<<<< HEAD

#    template_name='Proyeccion/consultarProyectos.html'
#    context_object_name = 'informacion_list'
#    datos=None
#    model=InformacionDescriptiva
    #Valido si hay una session existente o si no renderizo de nuevo a la pagina de 
    #Login
=======
>>>>>>> refs/remotes/origin/rama-jorge2
    def get(self, request, * args, ** kwargs):
        informacion_list=InformacionDescriptiva.objects.filter(coordinador_id=request.session['identificador'])
        if "cedula" in request.session:
            cedula = request.session["cedula"]
            usuario = Usuario.objects.get(cedula=cedula) 
            nombre=usuario.nombre
            return render(request, "Proyeccion/consultarProyectos.html", {'informacion_list':informacion_list,'nombre':nombre})
        else:
            return HttpResponseRedirect("/")
<<<<<<< HEAD
        
  
#    def get_queryset(self):
#        return InformacionDescriptiva.objects.filter(coordinador_id=self.datos['cedula'])
    
#    def get_context_data(self, **kwargs):
#        context = super(ArticleListView, self).get_context_data(**kwargs)
#        return context
#Nos muestra el proyecto seleccionado para hacerle alguna modificacion a la 
#informacion descriptiva del proyecto 
=======

>>>>>>> refs/remotes/origin/rama-jorge2
class ModificarProyecto(UpdateView):
    template_name='Proyeccion/modificarProyecto.html'
    model= InformacionDescriptiva
    form_class = InformacionDescriptivaForm
    nombre=""
    success_url=reverse_lazy('ConsultarProyectos')
    #Valido si hay una session existente o si no renderizo de nuevo a la pagina de 
    #Login
    def get(self,request, *args, **kwargs):
        if "cedula" in request.session:
            cedula = request.session["cedula"]
            usuario = Usuario.objects.get(cedula=cedula) 
            self.nombre=usuario.nombre
            return super(ModificarProyecto, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/")
    #Utilizo para crear una variable en el contexto 
    #para asi poderla mandar al template a renderizar que seria el home de la 
    #aplicaciones
    def get_context_data(self, ** kwargs):
	context = super(ModificarProyecto, self).get_context_data(** kwargs)
        context['nombre'] = self.nombre
        return context
