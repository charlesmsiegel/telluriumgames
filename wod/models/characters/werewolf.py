import random

from django.contrib.auth.models import User
from django.db import models

from accounts.models import WoDProfile
from core.utils import add_dot, weighted_choice
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
    type = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name


class Werewolf(Human):
    type = "garou"

    rank_names = {
        1: "Cliath",
        2: "Fostern",
        3: "Adren",
        4: "Athro",
        5: "Elder",
    }

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

    allies = models.IntegerField(default=0)
    ancestors = models.IntegerField(default=0)
    fate = models.IntegerField(default=0)
    fetish = models.IntegerField(default=0)
    kinfolk = models.IntegerField(default=0)
    pure_breed = models.IntegerField(default=0)
    resources = models.IntegerField(default=0)
    rites = models.IntegerField(default=0)
    spirit_heritage = models.IntegerField(default=0)
    totem = models.IntegerField(default=0)

    gnosis = models.IntegerField(default=0)
    rage = models.IntegerField(default=0)

    glory = models.IntegerField(default=0)
    temporary_glory = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    temporary_wisdom = models.IntegerField(default=0)
    honor = models.IntegerField(default=0)
    temporary_honor = models.IntegerField(default=0)

    renown_incidents = models.JSONField(default=list)

    gifts = models.ManyToManyField(Gift, blank=True)
    rites_known = models.ManyToManyField(Rite, blank=True)

    first_change = models.TextField(default="")
    battle_scars = models.TextField(default="")
    age_of_first_change = models.IntegerField(default=0)

    requirements = {
        "ragabash": {
            1: {"total": 3},
            2: {"total": 7},
            3: {"total": 13},
            4: {"total": 19},
            5: {"total": 25},
        },
        "theurge": {
            1: {"glory": 0, "honor": 0, "wisdom": 3},
            2: {"glory": 1, "honor": 0, "wisdom": 5},
            3: {"glory": 2, "honor": 1, "wisdom": 7},
            4: {"glory": 4, "honor": 2, "wisdom": 9},
            5: {"glory": 4, "honor": 9, "wisdom": 10},
        },
        "philodox": {
            1: {"glory": 0, "honor": 3, "wisdom": 0},
            2: {"glory": 1, "honor": 4, "wisdom": 1},
            3: {"glory": 2, "honor": 6, "wisdom": 2},
            4: {"glory": 3, "honor": 8, "wisdom": 4},
            5: {"glory": 4, "honor": 10, "wisdom": 9},
        },
        "galliard": {
            1: {"glory": 2, "honor": 0, "wisdom": 1},
            2: {"glory": 4, "honor": 0, "wisdom": 2},
            3: {"glory": 4, "honor": 2, "wisdom": 4},
            4: {"glory": 7, "honor": 2, "wisdom": 6},
            5: {"glory": 9, "honor": 5, "wisdom": 9},
        },
        "ahroun": {
            1: {"glory": 2, "honor": 1, "wisdom": 0},
            2: {"glory": 4, "honor": 1, "wisdom": 1},
            3: {"glory": 6, "honor": 3, "wisdom": 1},
            4: {"glory": 9, "honor": 4, "wisdom": 2},
            5: {"glory": 10, "honor": 9, "wisdom": 4},
        },
    }

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
        return self.breed != ""

    def set_breed(self, breed):
        self.breed = breed
        if breed == "homid":
            self.set_gnosis(1)
        elif breed == "metis":
            self.set_gnosis(3)
        elif breed == "lupus":
            self.set_gnosis(5)
        self.save()
        return True

    def random_breed(self):
        return self.set_breed(random.choice(["homid", "metis", "lupus"]))

    def has_auspice(self):
        return self.auspice != ""

    def set_auspice(self, auspice, ragabash_renown=(1, 1, 1)):
        self.auspice = auspice
        if auspice == "ragabash":
            self.set_glory(ragabash_renown[0])
            self.set_honor(ragabash_renown[1])
            self.set_wisdom(ragabash_renown[2])
            self.set_rage(1)
        elif auspice == "theurge":
            self.set_glory(0)
            self.set_honor(0)
            self.set_wisdom(3)
            self.set_rage(2)
        elif auspice == "philodox":
            self.set_glory(0)
            self.set_honor(3)
            self.set_wisdom(0)
            self.set_rage(3)
        elif auspice == "galliard":
            self.set_glory(2)
            self.set_honor(0)
            self.set_wisdom(1)
            self.set_rage(4)
        elif auspice == "ahroun":
            self.set_glory(2)
            self.set_honor(1)
            self.set_wisdom(0)
            self.set_rage(5)
        self.save()
        return True

    def random_auspice(self):
        choice = random.choice(
            ["ragabash", "theurge", "philodox", "galliard", "ahroun"]
        )
        if choice == "ragabash":
            g = random.randint(0, 3)
            h = random.randint(0, 3 - g)
            w = 3 - g - h
            ragabash_renown = [g, h, w]
        else:
            ragabash_renown = [1, 1, 1]
        return self.set_auspice(choice, ragabash_renown=ragabash_renown)

    def has_tribe(self):
        return self.tribe is not None

    def set_tribe(self, tribe):
        if tribe.name == "Red Talons" and self.breed == "homid":
            return False
        if tribe.name == "Black Furies" and self.sex == "Male":
            return False
        self.tribe = tribe
        self.willpower = tribe.willpower
        if self.tribe.name == "Silver Fangs" and self.pure_breed < 3:
            self.pure_breed = 3
        self.save()
        return True

    def random_tribe(self):
        value = True
        while self.tribe is None:
            value = self.set_tribe(Tribe.objects.order_by("?").first())
        return value

    def has_camp(self):
        return self.camp is not None

    def set_camp(self, camp):
        self.camp = camp
        self.save()
        return True

    def random_camp(self):
        return self.set_camp(
            Camp.objects.filter(tribe=self.tribe).order_by("?").first()
        )

    def add_gift(self, gift):
        self.gifts.add(gift)
        self.save()
        return True

    def filter_gifts(self):
        return [
            x
            for x in Gift.objects.filter(rank__lte=self.rank)
            if x not in self.gifts.all()
        ]

    def has_gifts(self):
        b = self.gifts.count() >= 3
        b = (
            b
            and len(
                [x for x in self.gifts.all() if self.tribe.name in x.allowed["garou"]]
            )
            > 0
        )
        b = (
            b
            and len([x for x in self.gifts.all() if self.auspice in x.allowed["garou"]])
            > 0
        )
        b = (
            b
            and len([x for x in self.gifts.all() if self.breed in x.allowed["garou"]])
            > 0
        )
        return b

    def choose_random_gift(
        self, breed=False, tribe=False, auspice=False, min_rank=1, max_rank=5
    ):
        while True:
            index = random.randint(1, Gift.objects.last().id)
            if Gift.objects.filter(pk=index).exists():
                choice = Gift.objects.get(pk=index)
                correct = True
                if breed and self.breed not in choice.allowed["garou"]:
                    correct = False
                if auspice and self.auspice not in choice.allowed["garou"]:
                    correct = False
                if tribe and self.tribe.name not in choice.allowed["garou"]:
                    correct = False
                if choice.rank < min_rank:
                    correct = False
                if choice.rank > max(max_rank, self.rank):
                    correct = False
                if correct:
                    return choice

    def random_gift(
        self, breed=False, tribe=False, auspice=False, min_rank=1, max_rank=5
    ):
        possible_gifts = self.filter_gifts()
        possible_gifts = [x for x in possible_gifts if min_rank <= x.rank <= max_rank]
        if breed:
            possible_gifts = [
                x for x in possible_gifts if self.breed in x.allowed["garou"]
            ]
        if tribe:
            possible_gifts = [
                x for x in possible_gifts if self.tribe.name in x.allowed["garou"]
            ]
        if auspice:
            possible_gifts = [
                x for x in possible_gifts if self.auspice in x.allowed["garou"]
            ]
        choice = random.choice(possible_gifts)
        return self.add_gift(choice)

    def random_gifts(self):
        self.random_gift(breed=True)
        self.random_gift(tribe=True)
        self.random_gift(auspice=True)

    def add_rite(self, rite):
        self.rites_known.add(rite)
        self.save()
        return True

    def filter_rites(self):
        return [x for x in Rite.objects.all() if x not in self.rites_known.all()]

    def has_rites(self):
        return self.rites == self.total_rites()

    def total_rites(self):
        return (
            sum(x.level for x in self.rites_known.all())
            + self.rites_known.filter(level=0).count() / 2
        )

    def random_rite(self, max_level=5):
        possibilities = [x for x in self.filter_rites() if x.level <= max_level]
        if len(possibilities) == 0:
            return False
        choice = random.choice(possibilities)
        return self.add_rite(choice)

    def random_rites(self):
        while not self.has_rites():
            self.random_rite(max_level=self.rites - self.total_rites())

    def set_glory(self, glory):
        self.glory = glory
        self.save()
        return True

    def set_honor(self, honor):
        self.honor = honor
        self.save()
        return True

    def set_wisdom(self, wisdom):
        self.wisdom = wisdom
        self.save()
        return True

    def has_renown(self):
        return (self.glory + self.honor + self.wisdom) == 3

    def update_renown(self):
        if self.temporary_glory >= 10:
            self.glory += 1
            self.temporary_glory -= 10
        if self.temporary_honor >= 10:
            self.honor += 1
            self.temporary_honor -= 10
        if self.temporary_wisdom >= 10:
            self.wisdom += 1
            self.temporary_wisdom -= 10

    def num_renown_incidents(self):
        return len(self.renown_incidents)

    def add_renown_incident(self, r):
        self.renown_incidents.append(r.name)
        self.temporary_glory += r.glory
        self.temporary_honor += r.honor
        self.temporary_wisdom += r.wisdom
        return True

    def random_renown_incident(self):
        if self.rank != 5 and self.auspice != "ragabash":
            reqs = self.requirements[self.auspice][self.rank + 1]
            glory = reqs["glory"] - self.glory
            honor = reqs["honor"] - self.honor
            wisdom = reqs["wisdom"] - self.wisdom
        else:
            glory = 10 - self.glory
            honor = 10 - self.honor
            wisdom = 10 - self.wisdom
        d = {
            r: sum([glory * r.glory, wisdom * r.wisdom, honor * r.honor])
            for r in RenownIncident.objects.all()
        }
        r = weighted_choice(d, floor=1, ceiling=20)
        return self.add_renown_incident(r)

    def add_gnosis(self):
        return add_dot(self, "gnosis", 10)

    def set_gnosis(self, gnosis):
        self.gnosis = gnosis
        self.save()
        return True

    def add_rage(self):
        return add_dot(self, "rage", 10)

    def set_rage(self, rage):
        self.rage = rage
        self.save()
        return True

    def set_rank(self, rank):
        self.rank = rank
        self.save()
        return True

    def increase_rank(self):
        if self.rank < 5:
            requirements = self.requirements[self.auspice][self.rank + 1]
            if "total" in requirements.keys():
                allowed = self.glory + self.honor + self.wisdom >= requirements["total"]
            else:
                allowed = (
                    (self.glory >= requirements["glory"])
                    and (self.honor >= requirements["honor"])
                    and (self.wisdom >= requirements["wisdom"])
                )
            if allowed:
                self.set_rank(self.rank + 1)
                self.save()
                return True
        return False

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

    def random_werewolf_history(self):
        self.first_change = "Young"
        self.battle_scars = "Several"
        self.age_of_first_change = 13

    def spend_freebies(self, trait):
        output = super().spend_freebies(trait)
        if output in [True, False]:
            return output
        if trait == "rage":
            cost = self.freebie_cost("rage")
            if cost <= self.freebies:
                if self.add_rage():
                    self.freebies -= cost
                    return True
                return False
            return False
        if trait == "gnosis":
            cost = self.freebie_cost("gnosis")
            if cost <= self.freebies:
                if self.add_gnosis():
                    self.freebies -= cost
                    return True
                return False
            return False
        if Gift.objects.filter(name=trait).exists():
            cost = self.freebie_cost("gift")
            g = Gift.objects.get(name=trait)
            if (
                self.auspice in g.allowed["garou"]
                or self.breed in g.allowed["garou"]
                or self.tribe.name in g.allowed["garou"]
            ):
                if cost <= self.freebies:
                    if self.add_gift(g):
                        self.freebies -= cost
                        return True
                    return False
                return False
            return False
        return trait

    def random_freebies(self):
        frequencies = {
            "attribute": 15,
            "ability": 8,
            "background": 10,
            "willpower": 1,
            "meritflaw": 50,
            "gift": 25,
            "rage": 5,
            "gnosis": 1,
        }
        while self.freebies > 0:
            choice = weighted_choice(frequencies)
            if choice == "attribute":
                trait = weighted_choice(self.get_attributes())
                self.spend_freebies(trait)
            if choice == "ability":
                trait = weighted_choice(self.get_abilities())
                self.spend_freebies(trait)
            if choice == "background":
                trait = weighted_choice(self.get_backgrounds())
                self.spend_freebies(trait)
            if choice == "willpower":
                self.spend_freebies(choice)
            if choice == "meritflaw":
                trait = random.choice([x.name for x in self.filter_mfs()])
                self.spend_freebies(trait)
            if choice == "gift":
                trait = random.choice(self.filter_gifts())
                self.spend_freebies(trait)
            if choice == "gnosis":
                self.spend_freebies(choice)
            if choice == "rage":
                self.spend_freebies(choice)

    def spend_xp(self, trait):
        output = super().spend_xp(trait)
        if output in [True, False]:
            return output
        if trait == "rage":
            cost = self.xp_cost("rage") * getattr(self, trait)
            if cost <= self.xp:
                if self.add_rage():
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if trait == "gnosis":
            cost = self.xp_cost("gnosis") * getattr(self, trait)
            if cost <= self.xp:
                if self.add_gnosis():
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if Gift.objects.filter(name=trait).exists():
            g = Gift.objects.get(name=trait)
            if (
                self.auspice in g.allowed["garou"]
                or self.breed in g.allowed["garou"]
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

    def random_xp(self):
        frequencies = {
            "attribute": 15,
            "ability": 20,
            "background": 15,
            "willpower": 5,
            "gift": 35,
            "rage": 5,
            "gnosis": 5,
        }
        starting_xp = self.xp
        renown_frequency_at_rank = {
            1: 3,
            2: 3,
            3: 3,
            4: 3,
            5: 3,
        }
        counter = 0
        while counter < 10000 and self.xp > 0:
            choice = weighted_choice(frequencies)
            if choice == "attribute":
                trait = weighted_choice(self.get_attributes())
                spent = self.spend_xp(trait)
            if choice == "ability":
                trait = weighted_choice(self.get_abilities())
                spent = self.spend_xp(trait)
            if choice == "background":
                trait = weighted_choice(self.get_backgrounds())
                spent = self.spend_xp(trait)
            if choice == "willpower":
                spent = self.spend_xp(choice)
            if choice == "gnosis":
                spent = self.spend_xp(choice)
            if choice == "gift":
                trait = self.choose_random_gift()
                spent = self.spend_xp(trait)
            if choice == "rage":
                spent = self.spend_xp(choice)
            if not spent:
                counter += 1
            num_renown_to_add = (starting_xp - self.xp) // renown_frequency_at_rank[
                self.rank
            ] - self.num_renown_incidents()
            for _ in range(num_renown_to_add):
                self.random_renown_incident()
                self.update_renown()
                if self.increase_rank():
                    starting_xp = self.xp

    def random(self, freebies=15, xp=0, ethnicity=None):
        self.freebies = freebies
        self.xp = xp
        self.random_name(ethnicity=ethnicity)
        self.random_concept()
        self.random_archetypes()
        self.random_breed()
        self.random_auspice()
        self.random_tribe()
        if random.random() < 0.2:
            self.random_camp()
        self.random_attributes()
        self.random_abilities()
        self.random_backgrounds()
        self.random_gifts()
        self.random_rites()
        self.random_history()
        self.random_finishing_touches()
        self.random_werewolf_history()
        self.random_freebies()
        self.random_xp()
        self.random_specialties()
        self.save()


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
        self.save()
        return True

    def has_totem(self):
        return self.totem is not None

    def random_totem(self):
        filtered = list(Totem.objects.filter(cost__lte=self.total_totem()))
        if len(filtered) == 0:
            return False
        return self.set_totem(random.choice(filtered))

    def total_totem(self):
        return sum(x.totem for x in self.members.all())

    def __str__(self):
        return self.name


class RenownIncident(models.Model):
    name = models.CharField(max_length=100, unique=True)

    glory = models.IntegerField(default=0)
    honor = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)

    def __str__(self):
        return self.name
