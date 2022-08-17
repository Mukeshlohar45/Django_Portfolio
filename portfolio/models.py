from django.db import models


# Create your models here.

class Person(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Subject = models.CharField(max_length=30)
    Message = models.CharField(max_length=300)
    