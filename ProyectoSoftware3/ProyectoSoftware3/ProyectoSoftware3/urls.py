from django.conf.urls import url,include
from django.contrib import admin
from Proyeccion.views import inicio,logear
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', inicio),
    url(r'^Login/$', logear.as_view()),
    url(r'^Proyeccion/', include("Proyeccion.urls")),
    
    
]