from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=200)
    cedula=models.CharField(max_length=200)
    clave=models.CharField(max_length=200)
    
class VinculacionDocente(models.Model):
    tipo=models.CharField(max_length=200)
    
class Docente(models.Model):
    valor_hora=models.IntegerField()
    vinculacion_id=models.ForeignKey(VinculacionDocente, on_delete=models.CASCADE)
    usuario_id=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class Departamento(models.Model):
    nombre=models.CharField(max_length=200)
    director_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    correo=models.CharField(max_length=200, null=True)
    telefono=models.CharField(max_length=200, null=True)
    
class Facultad(models.Model):
    nombre=models.CharField(max_length=200)
    decano_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    correo=models.CharField(max_length=200, null=True)
    telefono=models.CharField(max_length=200, null=True)
    
class Modalidad(models.Model):
    nombre=models.CharField(max_length=200)
    relevancia=models.IntegerField(null=True)
    
class InformacionDescriptiva(models.Model):
    fecha=models.DateField()
    codigo=models.CharField(max_length=200)
    numero_convenio=models.CharField(max_length=200)
    titulo=models.CharField(max_length=200)
    coordinador_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    departamento_id=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    facultad_id=models.ForeignKey(Facultad, on_delete=models.CASCADE)
    fecha_inicio=models.DateField()
    fecha_final=models.DateField()
    modalidad_id=models.ForeignKey(Modalidad, on_delete=models.CASCADE)
    problema=models.CharField(max_length=200)
    justificacion=models.CharField(max_length=200, null=True)
    objetivo_general=models.CharField(max_length=200)
    impacto=models.CharField(max_length=200, null=True)
    poblacion=models.CharField(max_length=200, null=True)
    metodologia=models.CharField(max_length=200, null=True)
    
class ObjetivoEspelcifico(models.Model):
    objetivo=models.CharField(max_length=200, null=True)
    informacion_descriptiva_id=models.ForeignKey(InformacionDescriptiva, on_delete=models.CASCADE)
