from django.db import models
from operator import mod 

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=50)
    email=models.TextField(max_length=50)
    phone_number=models.IntegerField(max_length=50)
    college=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)