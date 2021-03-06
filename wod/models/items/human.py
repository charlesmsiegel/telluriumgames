from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel


# Create your models here.
class Item(PolymorphicModel):
    type = "item"

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(default="")
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wod:items:item", args=[str(self.id)])
