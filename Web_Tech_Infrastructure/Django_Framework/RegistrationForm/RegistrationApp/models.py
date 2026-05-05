from django.db import models

# Create your models here.

class RecordsLength(models.Model):
    candidate_name = models.CharField(max_length = 50)
    age = models.IntegerField()
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 30)
    confirm_password = models.CharField(max_length = 30)