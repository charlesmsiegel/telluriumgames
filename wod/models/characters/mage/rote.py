from django.db import models
from django.urls import reverse


# Create your models here.
class Effect(models.Model):
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
    rote_cost = models.IntegerField(default=0)
    description = models.TextField(default="")

    def __str__(self):
        dots = {
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
        filtered_dots = [f"{k.title()}: {v}" for k, v in dots.items() if v != 0]
        final_dots = ", ".join(filtered_dots)
        return f"{self.name} ({final_dots})"

    def get_absolute_url(self):
        return reverse("wod:characters:mage:effect", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.rote_cost = self.cost()
        return super().save(*args, **kwargs)

    def spheres(self):
        dots = {
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
        filtered_dots = [f"{k.title()} {v * '●'}" for k, v in dots.items() if v != 0]
        final_dots = ", ".join(filtered_dots)
        return final_dots

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
