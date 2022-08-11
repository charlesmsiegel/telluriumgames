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

    def has_name(self):
        return self.name != ""

    def set_name(self, name):
        self.name = name
        return True

    def random_name(self, name=None):
        if self.has_name():
            return False
        if name is None:
            name = f"Random Item {Item.objects.count()}"
        return self.set_name(name)
