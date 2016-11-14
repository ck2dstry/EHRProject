from django.db import models

class PatientInfo(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    patient_lastname = models.CharField(max_length=45)
    patient_firstname = models.CharField(max_length=45)
    patient_email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'patient_info'



