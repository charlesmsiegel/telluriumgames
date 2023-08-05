from django.db import models
from django.urls import reverse

from .scene import Scene


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
        "game.Chronicle", null=True, blank=True, on_delete=models.SET_NULL
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"

    def save(self, *args, **kwargs):
        if Scene.objects.filter(story=self).exists():
            self.start_date = min(
                x.date_of_scene for x in Scene.objects.filter(story=self)
            )
            self.end_date = max(
                x.date_of_scene for x in Scene.objects.filter(story=self)
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game:story", kwargs={"pk": self.pk})

    def total_scenes(self):
        return Scene.objects.filter(story=self).count()

    def total_locations(self):
        return self.key_locations.count()

    def add_scene(self, name, location, date_played=None, date_of_scene=None):
        if isinstance(location, str):
            from core.models import LocationModel

            location = LocationModel.objects.get(name=location)
        if Scene.objects.filter(name=name, story=self, location=location).exists():
            return Scene.objects.filter(
                name=name, story=self, location=location
            ).first()
        s = Scene.objects.create(
            name=name,
            story=self,
            location=location,
            date_played=date_played,
            date_of_scene=date_of_scene,
        )
        self.key_locations.add(location)
        self.save()
        return s

    def total_pcs(self):
        return self.pcs.count()

    def total_npcs(self):
        return self.key_npcs.count()
