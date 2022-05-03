from turtle import title
from django.db import models

# Create your models here.

class Tudumodels(models.Model):
    title = models.CharField(max_length=155)
    body = models.TextField()
    
    def __str__(self): 
        return self.title
    
