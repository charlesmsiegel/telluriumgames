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

    def get_update_url(self):
        return reverse("wod:items:werewolf:update_fetish", args=[str(self.id)])

    def get_heading(self):
        return "wta_heading"

    def save(self, *args, **kwargs):
        self.background_cost = self.rank
        return super().save(*args, **kwargs)
