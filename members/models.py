
from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

class Court(models.Model):
  Number = models.CharField(max_length=5)
  Is_occupied= models.BooleanField(null=True)
  date_time_occupation= models.DateTimeField(null=True)


  
