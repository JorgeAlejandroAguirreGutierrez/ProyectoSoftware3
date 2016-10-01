from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=200)
    cedula=models.CharField(max_length=200)
    clave=models.CharField(max_length=200)
    def __str__(self):
        return '%s'%(self.nombre)
#    def __str__(self):
#        return "{'id':%d,'nombre':'%s','cedula':'%s','clave':'%s'}"%(self.id,self.nombre,self.cedula,self.clave)
#    
class VinculacionDocente(models.Model):
    tipo=models.CharField(max_length=200)
    def __str__(self):
        return '%s'%(self.tipo)

class Docente(models.Model):
    valor_hora=models.IntegerField()
    vinculacion_id=models.ForeignKey(VinculacionDocente, on_delete=models.CASCADE)
    usuario_id=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return '%s'%(self.usuario_id)

class Departamento(models.Model):
    nombre=models.CharField(max_length=200)
    director_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    correo=models.CharField(max_length=200, null=True)
    telefono=models.CharField(max_length=200, null=True)
    def __str__(self):
        return '%s'%(self.nombre)
    
class Facultad(models.Model):
    nombre=models.CharField(max_length=200)
    decano_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    correo=models.CharField(max_length=200, null=True)
    telefono=models.CharField(max_length=200, null=True)
    def __str__(self):
        return '%s'%(self.nombre)
    
class Modalidad(models.Model):
    nombre=models.CharField(max_length=200)
    relevancia=models.IntegerField(null=True)
    def __str__(self):
        return '%s'%(self.nombre)
    
class InformacionDescriptiva(models.Model):
    fecha=models.DateField()
    codigo=models.CharField(max_length=200)
    numero_convenio=models.CharField(max_length=200)
    titulo=models.CharField(max_length=400)
    coordinador_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    departamento_id=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    facultad_id=models.ForeignKey(Facultad, on_delete=models.CASCADE)
    fecha_inicio=models.DateField()
    fecha_final=models.DateField()
    modalidad_id=models.ForeignKey(Modalidad, on_delete=models.CASCADE)
    problema=models.TextField(default='')
    justificacion=models.TextField(null=True, default='')
    objetivo_general=models.TextField(default='')
    objetivos_especificos=models.TextField(default='')
    impacto=models.TextField(null=True, default='')
    poblacion=models.TextField(null=True, default='')
    metodologia=models.TextField(null=True, default='')
    def __str__(self):
        return '%s'%(self.titulo)