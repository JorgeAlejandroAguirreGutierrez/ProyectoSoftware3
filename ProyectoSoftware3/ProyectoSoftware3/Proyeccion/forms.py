# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from django import forms
from models import InformacionDescriptiva
class ProyectoForm(forms.ModelForm):

    class Meta:
        model = InformacionDescriptiva

        fields = [
            'fecha',
            'codigo',
            'numero_convenio',
            'titulo',
            'coordinador_id',
            'departamento_id',
            'facultad_id',
            'fecha_inicio',
            'fecha_final',
            'modalidad_id',
            'problema',
            'justificacion',
            'objetivo_general',
            'impacto',
            'poblacion',
            'metodologia',

      
			
        ]
        labels = {
            'fecha':'FECHA',
            'codigo':'CODIGO',
            'numero_convenio':'CONVENIO',
            'titulo':'TITULO',
            'coordinador_id':'COORDINADOR',
            'departamento_id':'DEPARTAMENTO',
            'facultad_id':'FACULTAD',
            'fecha_inicio':'FECHA INCIO',
            'fecha_final':'FECHA FINAL',
            'modalidad_id':'MODALIDAD',
            'problema':'PROBLEMA',
            'justificacion':'JUSTIFICACION',
            'objetivo_general':'OBJETIVO GENERAL',
            'impacto':'IMPACTO',
            'poblacion':'POBLACION',
            'metodologia':'METODOLOGIA',
		
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'fecha_inicio': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'fecha_final': forms.DateInput(attrs={'class':'form-control','type':'date'}),
        
        }

        
    
    

