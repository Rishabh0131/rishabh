from django.db import models

# Create your models here.
class Questions(models.Model):
    name = models.CharField(default = " ", max_length = 200)