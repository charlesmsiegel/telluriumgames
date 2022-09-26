from django.db import models
from django.urls import reverse

from .chronicle import Chronicle


# Create your models here.
class Story(models.Model):
    name = models.CharField(max_length=100, default="")
    pcs = models.ManyToManyField(
        "core.CharacterModel", blank=True, related_name="pc_in"
    )
    key_npcs = models.ManyToManyField(
        "core.CharacterModel", blank=True, related_name="npc_in"
    )
    plot_summary = models.TextField(default="")
    key_locations = models.ManyToManyField("core.LocationModel", blank=True)
    chronicle = models.ForeignKey(
        Chronicle, null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game:story", kwargs={"pk": self.pk})
