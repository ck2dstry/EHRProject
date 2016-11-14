from django import forms
from .models import PatientInfo

class PostPatientInfoForm(forms.ModelForm):
    
        class Meta:
            model = PatientInfo
            fields = ('patient_id', 'patient_lastname', 'patient_firstname', 'patient_email')
            labels = {
                'patient_id': ('Patient SSN'),
                'patient_lastname': ('Last Name'),
                'patient_firstname': ('First Name'),
                'patient_email': ('Email'),
            }