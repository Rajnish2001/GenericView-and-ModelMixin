import email
from statistics import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
