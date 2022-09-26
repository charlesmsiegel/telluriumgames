from django.db import models


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

    def __str__(self):
        return self.name
