
from django.conf.urls import url
from views import docente,cerrarSession,proyectos,CrearProyecto
urlpatterns = [
    url(r'^Docente/$', docente),
    url(r'^Proyectos/$', proyectos,name="listarProyectos"),
    url(r'^crearProyecto/$', CrearProyecto.as_view()),
    url(r'^CerrarSession/$', cerrarSession),
]

