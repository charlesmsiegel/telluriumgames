from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Chronicle(models.Model):
    name = models.CharField(max_length=100, default="")
    storytellers = models.ManyToManyField(User, blank=True)
    theme = models.CharField(max_length=200, default="")
    mood = models.CharField(max_length=200, default="")
    common_knowledge_elements = models.TextField(default="")
    system = models.CharField(
        default="",
        max_length=100,
        choices=[
            ("cod", "Chronicles of Darkness"),
            ("ex", "Exalted"),
            ("trinity", "Trinity Continuum"),
            ("wod", "World of Darkness"),
        ],
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game:chronicle", kwargs={"pk": self.pk})

    def storyteller_list(self):
        return ", ".join([x.username for x in self.storytellers.all()])
