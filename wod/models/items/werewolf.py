from django.db import models
from django.urls import reverse

from wod.models.items.human import Item


# Create your models here.
class Fetish(Item):
    type = "fetish"

    rank = models.IntegerField(default=0)
    gnosis = models.IntegerField(default=0)
    spirit = models.CharField(default="", max_length=100)

    def get_absolute_url(self):
        return reverse("wod:item", kwargs={"pk": self.pk})
