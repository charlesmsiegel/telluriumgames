from django.db import models

from core.utils import add_dot
from tc.models.character.human import Human


# Create your models here.
class Talent(Human):
    type = "talent"
    inspiration = models.IntegerField(default=1)

    intuitive = models.IntegerField(default=0)
    reflective = models.IntegerField(default=0)
    destructive = models.IntegerField(default=0)

    def has_moment_of_inspiration(self):
        return self.add_moment_of_inspiration != ""

    def add_moment_of_inspiration(self, inspiration):
        self.has_moment_of_inspiration = inspiration
        return True

    def add_facet(self, facet):
        facet = facet.lower()
        if add_dot(self, facet, 5):
            if getattr(self, facet) == 3:
                add_dot(self, "inspiration", 10)
            if getattr(self, facet) == 5:
                add_dot(self, "inspiration", 10)
            return True
        return False

    def has_facets(self):
        return self.total_facets() == 3

    def total_facets(self):
        return self.intuitive + self.reflective + self.destructive

    def random_facets(self):
        pass

    def add_gift(self, gift):
        pass

    def total_gifts(self, path=None):
        pass

    def has_gifts(self):
        pass

    def random_gifts(self):
        pass

    def filter_gifts(self, keyword=None, path=None):
        return []

    def has_template(self):
        pass

    def apply_random_template(self):
        pass


class Gift(models.Model):
    name = models.CharField(max_length=100)
    keywords = models.JSONField(default=list)
    prereqs = models.JSONField(default=list)
