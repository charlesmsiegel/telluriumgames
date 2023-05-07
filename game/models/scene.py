from django.db import models
from django.urls import reverse

from .post import Post


# Create your models here.
class Scene(models.Model):
    name = models.CharField(max_length=100, default="")
    story = models.ForeignKey("game.Story", on_delete=models.SET_NULL, null=True)
    date_played = models.DateField(null=True, blank=True)
    characters = models.ManyToManyField(
        "core.CharacterModel", related_name="scenes", blank=True
    )
    location = models.ForeignKey(
        "core.LocationModel", on_delete=models.SET_NULL, null=True
    )
    finished = models.BooleanField(default=False)
    xp_given = models.BooleanField(default=False)
    date_of_scene = models.CharField(default="", max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = "Scene"
        verbose_name_plural = "Scenes"

    def __str__(self):
        if self.name not in ["", "''"]:
            return self.name
        return str(self.location) + " " + str(self.date)

    def get_absolute_url(self):
        return reverse("game:scene", kwargs={"pk": self.pk})

    def close(self):
        self.finished = True
        self.save()

    def total_characters(self):
        return self.characters.count()

    def add_character(self, character):
        if isinstance(character, str):
            from core.models import CharacterModel

            character = CharacterModel.objects.get(name=character)
        self.characters.add(character)
        if character.npc:
            self.story.key_npcs.add(character)
        else:
            self.story.pcs.add(character)
        return character

    def total_posts(self):
        return Post.objects.filter(scene=self).count()

    def add_post(self, character, display, message):
        if character not in self.characters.all():
            self.add_character(character)
        if display == "":
            display = character.name
        post = Post.objects.create(
            character=character, message=message, display_name=display, scene=self
        )
        if message.startswith("/roll"):
            if self.story.chronicle.system == "wod":
                # /roll <num_dice> difficulty <diff> <specialty>
                tmp = message.split("/roll")[1]
                parts = [x.strip() for x in tmp.split("difficulty")]
                num_dice = int(parts[0])
                if " " in parts[1]:
                    difficulty = int(parts[1].split(" ")[0])
                    specialty = True
                else:
                    difficulty = int(parts[1])
                    specialty = False
                post.wod_roll(num_dice, difficulty=difficulty, specialty=specialty)
            elif self.story.chronicle.system == "cod":
                # /roll <num_dice> <again_threshold>-again
                tmp = message.split("/roll")[1]
                if tmp.endswith("-again"):
                    num_dice = int(tmp.split(" ")[0])
                    again = int(tmp.split(" ")[1].split("-")[0])
                else:
                    num_dice = int(tmp)
                    again = 10
                post.cod_roll(num_dice, again_minimum=again)
            elif self.story.chronicle.system == "tc":
                pass
            elif self.story.chronicle.system == "ex":
                pass
        return post
