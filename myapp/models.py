from django.db import models

# Create your models here.

class contact(models.Model):
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    email = models.EmailField()
    comment = models.TextField()

class register(models.Model):
    Name = models.CharField(max_length=100)
    email = models.EmailField()
    pwd = models.CharField(max_length=50)
    cpwd = models.CharField(max_length=50)