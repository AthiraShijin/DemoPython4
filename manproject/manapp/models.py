from django.db import models


# Create your models here.

class Persn(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name

class choose(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='piks')
    desc = models.TextField()

    def __str__(self):
        return self.name