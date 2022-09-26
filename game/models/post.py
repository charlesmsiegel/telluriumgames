from django.db import models

from .scene import Scene

# Create your models here.
class Post(models.Model):
    character = models.ForeignKey("core.CharacterModel", on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    message = models.TextField(default="")

    def __str__(self):
        if self.display_name:
            return self.display_name + ": " + self.message
        return self.character.name + ": " + self.message
