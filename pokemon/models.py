from email.policy import default
from random import choices
from time import timezone

from django.db import models
from django.forms import CharField

class Pokemon(models.Model):
 class PokemonType(models.TextChoices):
      WATER = 'WA'
      GRASS = 'GR'
      GHOST = 'GH'
      STEEL = 'ST'
      FAIRY = 'FA'

 name =models.CharField(max_length=30)
 type =models.CharField(max_length=30,choices=PokemonType.choices)
 hp=models.PositiveIntegerField()
 active =models.BooleanField(default=True)
 name_fr= models.CharField(max_length=30,default="",blank=True) 
 name_ar=models.CharField(max_length=30,default="",blank=True)
 name_jp=models.CharField(max_length=30,default="",blank=True)
 created_at=models.DateTimeField()
 modified_at=models.DateTimeField(auto_now=True)