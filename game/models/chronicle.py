from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .story import Story


# Create your models here.
class Chronicle(models.Model):
    name = models.CharField(max_length=100, default="")
    storytellers = models.ManyToManyField(User, blank=True)
    theme = models.CharField(max_length=200, default="")
    mood = models.CharField(max_length=200, default="")
    common_knowledge_elements = models.TextField(default="")
    headings = models.CharField(
        default="",
        max_length=100,
        choices=[
            ("vtm_heading", "Vampire: the Masquerade"),
            ("wta_heading", "Werewolf: the Apocalypse"),
            ("mtas_heading", "Mage: the Ascension"),
            ("ctd_heading", "Changeling: the Dreaming"),
            ("wto_heading", "Wraith: the Oblivion"),
            ("wod_heading", "World of Darkness"),
            ("cod_heading", "Chronicles of Darkness"),
            ("tc_aberrant_heading", "Trinity Continuum: Aberrant"),
            ("tc_core_heading", "Trinity Continuum"),
            ("exalted_heading", "Exalted"),
        ],
    )

    class Meta:
        verbose_name = "Chronicle"
        verbose_name_plural = "Chronicles"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game:chronicle", kwargs={"pk": self.pk})

    def storyteller_list(self):
        return ", ".join([x.username for x in self.storytellers.all()])

    def total_stories(self):
        return Story.objects.filter(chronicle=self).count()

    def add_story(self, name):
        return Story.objects.create(name=name, chronicle=self)
