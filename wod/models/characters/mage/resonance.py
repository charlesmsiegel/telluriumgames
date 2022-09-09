from django.db import models
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse("wod:characters:mage:resonance", args=[str(self.id)])

    def get_update_url(self):
        return reverse("wod:characters:mage:update_resonance", kwargs={"pk": self.pk})

    def get_heading(self):
        return "mtas_heading"

    def __str__(self):
        return self.name.title()

    def associated_spheres(self):
        all_spheres = {
            "correspondence": self.correspondence,
            "time": self.time,
            "spirit": self.spirit,
            "matter": self.matter,
            "life": self.life,
            "forces": self.forces,
            "entropy": self.entropy,
            "mind": self.mind,
            "prime": self.prime,
        }
        assoc_spheres = [k.title() for k, v in all_spheres.items() if v]
        return ", ".join(assoc_spheres)


class ResRating(models.Model):
    mage = models.ForeignKey("Mage", on_delete=models.CASCADE)
    resonance = models.ForeignKey(Resonance, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
