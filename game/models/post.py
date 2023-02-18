from django.db import models

from core.utils import cod_dice, wod_dice


# Create your models here.
class Post(models.Model):
    character = models.ForeignKey(
        "core.CharacterModel", on_delete=models.SET_NULL, null=True
    )
    display_name = models.CharField(max_length=100)
    scene = models.ForeignKey("game.Scene", on_delete=models.SET_NULL, null=True)
    message = models.TextField(default="")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        if self.display_name:
            return self.display_name + ": " + self.message
        return self.character.name + ": " + self.message

    def roll(self, number_of_dice, difficulty=6, specialty=False, again_minimum=10):
        if self.scene.story.chronicle.system == "cod":
            roll, success_count = cod_dice(number_of_dice, again_minimum=again_minimum)
        elif self.scene.story.chronicle.system == "wod":
            roll, success_count = wod_dice(
                number_of_dice, difficulty=difficulty, specialty=specialty
            )
        else:
            raise ValueError(
                f"Not Implemented System {self.scene.story.chronicle.system}"
            )
        roll = ", ".join(map(str, roll))
        self.message = f"{roll}: <b>{success_count}</b>"
        self.save()
