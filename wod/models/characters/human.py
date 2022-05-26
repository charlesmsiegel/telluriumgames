from django.db import models
from polymorphic.models import PolymorphicModel

from accounts.models import WoDProfile
from core.utils import add_dot, weighted_choice


# Create your models here.
class Archetype(models.Model):
    name = models.CharField(max_length=100, unique=True)

class MeritFlaw(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ratings = models.JSONField(default=list)

class MeritFlawRating(models.Model):
    character = models.ForeignKey("Human", on_delete=models.CASCADE)
    mf = models.ForeignKey(MeritFlaw, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

class Character(PolymorphicModel):
    type = "character"

    name = models.CharField(max_length=100, unique=True)
    player = models.ForeignKey(
        WoDProfile, on_delete=models.CASCADE, related_name="characters"
    )
    concept = models.CharField(max_length=100)
    
    def has_concept(self):
        return self.concept != ""

    def set_concept(self, concept):
        self.concept = concept
        return True

    def has_name(self):
        return self.name != ""

    def set_name(self, name):
        self.name = name
        return True


class Human(Character):
    type = "human"

    nature = models.ForeignKey(Archetype, on_delete=models.CASCADE, blank=True, null=True, related_name="nature_of")
    demeanor = models.ForeignKey(Archetype, on_delete=models.CASCADE, blank=True, null=True, related_name="demeanor_of")

    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
    perception = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    wits = models.IntegerField(default=1)
    charisma = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    appearance = models.IntegerField(default=1)

    willpower = models.IntegerField(default=3)

    merits_and_flaws = models.ManyToManyField(MeritFlaw, blank=True, through=MeritFlawRating)

    def has_archetypes(self):
        return self.nature is not None and self.demeanor is not None

    def set_archetypes(self, nature, demeanor):
        self.nature = nature
        self.demeanor = demeanor
        return True

    def add_attribute(self, attribute, maximum=5):
        return add_dot(self, attribute, maximum)

    def get_attributes(self):
        tmp = {}
        tmp.update(self.get_physical_attributes())
        tmp.update(self.get_mental_attributes())
        tmp.update(self.get_social_attributes())
        return tmp

    def get_physical_attributes(self):
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "stamina": self.stamina
        }

    def get_social_attributes(self):
        return {
            "charisma": self.charisma,
            "manipulation": self.manipulation,
            "appearance": self.appearance
        }

    def get_mental_attributes(self):
        return {
            "perception": self.perception,
            "intelligence": self.intelligence,
            "wits": self.wits
        }

    def total_physical_attributes(self):
        return sum(self.get_physical_attributes().values())

    def total_social_attributes(self):
        return sum(self.get_social_attributes().values())

    def total_mental_attributes(self):
        return sum(self.get_mental_attributes().values())

    def filter_attributes(self, minimum=0, maximum=5):
        return {k: v for k, v in self.get_attributes().items() if minimum <= v <= maximum}

    def total_talents(self):
        return 0

    def total_skills(self):
        return 0

    def total_knowledges(self):
        return 0

    def add_willpower(self):
        return add_dot(self, "willpower", 10)

    def add_mf(self, mf, rating):
        if rating in mf.ratings:
            mfr, _ = MeritFlawRating.objects.get_or_create(character=self, mf=mf)
            mfr.rating = rating
            mfr.save()
            return True
        return False

    def filter_mfs(self):
        full_set = MeritFlaw.objects.all()
        filtered_set = []
        for mf in full_set:
            for r in mf.ratings:
                if mf not in self.merits_and_flaws.all():
                    filtered_set.append((mf, r))
                elif r > self.mf_rating(mf) > 0:
                    filtered_set.append((mf, r))
                elif r < self.mf_rating(mf) < 0:
                    filtered_set.append((mf, r))
        filtered_set = [x[0] for x in filtered_set]
        if self.has_max_flaws():
            filtered_set = [x for x in filtered_set if max(x.ratings) > 0]
        return filtered_set

    def mf_rating(self, mf):
        if mf not in self.merits_and_flaws.all():
            return 0
        return MeritFlawRating.objects.get(character=self, mf=mf).rating

    def has_max_flaws(self):
        return self.total_flaws() <= -7

    def total_flaws(self):
        return sum([x.rating for x in MeritFlawRating.objects.filter(character=self) if x.rating < 0])

    def total_merits(self):
        return sum([x.rating for x in MeritFlawRating.objects.filter(character=self) if x.rating > 0])
