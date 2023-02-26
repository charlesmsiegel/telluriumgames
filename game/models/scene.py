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
        if display == "":
            display = character.name
        post = Post.objects.create(
            character=character, message=message, display_name=display, scene=self
        )
        if message.startswith("/roll"):
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
            post.roll(num_dice, difficulty=difficulty, specialty=specialty)
        return post
