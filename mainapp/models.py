from django.db import models

# Create your models here.

class Appsmodel(models.Model):
    title = models.CharField(max_length = 60)
    body = models.TextField()
    