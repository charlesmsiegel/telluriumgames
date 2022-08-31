from django.urls import reverse
from django.db import models

from wod.models.locations.human import Location


# Create your models here.
class Sector(Location):
    type = "sector"

    SECTOR_CLASS = [
        ("virgin", "Virgin Web"),
        ("grid", "Grid"),
        ("formatted", "Formatted Web"),
        ("corrupted", "Corrupted Web"),
        ("junklands", "Junklands"),
        ("haunts", "Haunts"),
        ("trash", "Trash"),
        ("streamland", "Streamland"),
    ]

    sector_class = models.CharField(max_length=10, choices=SECTOR_CLASS, default="")
    constraints = models.TextField(default="")

    def get_update_url(self):
        return reverse("wod:locations:mage:update_sector", args=[str(self.id)])
