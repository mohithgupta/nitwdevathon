from django.db import models

# Create your models here.
class Branch(models.Model):
    #username = models.EmailField()
    username = models.CharField(max_length = 20)
    branch = models.CharField(max_length = 20)
    c1 = models.CharField(max_length = 20)
    c2 = models.CharField(max_length = 20)
    c3 = models.CharField(max_length = 20)
    c4 = models.CharField(max_length = 20)
    c5 = models.CharField(max_length = 20)
    c6 = models.CharField(max_length = 20)
    c7 = models.CharField(max_length = 20)

#class Registered(models.Model):
#    username = 