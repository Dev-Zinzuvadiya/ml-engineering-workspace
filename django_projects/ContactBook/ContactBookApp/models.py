from django.db import models


# Create your models here.
class DataBases(models.Model):
    owner = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="contacts"
    )
    names = models.CharField(max_length=30)
    emails = models.EmailField(max_length=30)
    passwords = models.CharField(max_length=30)
    contact_numbers = models.CharField(max_length=15)
