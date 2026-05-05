from django.db import models

# Create your models here.


# Set all Field length
class CandidateDataBases(models.Model):
    candidate_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    contact_number = models.BigIntegerField()
