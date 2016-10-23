
from django.conf.urls import url
from views import docente,cerrarSession,ConsultarProyectos,CrearProyecto, ModificarProyecto
urlpatterns = [
    #Mapa de rutas de la aplicacion de Proyeccion 
    url(r'^Docente/$', docente),
    url(r'^Proyectos/$', ConsultarProyectos.as_view(), name='ConsultarProyectos'),
    url(r'^CrearProyecto/$', CrearProyecto.as_view()),
    url(r'^modificarProyecto/(?P<pk>\d+)$', ModificarProyecto.as_view()),
    url(r'^CerrarSession/$', cerrarSession),
]

