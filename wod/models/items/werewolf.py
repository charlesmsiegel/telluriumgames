from django.db import models
from django.urls import reverse

from wod.models.items.mage import Wonder


# Create your models here.
class Fetish(Wonder):
    type = "fetish"

    gnosis = models.IntegerField(default=0)
    spirit = models.CharField(default="", max_length=100)

    # def __init__(self, *args, **kwargs):
    #     kwargs["background_cost"] = kwargs.get("rank")
    #     super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.background_cost = self.rank
        return super().save(*args, **kwargs)
