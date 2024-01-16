from django.db import models

# Create your models here.
class datainsert(models.Model):
        title = models.CharField(max_length=200, default="x")
        name = models.CharField(max_length=200, default="x")
        play = models.CharField(max_length=200, default="x")
        play2 = models.CharField(max_length=200, default="x")
class post(models.Model):
    author = models.CharField(max_length=200, default="x")
    title = models.CharField(max_length=200, default="x")
    todaysmood = models.CharField(max_length=200, default="x")
    pocet = models.DecimalField(max_digits=10, decimal_places=2)

