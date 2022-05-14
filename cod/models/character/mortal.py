import random
from django.db import models
from polymorphic.models import PolymorphicModel

from accounts.models import CoDProfile


# Create your models here.
class Mortal(PolymorphicModel):
    type = "mortal"
    name = models.CharField(max_length=100)
    player = models.ForeignKey(
        CoDProfile, on_delete=models.CASCADE, related_name="characters"
    )
    virtue = models.CharField(max_length=100)
    vice = models.CharField(max_length=100)

    def has_virtue(self):
        return self.virtue != ""

    def random_virtue(self):
        virtues = ["Competitive", "Generous", "Just", "Loyal"]
        self.add_virtue(random.choice(virtues))
        
    def add_virtue(self, virtue):
        if virtue not in self.virtue.split(", "):
            virtues = self.virtue.split(", ")
            virtues.append(virtue)
            virtues = [x for x in virtues if x]
            self.virtue = ", ".join(virtues)
            return True
        return False
    
    def has_vice(self):
        return self.vice != ""

    def random_vice(self):
        vices = ["Competitive", "Generous", "Just", "Loyal"]
        self.add_vice(random.choice(vices))
        
    def add_vice(self, vice):
        if vice not in self.vice.split(", "):
            vices = self.vice.split(", ")
            vices.append(vice)
            vices = [x for x in vices if x]
            self.vice = ", ".join(vices)
            return True
        return False


class Merit(models.Model):
    pass


class Specialty(models.Model):
    pass
