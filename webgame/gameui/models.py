from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    isPublic = models.BooleanField(default=False)

class Pet(models.Model):
    name = models.CharField(max_length=32)
    genes = models.CharField(max_length=32)
    age = models.FloatField(default=0.0)
    master = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.BooleanField(default=False)
    letterId = models.CharField(max_length=255)

class Egg(models.Model):
    color = models.CharField(max_length=6)
    mother = models.ForeignKey(Pet, related_name='egg_mother', on_delete=models.PROTECT, null=True)
    father = models.ForeignKey(Pet, related_name='egg_father', on_delete=models.PROTECT, null=True)
    master = models.ForeignKey(User, on_delete=models.CASCADE)