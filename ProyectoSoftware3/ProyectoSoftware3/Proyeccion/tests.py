from django.test import TestCase
from models import *
from django.core.exceptions import ValidationError

# Create your tests here.

class UsuarioTest(TestCase):
    def setUp(self):
        Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
    def test_loginValidate(self):
        usuario = Usuario(nombre="GIAN", cedula="1053855850", clave="12345")
        try:  
            usuarioLogin = Usuario.objects.get(cedula=usuario.cedula, clave=usuario.clave)
            self.assertTrue(True)
        except:             
            self.assertTrue(False)
            
    def test_loginInvalidate(self):
        usuario = Usuario(nombre="GIAN", cedula="1053855850", clave="123456")
        try:  
            usuarioLogin = Usuario.objects.get(cedula=usuario.cedula, clave=usuario.clave)
            self.assertTrue(False)
        except:             
            self.assertTrue(True)   
            
class RegisterProjectTest(TestCase): 
    def setUp(self):
        Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        
        
        
    def test_registerProjectValidate(self):
      
        docente= Docente.objects.get(valor_hora=35000)
        departamento= Departamento.objects.get(nombre="SALUD INTERNA")
        facultad= Facultad.objects.get(nombre="CIENCIAS PARA LA SALUD")
        modalidad= Modalidad.objects.get(nombre="SEMINARIO",)
        try:     
            proyecto=InformacionDescriptiva(fecha="2016-05-05", codigo="VPU-000", 
            numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
            coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
            fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
            problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
            objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
            impacto="IMPACTO PROYECTO", poblacion="POBLACION DEL PROYECTO", metodologia="METODOLOGIA PROYECTO")
            proyecto.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_registerProjectInvalidateEmptyFacultad(self):
        docente= Docente.objects.get(valor_hora=35000)
        departamento= Departamento.objects.get(nombre="SALUD INTERNA")
        facultad= Facultad.objects.get(nombre="CIENCIAS PARA LA SALUD")
        modalidad= Modalidad.objects.get(nombre="SEMINARIO",)
        
        try:     
            proyecto=InformacionDescriptiva(fecha="2016-05-05", codigo="VPU-000", 
            numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
            coordinador_id=docente, departamento_id=departamento, facultad_id=None,
            fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
            problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
            objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
            impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO")
            proyecto.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
            
    def test_registerProjectInvalidateEmptyDocente(self):
        docente= Docente.objects.get(valor_hora=35000)
        departamento= Departamento.objects.get(nombre="SALUD INTERNA")
        facultad= Facultad.objects.get(nombre="CIENCIAS PARA LA SALUD")
        modalidad= Modalidad.objects.get(nombre="SEMINARIO",)
        
        try:     
            proyecto=InformacionDescriptiva(fecha="2016-05-05", codigo="VPU-000", 
            numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
            coordinador_id=None, departamento_id=departamento, facultad_id=facultad,
            fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
            problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
            objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
            impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO")
            proyecto.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
class updateProjectTest(TestCase):
    
    def setUp(self):
        modalidad=Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        departamento=Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        facultad=Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        
        InformacionDescriptiva.objects.create(fecha="2016-05-05", codigo="VPU-000", 
        numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
        coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
        fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
        problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
        objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
        impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO")
        
        
        
    def test_updateProjectValidate(self):
        try:
            proyecto = InformacionDescriptiva.objects.get(codigo="VPU-000")
            proyecto.titulo="CONGRESO DE MEDICINA"
            proyecto.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_updateProjectInvalidateEmptyTitulo(self):
        try:
            proyecto = InformacionDescriptiva.objects.get(codigo="VPU-000")
            proyecto.titulo=None
            proyecto.save()
            self.assertTrue(False) 
        except:       
            self.assertTrue(True)
    
    def test_updateProjectInvalidateEmptyDepartamento(self):
        try:
            proyecto = InformacionDescriptiva.objects.get(codigo="VPU-000")
            proyecto.departamento=None
            proyecto.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
        
            
            
 