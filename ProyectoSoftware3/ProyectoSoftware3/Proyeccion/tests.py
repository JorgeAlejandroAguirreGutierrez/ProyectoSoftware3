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
        try: 
            proyecto=Proyecto(activo=True)
            docente= Docente.objects.get(valor_hora=35000)
            departamento= Departamento.objects.get(nombre="SALUD INTERNA")
            facultad= Facultad.objects.get(nombre="CIENCIAS PARA LA SALUD")
            modalidad= Modalidad.objects.get(nombre="SEMINARIO",)
            proyecto.save()
            informacion=InformacionDescriptiva(fecha="2016-05-05", codigo="VPU-000", 
            numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
            coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
            fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
            problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
            objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
            impacto="IMPACTO PROYECTO", poblacion="POBLACION DEL PROYECTO", metodologia="METODOLOGIA PROYECTO", proyecto_id=proyecto)
            informacion.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_registerProjectInvalidateEmptyFacultad(self):
        try: 
            proyecto=Proyecto(activo=True)
            docente= Docente.objects.get(valor_hora=35000)
            departamento= Departamento.objects.get(nombre="SALUD INTERNA")
            modalidad= Modalidad.objects.get(nombre="SEMINARIO",)
            proyecto.save()
            
            informacion=InformacionDescriptiva(fecha="2016-05-05", codigo="VPU-000", 
            numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
            coordinador_id=docente, departamento_id=departamento, facultad_id=None,
            fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
            problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
            objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
            impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO", proyecto_id=proyecto)
            informacion.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
            
    def test_registerProjectInvalidateEmptyDocente(self):
        try:
            proyecto=Proyecto(activo=True)
            departamento= Departamento.objects.get(nombre="SALUD INTERNA")
            facultad= Facultad.objects.get(nombre="CIENCIAS PARA LA SALUD")
            modalidad= Modalidad.objects.get(nombre="SEMINARIO",)
            
            proyecto.save() 
            informacion=InformacionDescriptiva(fecha="2016-05-05", codigo="VPU-000", 
            numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
            coordinador_id=None, departamento_id=departamento, facultad_id=facultad,
            fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
            problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
            objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
            impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO", proyecto_id=proyecto)
            informacion.save()
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
        
        proyecto=Proyecto.objects.create(activo=True)
        
        InformacionDescriptiva.objects.create(fecha="2016-05-05", codigo="VPU-000", 
        numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
        coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
        fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
        problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
        objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
        impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO", proyecto_id=proyecto)
        
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
        

class DeleteProjectTest(TestCase): 
    def setUp(self):
        modalidad=Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        departamento=Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        facultad=Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        
        proyecto=Proyecto.objects.create(activo=True)
        
        InformacionDescriptiva.objects.create(fecha="2016-05-05", codigo="VPU-000", 
        numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
        coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
        fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
        problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
        objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
        impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO", proyecto_id=proyecto)
        
            
    def test_DeleteProjectValidate(self):
        try:     
            proyecto=InformacionDescriptiva.objects.get(codigo="VPU-000")
            proyecto.delete()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
    
    def test_DeleteProjectInvalidate(self):
        try:     
            proyecto=InformacionDescriptiva.objects.get(codigo="VPU-001")
            proyecto.delete()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
    
            
class RegisterTeachingTest(TestCase): 
    def setUp(self):
        modalidad=Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        departamento=Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        facultad=Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        
        proyecto=Proyecto.objects.create(activo=True)
        
        InformacionDescriptiva.objects.create(fecha="2016-05-05", codigo="VPU-000", 
        numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
        coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
        fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
        problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
        objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
        impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO", proyecto_id=proyecto)
        
        
        
        
    def test_registerTeachingValidate(self):
        try:
            docente= Docente.objects.get(valor_hora=35000)
            proyecto=Proyecto.objects.all()
            recursoDocente=RecursoDocente(numero_horas_semana=4, fecha_inicio="2016-07-08", fecha_final="2016-07-09", tipo_financiacion="RECURRENTE", docente_id=docente, proyecto_id=proyecto[0])
            recursoDocente.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_registerTeachingInvalidateEmptyNumeroHoras(self):
        docente= Docente.objects.get(valor_hora=35000)
        proyecto= Proyecto.objects.all()
        
        try:     
            recursoDocente=RecursoDocente(numero_horas_semana=None, fecha_inicio="2016-07-08", fecha_final="2016-07-09", tipo_financiacion="RECURRENTE", docente_id=docente, proyecto_id=proyecto[0])
            recursoDocente.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
            
    def test_registerTeachingInvalidateEmptyFechaFinal(self):
        docente= Docente.objects.get(valor_hora=35000)
        proyecto= Proyecto.objects.all()
        try:     
            recursoDocente=RecursoDocente(numero_horas_semana=4, fecha_inicio="2016-07-12", fecha_final=None, tipo_financiacion="RECURRENTE", docente_id=docente, proyecto_id=proyecto[0])
            recursoDocente.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
class updateTeachingTest(TestCase):
    
    def setUp(self):
        modalidad=Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        departamento=departamento=Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        facultad=Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        
        proyecto=Proyecto.objects.create(activo=True)
        
        InformacionDescriptiva.objects.create(fecha="2016-05-05", codigo="VPU-000", 
        numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
        coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
        fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
        problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
        objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
        impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO", proyecto_id=proyecto)
        
        RecursoDocente.objects.create(numero_horas_semana=2, fecha_inicio="2016-07-12", fecha_final="2016-07-18", tipo_financiacion="RECURRENTE", docente_id=docente, proyecto_id=proyecto)
        
    def test_updateTeachingValidate(self):
        try:
            recursoDocente=RecursoDocente.objects.get(numero_horas_semana=2)
            recursoDocente.numero_horas_semana=10
            recursoDocente.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_updateTeachingInvalidateEmptyNumeroHorasSemana(self):
        try:
            recursoDocente=RecursoDocente.objects.get(numero_horas_semana=10)
            recursoDocente.numero_horas_semana=None
            recursoDocente.save()
            self.assertTrue(False) 
        except:       
            self.assertTrue(True)
    
    def test_updateTeachingInvalidateEmptyTipoFinanciacion(self):
        try:
            recursoDocente=RecursoDocente.objects.get(numero_horas_semana=10)
            recursoDocente.tipo_financiacion=None
            recursoDocente.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
class RegisterStudentTest(TestCase): 
    def setUp(self):
        modalidad=Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        departamento=Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        facultad=Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        facultad2=Facultad.objects.create(nombre="INGENIERIAS", decano_id=docente,
        correo="INGENIERIAS@UCALDAS.EDU.CO", telefono="8750584")
        Programa.objects.create(nombre="INGENIERIA DE SISTEMAS Y COMPUTACION", director_id=docente, facultad_id=facultad2)
        
        proyecto=Proyecto.objects.create(activo=True)
        
        InformacionDescriptiva.objects.create(fecha="2016-05-05", codigo="VPU-000", 
        numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
        coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
        fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
        problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
        objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
        impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO", proyecto_id=proyecto)
        
        
        
    def test_registerStudentValidate(self):
        try:
            programa=Programa.objects.get(nombre="INGENIERIA DE SISTEMAS Y COMPUTACION")
            proyecto=Proyecto.objects.all()
            recursoEstudiante=RecursoEstudiante(nombre="JULIAN",codigo="1701313530",semestre=6,numero_horas_semana=5, fecha_inicio="2016-07-12", fecha_final="2016-07-18", programa_id=programa, proyecto_id=proyecto[0])
            recursoEstudiante.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_registerStudentInvalidateEmptyCodigo(self):
        programa=Programa.objects.get(nombre="INGENIERIA DE SISTEMAS Y COMPUTACION")
        proyecto= Proyecto.objects.all()
        try:     
            recursoEstudiante=RecursoEstudiante(nombre="JULIAN",codigo=None,semestre=6,numero_horas_semana=5, fecha_inicio="2016-07-12", fecha_final="2016-07-18", programada_id=programa, proyecto_id=proyecto[0])
            recursoEstudiante.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
            
    def test_registerStudentInvalidateEmptyNumeroHorasSemana(self):
        programa= Programa.objects.get(nombre="INGENIERIA DE SISTEMAS Y COMPUTACION")
        proyecto= Proyecto.objects.all()
        try:     
            recursoEstudiante=RecursoEstudiante(nombre="JULIAN",codigo="1701313530",semestre=6,numero_horas_semana=None, fecha_inicio="2016-07-12", fecha_final="2016-07-18", programada_id=programa, proyecto_id=proyecto[0])
            recursoEstudiante.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
class updateStudentTest(TestCase):
    
    def setUp(self):
        modalidad=Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        departamento=departamento=Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        facultad=Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        facultad2=Facultad.objects.create(nombre="INGENIERIAS", decano_id=docente,
        correo="INGENIERIAS@UCALDAS.EDU.CO", telefono="8750584")
        programa=Programa.objects.create(nombre="INGENIERIA DE SISTEMAS Y COMPUTACION", director_id=docente, facultad_id=facultad2)
        
        proyecto=Proyecto.objects.create(activo=True)
        
        InformacionDescriptiva.objects.create(fecha="2016-05-05", codigo="VPU-000", 
        numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
        coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
        fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
        problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
        objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
        impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO", proyecto_id=proyecto)
 
        RecursoEstudiante.objects.create(nombre="JULIAN",codigo="1701313530",semestre=6,numero_horas_semana=5, fecha_inicio="2016-07-12", fecha_final="2016-07-18", programa_id=programa, proyecto_id=proyecto)
        
    def test_updateStudentValidate(self):
        try:
            recursoEstudiante=RecursoEstudiante.objects.get(codigo="1701313530")
            recursoEstudiante.nombre="CRISTIAN"
            recursoEstudiante.numero_horas_semana=10
            recursoEstudiante.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_updateTeachingInvalidateEmptyTipoCodigo(self):
        try:
            recursoEstudiante=RecursoEstudiante.objects.get(codigo="1701313530")
            recursoEstudiante.codigo=None
            recursoEstudiante.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
    def test_updateStudentInvalidateEmptyNumeroHorasSemana(self):
        try:
            recursoEstudiante=RecursoEstudiante.objects.get(codigo="1701313530")
            recursoEstudiante.numero_horas_semana=None
            recursoEstudiante.save()
            self.assertTrue(False) 
        except:       
            self.assertTrue(True)
                 
class IntegrativeTest(TestCase): 
    def setUp(self):
        Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario1=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        usuario2=Usuario.objects.create(nombre="GIAN", cedula="1053855855", clave="123")
        vinculacion1=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        vinculacion2=VinculacionDocente.objects.create(tipo="DOCENTE OCASIONAL")
        docente1=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion1, usuario_id=usuario1)
        docente2=Docente.objects.create(valor_hora=45000, vinculacion_id=vinculacion2, usuario_id=usuario2)
        Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente1, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        facultad=Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente2,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        Programa.objects.create(nombre="MEDICINA", director_id=docente2, facultad_id=facultad)
        
    def test_registerProjectTeachingStudentValidate(self):
        try: 
            docente1= Docente.objects.get(valor_hora=35000)
            docente2= Docente.objects.get(valor_hora=45000)
            departamento= Departamento.objects.get(nombre="SALUD INTERNA")
            facultad= Facultad.objects.get(nombre="CIENCIAS PARA LA SALUD")
            modalidad= Modalidad.objects.get(nombre="SEMINARIO")
            programa=Programa.objects.get(nombre="MEDICINA")
            proyecto=Proyecto(activo=True)
            proyecto.save()
            informacion=InformacionDescriptiva(fecha="2016-05-05", codigo="VPU-000", 
            numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
            coordinador_id=docente1, departamento_id=departamento, facultad_id=facultad,
            fecha_inicio="2016-07-07", fecha_final="2016-08-08", modalidad_id=modalidad, 
            problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
            objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
            impacto="IMPACTO PROYECTO", poblacion="POBLACION DEL PROYECTO", metodologia="METODOLOGIA PROYECTO", proyecto_id=proyecto)
            informacion.save()
            recursoDocente=RecursoDocente(docente_id=docente2, numero_horas_semana=5, fecha_inicio="2016-05-10", fecha_final="2016-05-25", tipo_financiacion="RECURRENTE",proyecto_id=proyecto)
            recursoDocente.save()
            recursoEstudiante=RecursoEstudiante(nombre="PABLO",codigo="7854125",programa_id=programa, semestre=4, numero_horas_semana=3, fecha_inicio="2016-05-10", fecha_final="2016-05-25",proyecto_id=proyecto)
            recursoEstudiante.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_registerProjectTeachingStudentInvalidateEmptyDocente(self):
        try: 
            docente1= Docente.objects.get(valor_hora=35000)
#            docente2= Docente.objects.get(valor_hora=45000)
            departamento= Departamento.objects.get(nombre="SALUD INTERNA")
            facultad= Facultad.objects.get(nombre="CIENCIAS PARA LA SALUD")
            modalidad= Modalidad.objects.get(nombre="SEMINARIO")
            programa=Programa.objects.get(nombre="MEDICINA")
            proyecto=Proyecto(activo=True)
            proyecto.save()
            informacion=InformacionDescriptiva(fecha="2016-05-05", codigo="VPU-000", 
            numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
            coordinador_id=docente1, departamento_id=departamento, facultad_id=facultad,
            fecha_inicio="2016-07-07", fecha_final="2016-08-08", modalidad_id=modalidad, 
            problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
            objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
            impacto="IMPACTO PROYECTO", poblacion="POBLACION DEL PROYECTO", metodologia="METODOLOGIA PROYECTO", proyecto_id=proyecto)
            informacion.save()
            recursoDocente=RecursoDocente(docente_id=None, numero_horas_semana=5, fecha_inicio="2016-05-10", fecha_final="2016-05-25", tipo_financiacion="RECURRENTE",proyecto_id=proyecto)
            recursoDocente.save()
            recursoEstudiante=RecursoEstudiante(nombre="PABLO",codigo="7854125",programa_id=programa, semestre=4, numero_horas_semana=3, fecha_inicio="2016-05-10", fecha_final="2016-05-25", proyecto_id=proyecto)
            recursoEstudiante.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
            
    def test_registerProjectTeachingStudentInvalidateEmptyCodigo(self):
        try: 
            docente1= Docente.objects.get(valor_hora=35000)
            docente2= Docente.objects.get(valor_hora=45000)
            departamento= Departamento.objects.get(nombre="SALUD INTERNA")
            facultad= Facultad.objects.get(nombre="CIENCIAS PARA LA SALUD")
            modalidad= Modalidad.objects.get(nombre="SEMINARIO")
            programa=Programa.objects.get(nombre="MEDICINA")
            proyecto=Proyecto(activo=True)
            proyecto.save()
            informacion=InformacionDescriptiva(fecha="2016-05-05", codigo=None, 
            numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
            coordinador_id=docente1, departamento_id=departamento, facultad_id=facultad,
            fecha_inicio="2016-07-07", fecha_final="2016-08-08", modalidad_id=modalidad, 
            problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
            objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
            impacto="IMPACTO PROYECTO", poblacion="POBLACION DEL PROYECTO", metodologia="METODOLOGIA PROYECTO", proyecto_id=proyecto)
            informacion.save()
            recursoDocente=RecursoDocente(docente_id=docente2, numero_horas_semana=5, fecha_inicio="2016-05-10", fecha_final="2016-05-25", tipo_financiacion="RECURRENTE",proyecto_id=proyecto)
            recursoDocente.save()
            recursoEstudiante=RecursoEstudiante(nombre="PABLO",codigo="7854125",programa_id=programa, semestre=4, numero_horas_semana=3, fecha_inicio="2016-05-10", fecha_final="2016-05-25", proyecto_id=proyecto)
            recursoEstudiante.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)