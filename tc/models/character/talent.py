from django.db import models

from tc.models.character.human import Human


# Create your models here.
class Talent(Human):
    type = "talent"

    def has_moment_of_inspiration(self):
        pass

    def add_moment_of_inspiration(self, inspiration):
        pass
