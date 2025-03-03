from email.policy import default
from enum import auto
from random import choices
from time import timezone
from datetime import datetime
from django.db import models
from django.forms import CharField
from django.core.validators import MinValueValidator, MaxValueValidator

class Pokemon(models.Model):
 class PokemonType(models.TextChoices):
      WATER = 'WA'
      GRASS = 'GR'
      GHOST = 'GH'
      STEEL = 'ST'
      FAIRY = 'FA'

 name =models.CharField(max_length=30)
 type =models.CharField(max_length=30,choices=PokemonType.choices)
 hp=models.PositiveIntegerField(validators=[MinValueValidator(50, 'can not be under 50'), MaxValueValidator(350, 'can not be more than 350')])
 active =models.BooleanField(default=True)
 name_fr= models.CharField(max_length=30,default="",blank=True) 
 name_ar=models.CharField(max_length=30,default="",blank=True)
 name_jp=models.CharField(max_length=30,default="",blank=True)
 created_at=models.DateTimeField(auto_now_add=True, blank=True)
 modified_at=models.DateTimeField(auto_now=True)
#  default=datetime.now()