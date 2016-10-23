from __future__ import unicode_literals

from django.db import models

# Create your models here.
#Modelo Usuario: Entidad que permite el registro de los usuarios que van utilizar el sistema
class Usuario(models.Model):
    nombre=models.CharField(max_length=200)
    cedula=models.CharField(max_length=200)
    clave=models.CharField(max_length=200)
    def __str__(self):
        return '%s'%(self.nombre)
#    def __str__(self):
#        return "{'id':%d,'nombre':'%s','cedula':'%s','clave':'%s'}"%(self.id,self.nombre,self.cedula,self.clave)
#    
#Modelo vinculacionDocente:Este modelo nos indica las difetentes vinculaciones Docente
#que tiene el sitema (Catedratico,Planta,Ocasional)
class VinculacionDocente(models.Model):
    tipo=models.CharField(max_length=200)
    def __str__(self):
        return '%s'%(self.tipo)
#Modelo Docente: Entidad donde se almacena los diferentes profesores que van a 
#coordinar los proyectos 
class Docente(models.Model):
    valor_hora=models.IntegerField()
    vinculacion_id=models.ForeignKey(VinculacionDocente, on_delete=models.CASCADE)
    usuario_id=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return '%s'%(self.usuario_id)
#Modelo Departamento:Define los departamento a los cuales se inscriben los proyectos 
class Departamento(models.Model):
    nombre=models.CharField(max_length=200)
    director_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    correo=models.CharField(max_length=200, null=True)
    telefono=models.CharField(max_length=200, null=True)
    def __str__(self):
        return '%s'%(self.nombre)
#Modelo Facultad: Define las facultades a las cuales se definen los proyectos    
class Facultad(models.Model):
    nombre=models.CharField(max_length=200)
    decano_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    correo=models.CharField(max_length=200, null=True)
    telefono=models.CharField(max_length=200, null=True)
    def __str__(self):
        return '%s'%(self.nombre)
#Modelo Modalidad:Entidad que define los diferentes tipos de proyectos     
class Modalidad(models.Model):
    nombre=models.CharField(max_length=200)
    relevancia=models.IntegerField(null=True)
    def __str__(self):
        return '%s'%(self.nombre)
#Modelo informacion Descriptiva: Esta estructura nos almacena todo el contenido del proyecto
#con sus diferentes relaciones con entidades creadas anteriormente
class InformacionDescriptiva(models.Model):
    
    fecha=models.DateField(null=False, blank=False)
    codigo=models.CharField(null=False, blank=False,max_length=200)
    numero_convenio=models.CharField(null=False, blank=False,max_length=200)
    titulo=models.CharField(null=False, blank=False,max_length=400)
    coordinador_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    departamento_id=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    facultad_id=models.ForeignKey(Facultad, on_delete=models.CASCADE)
    fecha_inicio=models.DateField(null=False, blank=False)
    fecha_final=models.DateField(null=False, blank=False)
    modalidad_id=models.ForeignKey(Modalidad, on_delete=models.CASCADE)
    problema=models.TextField(null=False, blank=False)
    justificacion=models.TextField(null=False, blank=False)
    objetivo_general=models.TextField(null=False, blank=False)
    objetivos_especificos=models.TextField(null=False, blank=False)
    impacto=models.TextField(null=False, blank=False)
    poblacion=models.TextField(null=False, blank=False)
    metodologia=models.TextField(null=False, blank=False)
   
    def __str__(self):
        return '%s'%(self.titulo)