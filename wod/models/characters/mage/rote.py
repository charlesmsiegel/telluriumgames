from django.db import models


# Create your models here.
class Rote(models.Model):
    name = models.CharField(max_length=100, unique=True)
    correspondence = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    spirit = models.IntegerField(default=0)
    matter = models.IntegerField(default=0)
    life = models.IntegerField(default=0)
    forces = models.IntegerField(default=0)
    entropy = models.IntegerField(default=0)
    mind = models.IntegerField(default=0)
    prime = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def cost(self):
        return (
            self.correspondence
            + self.time
            + self.spirit
            + self.forces
            + self.matter
            + self.life
            + self.prime
            + self.entropy
            + self.mind
        )

    def is_learnable(self, mage):
        for sphere in mage.get_spheres().keys():
            if getattr(self, sphere) > getattr(mage, sphere):
                return False
        return True
