import random
from collections import defaultdict

from django.db import models

from core.utils import add_dot
from wod.models.characters.human import MeritFlaw, MeritFlawRating

from .garou import Fetish, Gift, Tribe
from .wtahuman import WtAHuman


class Kinfolk(WtAHuman):
    type = "kinfolk"

    breed = models.CharField(
        default="", max_length=100, choices=[("homid", "Homid"), ("lupus", "Lupus"),],
    )
    tribe = models.ForeignKey(Tribe, blank=True, null=True, on_delete=models.CASCADE)

    relation = models.CharField(max_length=100, default="")
    gifts = models.ManyToManyField(Gift, blank=True)

    gnosis = models.IntegerField(default=0)
    fetishes_owned = models.ManyToManyField(Fetish, blank=True)

    glory = models.IntegerField(default=0)
    temporary_glory = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    temporary_wisdom = models.IntegerField(default=0)
    honor = models.IntegerField(default=0)
    temporary_honor = models.IntegerField(default=0)

    # def __init__(self, *args, **kwargs):
    #     kwargs["willpower"] = kwargs.get("willpower") or 3
    #     super().__init__(*args, **kwargs)

    def has_breed(self):
        return self.breed != ""

    def set_breed(self, breed):
        self.breed = breed
        self.save()
        return True

    def random_breed(self):
        return self.set_breed(random.choice(["homid", "lupus"]))

    def has_tribe(self):
        return self.tribe is not None

    def set_tribe(self, tribe):
        if tribe.name == "Red Talons" and self.breed == "homid":
            return False
        self.tribe = tribe
        if self.tribe.name == "Silver Fangs" and self.pure_breed < 1:
            self.pure_breed = 1
        if self.tribe.name == "Black Spiral Dancers":
            self.random_derangement()
        self.save()
        return True

    def random_tribe(self):
        value = True
        while self.tribe is None:
            value = self.set_tribe(Tribe.objects.order_by("?").first())
        return value

    def get_backgrounds(self):
        return {
            "allies": self.allies,
            "contacts": self.contacts,
            "mentor": self.mentor,
            "pure_breed": self.pure_breed,
            "resources": self.resources,
        }

    def add_background(self, background, maximum=5):
        if self.tribe.name == "Bone Gnawers":
            if background == "pure_breed":
                return False
            if background == "resources" and self.resources == 3:
                return False
        if self.tribe.name == "Glass Walkers":
            if background in ["pure_breed", "mentor"]:
                return False
        if self.tribe.name == "Red Talons":
            if background == "resources":
                return False
        if self.tribe.name == "Shadow Lords":
            if background == "mentor":
                return False
        if self.tribe.name == "Silent Striders":
            if background == "resources" and self.resources == 3:
                return False
        if self.tribe.name == "Stargazers":
            if background == "resources" and self.resources == 3:
                return False
        if self.tribe.name == "Wendigo":
            if background == "resources" and self.resources == 3:
                return False
        return add_dot(self, background, maximum)

    def xp_cost(self, trait):
        cost = super().xp_cost(trait)
        if cost != 10000:
            return cost
        costs = defaultdict(lambda: 10000, {"gift": 15, "outside gift": 20})
        return costs[trait]

    def spend_xp(self, trait):
        output = super().spend_xp(trait)
        if output in [True, False]:
            return output
        if Gift.objects.filter(name=trait).exists():
            g = Gift.objects.get(name=trait)
            if (
                self.breed in g.allowed["garou"]
                or self.tribe.name in g.allowed["garou"]
            ):
                trait_type = "gift"
            else:
                trait_type = "outside gift"
            cost = self.xp_cost(trait_type) * g.rank
            if cost <= self.xp:
                if self.add_gift(g):
                    self.xp -= cost
                    return True
                return False
            return False
        return trait

    def xp_frequencies(self):
        return {
            "attribute": 15,
            "ability": 20,
            "background": 15,
            "willpower": 5,
            "gift": 35,
        }

    def random_xp_functions(self):
        return {
            "attribute": self.random_xp_attributes,
            "ability": self.random_xp_abilities,
            "background": self.random_xp_background,
            "willpower": self.random_xp_willpower,
            "gift": self.random_xp_gift,
        }

    def choose_random_gift(self, breed=False, tribe=False):
        while True:
            index = random.randint(1, Gift.objects.last().id)
            if Gift.objects.filter(pk=index).exists():
                choice = Gift.objects.get(pk=index)
                correct = True
                if breed and self.breed not in choice.allowed["garou"]:
                    correct = False
                if tribe:
                    if self.camp is not None:
                        if (
                            self.tribe.name not in choice.allowed["garou"]
                            and self.camp.name not in choice.allowed["garou"]
                        ):
                            correct = False
                    elif self.tribe.name not in choice.allowed["garou"]:
                        correct = False
                if choice.rank != 1:
                    correct = False
                if correct:
                    return choice

    def random_xp_gift(self):
        trait = self.choose_random_gift()
        return self.spend_xp(trait)

    def add_gift(self, gift):
        self.gifts.add(gift)
        self.save()
        return True

    def set_relation(self, relation):
        self.relation = relation
        return True

    def has_relation(self):
        return self.relation != ""

    def random_relation(self):
        relation = random.choice(["Related"])
        return self.set_relation(relation)

    def mf_based_corrections(self):
        if self.merits_and_flaws.filter(name="Gnosis").exists():
            gnosis = MeritFlaw.objects.get(name="Gnosis")
            rating = MeritFlawRating.objects.get(mf=gnosis, character=self).rating
            self.gnosis = rating - 4
        if self.merits_and_flaws.filter(name="Fetish").exists():
            fetish = MeritFlaw.objects.get(name="Fetish")
            rating = MeritFlawRating.objects.get(mf=fetish, character=self).rating
            self.random_fetish(min_rating=rating - 4, max_rating=rating - 4)
        return super().mf_based_corrections()

    def add_fetish(self, fetish):
        if fetish in self.fetishes_owned.all():
            return False
        self.fetishes_owned.add(fetish)
        return True

    def filter_fetishes(self, min_rating=0, max_rating=5):
        return Fetish.objects.filter(
            rank__lte=max_rating, rank__gte=min_rating
        ).exclude(pk__in=self.fetishes_owned.all())

    def random_fetish(self, min_rating=0, max_rating=5):
        options = self.filter_fetishes(min_rating=min_rating, max_rating=max_rating)
        if options.count() != 0:
            choice = random.choice(options)
            return self.add_fetish(choice)
        return False

    def random(self, freebies=15, xp=0, ethnicity=None):
        self.willpower = 3
        self.freebies = freebies
        self.xp = xp
        self.random_name(ethnicity=ethnicity)
        self.random_concept()
        self.random_archetypes()
        self.random_breed()
        self.random_tribe()
        self.random_relation()
        self.random_attributes(primary=6, secondary=4, tertiary=3)
        self.random_abilities(primary=11, secondary=7, tertiary=4)
        self.random_backgrounds()
        self.random_history()
        self.random_finishing_touches()
        self.random_freebies()
        self.mf_based_corrections()
        self.random_xp()
        self.random_specialties()
        self.save()
