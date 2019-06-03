from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=99)
    lastname = models.CharField(max_length=99)
    age = models.IntegerField()
    tel = models.CharField(max_length=99)