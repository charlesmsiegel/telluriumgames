from django.db import models
from core.models import Model


# Create your models here.
class Resonance(Model):
    type = "resonance"
    
    correspondence = models.BooleanField(default=False)
    time = models.BooleanField(default=False)
    spirit = models.BooleanField(default=False)
    matter = models.BooleanField(default=False)
    life = models.BooleanField(default=False)
    forces = models.BooleanField(default=False)
    entropy = models.BooleanField(default=False)
    mind = models.BooleanField(default=False)
    prime = models.BooleanField(default=False)

    def __str__(self):
        return self.name.title()


class ResRating(models.Model):
    mage = models.ForeignKey("Mage", on_delete=models.CASCADE)
    resonance = models.ForeignKey(Resonance, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
