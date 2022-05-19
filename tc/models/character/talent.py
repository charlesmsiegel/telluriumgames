from email.policy import default

from django.db import models

from tc.models.character.human import Human


# Create your models here.
class Talent(Human):
    type = "talent"
    inspiration = models.IntegerField(default=1)

    def has_moment_of_inspiration(self):
        pass

    def add_moment_of_inspiration(self, inspiration):
        pass

    def add_inspiration(self):
        pass

    def add_facet(self, facet):
        pass

    def has_facets(self):
        pass

    def add_gift(self, gift):
        pass

    def total_gifts(self, path=None):
        pass

    def has_gifts(self):
        pass


class Gift(models.Model):
    name = models.CharField(max_length=100)
    keywords = models.JSONField(default=list)
    prereqs = models.JSONField(default=list)
