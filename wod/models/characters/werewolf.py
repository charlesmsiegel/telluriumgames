import random

from django.contrib.auth.models import User
from django.db import models

from accounts.models import WoDProfile
from core.utils import add_dot
from wod.models.characters.human import Human


class Totem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Tribe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    willpower = models.IntegerField(default=3)

    def __str__(self):
        return self.name


class Camp(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tribe = models.ForeignKey(Tribe, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Gift(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rank = models.IntegerField(default=0)
    allowed = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class Rite(models.Model):
    name = models.CharField(max_length=100, unique=True)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Werewolf(Human):
    type = "garou"

    rank = models.IntegerField(default=1)
    auspice = models.CharField(
        default="",
        max_length=100,
        choices=[
            ("ragabash", "Ragabash"),
            ("theurge", "Theurge"),
            ("philodox", "Philodox"),
            ("galliard", "Galliard"),
            ("ahroun", "Ahroun"),
        ],
    )
    breed = models.CharField(
        default="",
        max_length=100,
        choices=[("homid", "Homid"), ("metis", "Metis"), ("lupus", "Lupus"),],
    )
    tribe = models.ForeignKey(Tribe, blank=True, null=True, on_delete=models.CASCADE)
    camp = models.ForeignKey(Camp, blank=True, null=True, on_delete=models.CASCADE)

    leadership = models.IntegerField(default=0)
    primal_urge = models.IntegerField(default=0)

    animal_ken = models.IntegerField(default=0)
    larceny = models.IntegerField(default=0)
    performance = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)

    enigmas = models.IntegerField(default=0)
    law = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    rituals = models.IntegerField(default=0)
    technology = models.IntegerField(default=0)

    rites = models.IntegerField(default=0)
    allies = models.IntegerField(default=0)
    ancestors = models.IntegerField(default=0)
    fate = models.IntegerField(default=0)
    fetish = models.IntegerField(default=0)
    kinfolk = models.IntegerField(default=0)
    pure_breed = models.IntegerField(default=0)
    resources = models.IntegerField(default=0)
    spirit_heritage = models.IntegerField(default=0)
    totem = models.IntegerField(default=0)

    gnosis = models.IntegerField(default=0)
    rage = models.IntegerField(default=0)

    glory = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    honor = models.IntegerField(default=0)

    gifts = models.ManyToManyField(Gift, blank=True)
    rites_known = models.ManyToManyField(Rite, blank=True)

    first_change = models.TextField(default="")
    battle_scars = models.TextField(default="")
    age_of_first_change = models.IntegerField(default=0)

    def get_backgrounds(self):
        tmp = super().get_backgrounds()
        tmp.update(
            {
                "allies": self.allies,
                "ancestors": self.ancestors,
                "fate": self.fate,
                "fetish": self.fetish,
                "kinfolk": self.kinfolk,
                "pure_breed": self.pure_breed,
                "resources": self.resources,
                "rites": self.rites,
                "spirit_heritage": self.spirit_heritage,
                "totem": self.totem,
            }
        )
        return tmp

    def get_talents(self):
        tmp = super().get_talents()
        tmp.update(
            {"leadership": self.leadership, "primal_urge": self.primal_urge,}
        )
        return tmp

    def get_skills(self):
        tmp = super().get_skills()
        tmp.update(
            {
                "animal_ken": self.animal_ken,
                "larceny": self.larceny,
                "performance": self.performance,
                "survival": self.survival,
            }
        )
        return tmp

    def get_knowledges(self):
        tmp = super().get_knowledges()
        tmp.update(
            {
                "enigmas": self.enigmas,
                "law": self.law,
                "occult": self.occult,
                "rituals": self.rituals,
                "technology": self.technology,
            }
        )
        return tmp

    def has_breed(self):
        return self.breed is not None

    def set_breed(self, breed):
        self.breed = breed
        return True

    def random_breed(self):
        return self.set_breed(random.choice(["homid", "metis", "lupus"]))

    def has_auspice(self):
        return self.auspice is not None

    def set_auspice(self, auspice):
        self.auspice = auspice
        return True

    def random_auspice(self):
        return self.set_auspice(
            random.choice(["ragabash", "theurge", "philodox", "galliard", "ahroun"])
        )

    def has_tribe(self):
        return self.tribe is not None

    def set_tribe(self, tribe):
        self.tribe = tribe
        self.willpower = tribe.willpower
        return True

    def random_tribe(self):
        return self.set_tribe(Tribe.objects.order_by("?").first())

    def has_camp(self):
        return self.camp is not None

    def set_camp(self, camp):
        self.camp = camp
        return True

    def random_camp(self):
        return self.set_tribe(
            Camp.objects.filter(tribe=self.tribe).order_by("?").first()
        )

    def add_gift(self, gift):
        self.gifts.add(gift)
        self.save()
        return True

    def filter_gifts(self):
        return []

    def has_gifts(self):
        pass

    def random_gift(self):
        pass

    def random_gifts(self):
        pass

    def add_rite(self, rite):
        self.rites_known.add(rite)
        self.save()
        return True

    def filter_rites(self):
        return []

    def has_rites(self):
        return self.rites == self.total_rites()

    def total_rites(self):
        return (
            sum([x.level for x in self.rites_known.all()])
            + self.rites_known.filter(level=0).count() // 2
        )

    def random_rites(self):
        pass

    def set_glory(self, glory):
        self.glory = glory
        return True

    def set_honor(self, honor):
        self.honor = honor
        return True

    def set_wisdom(self, wisdom):
        self.wisdom = wisdom
        return True

    def has_renown(self):
        pass

    def add_gnosis(self):
        return add_dot(self, "gnosis", 10)

    def add_rage(self):
        return add_dot(self, "rage", 10)

    def set_rank(self, rank):
        self.rank = rank
        return True

    def increase_rank(self):
        pass

    def xp_cost(self, trait):
        if trait == "gift":
            return 3
        if trait == "outside gift":
            return 5
        if trait == "rage":
            return 1
        if trait == "gnosis":
            return 2
        return super().xp_cost(trait)

    def freebie_cost(self, trait):
        if trait == "gift":
            return 7
        if trait == "rage":
            return 1
        if trait == "gnosis":
            return 2
        return super().freebie_cost(trait)

    def has_werewolf_history(self):
        return (
            (self.first_change != "")
            and (self.battle_scars != "")
            and (self.age_of_first_change != 0)
        )


class Pack(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(Werewolf, blank=True)
    leader = models.ForeignKey(
        Werewolf, blank=True, null=True, on_delete=models.CASCADE, related_name="leads"
    )
    totem = models.ForeignKey(Totem, null=True, blank=True, on_delete=models.CASCADE)

    def random(self, num_chars, new_characters=False):
        if not new_characters and Werewolf.objects.count() < num_chars:
            raise ValueError("Not enough Werewolves!")
        if not new_characters:
            self.members.set(Werewolf.objects.order_by("?")[:num_chars])
        else:
            if WoDProfile.objects.filter(storyteller=True).count() > 0:
                user = (
                    WoDProfile.objects.filter(storyteller=True)
                    .order_by("?")
                    .first()
                    .user
                )
            else:
                user = User.objects.create_user(username="New User")
                user.wod_profile.storyteller = True
                user.save()
            for _ in range(num_chars):
                w = Werewolf.objects.create(
                    name=f"{self.name} {self.members.count() + 1}",
                    player=user.wod_profile,
                )
                w.random()
                self.members.add(w)
        self.leader = self.members.order_by("?").first()
        self.random_totem()
        self.save()

    def set_totem(self, totem):
        self.totem = totem
        return True

    def has_totem(self):
        return self.totem is not None

    def random_totem(self):
        pass

    def total_totem(self):
        return sum([x.totem for x in self.members.all()])

    def __str__(self):
        return self.name
