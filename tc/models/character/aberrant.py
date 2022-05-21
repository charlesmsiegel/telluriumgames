from django.db import models

from tc.models.character.human import Edge, Human


# Create your models here.
class Aberrant(Human):
    type = "aberrant"

    mega_intellect = models.IntegerField(default=0)
    mega_cunning = models.IntegerField(default=0)
    mega_resolve = models.IntegerField(default=0)
    mega_might = models.IntegerField(default=0)
    mega_dexterity = models.IntegerField(default=0)
    mega_stamina = models.IntegerField(default=0)
    mega_presence = models.IntegerField(default=0)
    mega_manipulation = models.IntegerField(default=0)
    mega_composure = models.IntegerField(default=0)

    powers = models.ManyToManyField("Power", blank=True)

    transcendence = models.IntegerField(default=0)

    def add_mega_attribute(self, attribute):
        pass

    def filter_mega_attributes(self):
        pass

    def get_mega_attributes(self):
        return {
            "mega_intellect": self.mega_intellect,
            "mega_cunning": self.mega_cunning,
            "mega_resolve": self.mega_resolve,
            "mega_might": self.mega_might,
            "mega_dexterity": self.mega_dexterity,
            "mega_stamina": self.mega_stamina,
            "mega_presence": self.mega_presence,
            "mega_manipulation": self.mega_manipulation,
            "mega_composure": self.mega_composure,
        }

    def random_mega_attribute(self):
        pass

    def total_mega_attributes(self):
        return sum(self.get_mega_attributes().values())

    def total_mega_edges(self):
        return -100

    def filter_mega_edges(self):
        return []

    def random_mega_edge(self, dots=100):
        pass

    def random_mega_edges(self):
        pass

    def add_power(self, power):
        pass

    def total_powers(self):
        return -100

    def random_power(self):
        pass

    def get_tags(self, power):
        return []

    def add_tag(self, power, tag):
        pass

    def random_tag(self, power):
        pass

    def tag_rating(self, power, tag):
        pass

    def filter_tags(self, power):
        return []

    def add_transformation(self, transformation):
        pass

    def filter_transformations(self):
        return []

    def add_transcendence(self):
        pass

    def add_quantum(self):
        pass

    def update_quantum_points(self):
        pass

        # self.fail("Quantum of 1")
        # self.fail("One dot in favored approach")
        # self.fail("Either 1 dot of Fame or 1 dot of Alternate Identity Edge")
        # self.fail("150 XP")
        # self.fail("Check spend_xp?")

    def apply_random_template(self):
        pass

    # TODO: Random XP Spend extension


class MegaEdge(Edge):
    type = "megaedge"


class Power(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantum_minimum = models.IntegerField(default=0)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ratings = models.JSONField(default=list)
    permitted_powers = models.ManyToManyField(Power, blank=True)


class Transformation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    level = models.CharField(
        max_length=4, choices=[("low", "low"), ("med", "medium"), ("high", "high"),],
    )
