from django.db import models

name =models.CharField(max_lenght=30)
 type =models.CharField(max_lenght=30,choices=PokemonType,default="ST")
 hp=models.PositiveIntegerField()
 active =models.BooleanField(default=True)
 name_fr= models/CharField(max_length=30, default="") 
 name_ar=models.CharField(max_length=30, default="")
 name_jp=models.CharField(max_length=30, default="")
 created_at=models.DateTimeField(auto_now_add=True)
 modified_at=models.DateTimeField(auto_now=True)
# Create your models here.
