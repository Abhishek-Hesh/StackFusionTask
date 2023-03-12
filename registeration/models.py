from django.db import models

class Person(models.Model):
     name = models.CharField(max_length=25)
     dob = models.DateField()
     email = models.EmailField(max_length=25)
     phone_no = models.IntegerField()