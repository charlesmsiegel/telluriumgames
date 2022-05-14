import random
from django.db import models
from polymorphic.models import PolymorphicModel

from accounts.models import CoDProfile
from core.utils import add_dot


# Create your models here.
class Mortal(PolymorphicModel):
    type = "mortal"
    name = models.CharField(max_length=100)
    player = models.ForeignKey(
        CoDProfile, on_delete=models.CASCADE, related_name="characters"
    )

    concept = models.CharField(max_length=300)

    virtue = models.CharField(max_length=100)
    vice = models.CharField(max_length=100)

    intelligence = models.IntegerField(default=1)
    wits = models.IntegerField(default=1)
    resolve = models.IntegerField(default=1)

    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)

    presence = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    composure = models.IntegerField(default=1)

    academics = models.IntegerField(default=0)
    computer = models.IntegerField(default=0)
    crafts = models.IntegerField(default=0)
    investigation = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    politics = models.IntegerField(default=0)
    science = models.IntegerField(default=0)

    athletics = models.IntegerField(default=0)
    brawl = models.IntegerField(default=0)
    drive = models.IntegerField(default=0)
    firearms = models.IntegerField(default=0)
    larceny = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    weaponry = models.IntegerField(default=0)

    animal_ken = models.IntegerField(default=0)
    empathy = models.IntegerField(default=0)
    expression = models.IntegerField(default=0)
    intimidation = models.IntegerField(default=0)
    persuasion = models.IntegerField(default=0)
    socialize = models.IntegerField(default=0)
    streetwise = models.IntegerField(default=0)
    subterfuge = models.IntegerField(default=0)

    merits = models.ManyToManyField("Merit", through="MeritRating")

    specialties = models.ManyToManyField("Specialty", blank=True)

    def add_name(self, name):
        self.name = name
        return True

    def has_name(self):
        pass

    def add_concept(self, concept):
        self.concept = concept
        return True

    def has_concept(self):
        return self.concept != ""

    def has_virtue(self):
        return self.virtue != ""

    def filter_virtues(self, virtue_list=None):
        virtues = [x for x in self.virtue.split(", ") if x]
        return [x for x in virtue_list if x not in virtues]

    def random_virtue(self):
        virtues = ["Competitive", "Generous", "Just", "Loyal"]
        virtues = self.filter_virtues(virtues)
        self.add_virtue(random.choice(virtues))

    def add_virtue(self, virtue):
        if virtue not in self.virtue.split(", "):
            virtues = self.virtue.split(", ")
            virtues.append(virtue)
            virtues = [x for x in virtues if x]
            self.virtue = ", ".join(virtues)
            return True
        return False

    def has_vice(self):
        return self.vice != ""

    def filter_vices(self, vice_list=None):
        vices = [x for x in self.vice.split(", ") if x]
        return [x for x in vice_list if x not in vices]

    def random_vice(self):
        vices = ["Competitive", "Generous", "Just", "Loyal"]
        vices = self.filter_vices(vices)
        self.add_vice(random.choice(vices))

    def add_vice(self, vice):
        if vice not in self.vice.split(", "):
            vices = self.vice.split(", ")
            vices.append(vice)
            vices = [x for x in vices if x]
            self.vice = ", ".join(vices)
            return True
        return False

    def add_attribute(self, attribute, max=5):
        return add_dot(self, attribute, max)

    def get_mental_attributes(self):
        return {
            "intelligence": self.intelligence,
            "wits": self.wits,
            "resolve": self.resolve,
        }

    def get_physical_attributes(self):
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "stamina": self.stamina,
        }

    def get_social_attributes(self):
        return {
            "presence": self.presence,
            "manipulation": self.manipulation,
            "composure": self.composure,
        }

    def total_physical_attributes(self):
        return sum(self.get_physical_attributes().values())

    def total_social_attributes(self):
        return sum(self.get_social_attributes().values())

    def total_mental_attributes(self):
        return sum(self.get_mental_attributes().values())

    def total_attributes(self):
        return (
            self.total_physical_attributes()
            + self.total_social_attributes()
            + self.total_mental_attributes()
        )

    def has_attributes(self):
        pass

    def get_attributes(self):
        tmp = {}
        tmp.update(self.get_physical_attributes())
        tmp.update(self.get_mental_attributes())
        tmp.update(self.get_social_attributes())
        return tmp

    def filter_attributes(self, min=0, max=5):
        return {k: v for k, v in self.get_attributes().items() if min <= v <= max}

    def random_attribute(self):
        pass

    def random_attributes(self):
        pass

    def get_mental_skills(self):
        return {
            "academics": self.academics,
            "computer": self.computer,
            "crafts": self.crafts,
            "investigation": self.investigation,
            "medicine": self.medicine,
            "occult": self.occult,
            "politics": self.politics,
            "science": self.science,
        }

    def get_physical_skills(self):
        return {
            "athletics": self.athletics,
            "brawl": self.brawl,
            "drive": self.drive,
            "firearms": self.firearms,
            "larceny": self.larceny,
            "stealth": self.stealth,
            "survival": self.survival,
            "weaponry": self.weaponry,
        }

    def get_social_skills(self):
        return {
            "animal_ken": self.animal_ken,
            "empathy": self.empathy,
            "expression": self.expression,
            "intimidation": self.intimidation,
            "persuasion": self.persuasion,
            "socialize": self.socialize,
            "streetwise": self.streetwise,
            "subterfuge": self.subterfuge,
        }

    def total_physical_skills(self):
        return sum(self.get_physical_skills().values())

    def total_mental_skills(self):
        return sum(self.get_mental_skills().values())

    def total_social_skills(self):
        return sum(self.get_social_skills().values())

    def has_skills(self):
        pass

    def total_skills(self):
        return (
            self.total_physical_skills()
            + self.total_mental_skills()
            + self.total_social_skills()
        )

    def filter_skills(self, min=0, max=5):
        return {k: v for k, v in self.get_skills().items() if min <= v <= max}

    def get_skills(self):
        tmp = {}
        tmp.update(self.get_physical_skills())
        tmp.update(self.get_mental_skills())
        tmp.update(self.get_social_skills())
        return tmp

    def random_skill(self):
        pass

    def random_skills(self):
        pass

    def has_specialties(self):
        pass

    def filter_specialties(self, skill=None):
        if skill is None:
            return [
                x for x in Specialty.objects.all() if x not in self.specialties.all()
            ]
        else:
            return [
                x
                for x in Specialty.objects.filter(skill=skill)
                if x not in self.specialties.all()
            ]

    def add_specialty(self, specialty):
        if specialty not in self.specialties.all():
            self.specialties.add(specialty)
            return True
        return False

    def random_specialties(self):
        pass

    def random_specialty(self):
        pass

    def add_merit(self, merit):
        if merit in self.merits.all():
            merit_rating = MeritRating.objects.get(character=self, merit=merit)
            current_rating = merit_rating.rating
            values = [x for x in merit.ratings if x > current_rating]
            if len(values) != 0:
                merit_rating.rating = min(values)
                merit_rating.save()
                return True
            else:
                return False
        else:
            rating = merit.ratings[0]
            MeritRating.objects.create(character=self, merit=merit, rating=rating)
            return True

    def merit_rating(self, name):
        merit = Merit.objects.get(name=name)
        if merit not in self.merits.all():
            return 0
        else:
            return MeritRating.objects.get(character=self, merit=merit).rating

    def total_merits(self):
        return 0

    def has_merits(self):
        pass

    def filter_merits(self, dots=None):
        all_merits = Merit.objects.all()
        pairs = [(m, r) for m in all_merits for r in m.ratings]
        pairs = [p for p in pairs if p[1] <= dots]
        output = []
        for merit, rating in pairs:
            if merit in self.merits.all():
                r = MeritRating.objects.get(character=self, merit=merit).rating
                if rating > r:
                    output.append(merit)
            else:
                output.append(merit)
        output = list(set(output))
        return output

    def random_merit(self):
        pass

    def random_merits(self):
        pass


class Merit(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.JSONField(default=list)


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)


class MeritRating(models.Model):
    character = models.ForeignKey(
        "Mortal", null=False, blank=False, on_delete=models.CASCADE
    )
    merit = models.ForeignKey(
        "Merit", null=False, blank=False, on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=0)
