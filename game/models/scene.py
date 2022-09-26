from django.db import models

from .story import Story


# Create your models here.
class Scene(models.Model):
    name = models.CharField(max_length=100, default="")
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    date_played = models.DateField(null=True, blank=True)
    characters = models.ManyToManyField(
        "core.CharacterModel", related_name="scenes", blank=True
    )
    location = models.ForeignKey(
        "core.LocationModel", on_delete=models.CASCADE, null=True
    )
    finished = models.BooleanField(default=False)
    xp_given = models.BooleanField(default=False)
    # date_of_scene

    def __str__(self):
        if self.name not in ["", "''"]:
            return self.name
        return str(self.location) + " " + str(self.date)

    def close(self):
        """Closes the scene"""
        self.finished = True
        self.save()
