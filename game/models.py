from django.contrib.auth.models import User
from django.db import models
from pyexpat import model


# Create your models here.
class Chronicle(models.Model):
    name = models.CharField(max_length=100, default="")
    head_storyteller = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.name
