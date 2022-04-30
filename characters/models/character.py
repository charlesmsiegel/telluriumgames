import random

from django.db import models
from django.shortcuts import reverse
from django.utils.timezone import now
from polymorphic.models import PolymorphicModel


# Create your models here.
class Character(PolymorphicModel):
    """Base Character class"""

    player = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="characters"
    )
    name = models.CharField(max_length=100, unique=True)
    concept = models.CharField(max_length=300)
    status_keys = ["Un", "Sub", "App", "Ret", "Dec"]
    statuses = ["Unfinished", "Submitted", "Approved", "Retired", "Deceased"]
    status = models.CharField(
        max_length=3, choices=zip(status_keys, statuses), default="Un"
    )
    minor = models.BooleanField(default=False)
    type = "character"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("character", args=[str(self.id)])

    def has_name(self):
        if self.name != "":
            return True
        return False

    def has_concept(self):
        if self.concept != "":
            return True
        return False
