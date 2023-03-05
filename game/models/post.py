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

    def cod_roll(self, number_of_dice, again_minimum=10):
        roll, success_count = cod_dice(number_of_dice, again_minimum=again_minimum)
        roll = ", ".join(map(str, roll))
        self.message = f"{roll}: <b>{success_count}</b>"
        self.save()

    def wod_roll(self, number_of_dice, difficulty=6, specialty=False):
        roll, success_count = wod_dice(
            number_of_dice, difficulty=difficulty, specialty=specialty
        )
        roll = ", ".join(map(str, roll))
        self.message = f"{roll}: <b>{success_count}</b>"
        self.save()
