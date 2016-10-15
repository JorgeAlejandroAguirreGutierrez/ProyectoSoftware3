from django.test import TestCase
from models import Usuario
# Create your tests here.

class UsuarioTest(TestCase):
    def setUp(self):
        Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
    def test_loginValidate(self):
        usuario = Usuario(nombre="GIAN", cedula="1053855850", clave="12345")
        try:  
            usuarioLogin = Usuario.objects.get(cedula=usuario.cedula, clave=usuario.clave)
            self.assertTrue(True)
        except Usuario.DoesNotExist:             
            self.assertTrue(False)
            
    def test_loginInvalidate(self):
        usuario = Usuario(nombre="GIAN", cedula="1053855850", clave="123456")
        try:  
            usuarioLogin = Usuario.objects.get(cedula=usuario.cedula, clave=usuario.clave)
            self.assertTrue(False)
        except Usuario.DoesNotExist:             
            self.assertTrue(True)   
            
class RegisterProjectTest(TestCase):
    def setUp(self):
        Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente, correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        
    def test_registerProjectValidate(self):
        docente= Usuario.objects.get(id=1);
        departamento= Departamento.objects.get(id=1);
        facultad= Facultad.objects.get(id=1);
        modalidad= Modalidad.objects.get(id=1);
        proyecto=InformacionDescriptiva(fecha="2016-10-10", codigo="VPU-000", numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,fecha_inicio="2016-05-05", fecha_final="2016-09-09",modalidad_id=modalidad, problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", objetivo_general="OBJETIVO PROYECTO", objectivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", impacto="IMPACTO PROYECTO", poblacion="POBLACION PROYECTO", metodologia="METODOLOGIA PROYECTO")    
      
            
 