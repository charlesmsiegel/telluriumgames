from django.db import models
from polymorphic.models import PolymorphicModel


# Create your models here.
class Item(PolymorphicModel):
    type = "item"

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
