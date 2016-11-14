
from django.conf.urls import url
from views import docente,cerrarSession,ConsultarProyectos,CrearProyecto, ModificarProyecto,ConsultarRecursoEstudiante,ModificarRecursoEstudiante,ConsultarRecursoDocente,ModificarRecursoDocente
urlpatterns = [
    #Mapa de rutas de la aplicacion de Proyeccion 
    url(r'^Docente/$', docente),
    url(r'^Proyectos/$', ConsultarProyectos.as_view(), name='ConsultarProyectos'),
    url(r'^CrearProyecto/$', CrearProyecto.as_view()),
    url(r'^recursoEstudiante/(?P<pk>\d+)$', ConsultarRecursoEstudiante.as_view(),name='ConsultarRecursoEstudiante'),
    url(r'^recursoDocente/(?P<pk>\d+)$', ConsultarRecursoDocente.as_view(),name='ConsultarRecursoDocente'),
    url(r'^modificarProyecto/(?P<pk>\d+)$', ModificarProyecto.as_view()),
    url(r'^modificarRecursoEstudiante/(?P<pk>\d+)$', ModificarRecursoEstudiante.as_view()),
    url(r'^modificarRecursoDocente/(?P<pk>\d+)$', ModificarRecursoDocente.as_view()),
    url(r'^CerrarSession/$', cerrarSession),
]

