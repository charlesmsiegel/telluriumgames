from django.db import models

from wod.models.locations.human import Location
# Create your models here.
class Caern(Location):
    type = "caern"
    
    rank = models.IntegerField(default=0)
    
    TYPES = [
        ("enigmas", "Enigmas"),
        ("gnosis", "Gnosis"),
        ("healing", "Healing"),
        ("leadership", "Leadership"),
        ("rage", "Rage"),
        ("stamina", "Stamina"),
        ("strength", "Strength"),
        ("urban", "Urban"),
        ("visions", "Visions"),
        ("will", "Will"),
        ("wisdom", "Wisdom"),
        ("wyld", "Wyld"),
    ]
    
    caern_type = models.CharField(default="", choices=TYPES, max_length=15)
    
    def save(self, *args, **kwargs):
        if "gauntlet" not in kwargs:
            if self.rank < 3:
                self.gauntlet = 4
            elif self.rank < 5:
                self.gauntlet = 3
            else:
                self.gauntlet = 2
        return super().save(*args, **kwargs)
    