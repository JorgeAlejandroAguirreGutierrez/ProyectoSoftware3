
from django.conf.urls import url
from views import docente,cerrarSession
urlpatterns = [
    url(r'^Docente/$', docente),
    url(r'^CerrarSession/$', cerrarSession),
    
]
