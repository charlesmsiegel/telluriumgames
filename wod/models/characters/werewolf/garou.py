import random
from collections import defaultdict

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.urls import reverse

from core.models import Model
from core.utils import add_dot, weighted_choice
from wod.models.characters.human import Derangement, Group, Human
from wod.models.characters.werewolf.spirits import Totem
from wod.models.items.werewolf import Fetish

from .wtahuman import WtAHuman


class Tribe(Model):
    type = "tribe"

    willpower = models.IntegerField(default=3)

    class Meta:
        verbose_name = "Tribe"
        verbose_name_plural = "Tribes"

    def get_absolute_url(self):
        return reverse("wod:characters:werewolf:tribe", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("wod:characters:werewolf:update_tribe", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wta_heading"

    def camp_list(self):
        return ", ".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in Camp.objects.filter(tribe=self)
            ]
        )

    def gifts_level_1(self):
        level = [
            x for x in Gift.objects.filter(rank=1) if self.name in x.allowed["garou"]
        ]
        return [f'<a href="{x.get_absolute_url()}">{x}</a>' for x in level]

    def gifts_level_2(self):
        level = [
            x for x in Gift.objects.filter(rank=2) if self.name in x.allowed["garou"]
        ]
        return [f'<a href="{x.get_absolute_url()}">{x}</a>' for x in level]

    def gifts_level_3(self):
        level = [
            x for x in Gift.objects.filter(rank=3) if self.name in x.allowed["garou"]
        ]
        return [f'<a href="{x.get_absolute_url()}">{x}</a>' for x in level]

    def gifts_level_4(self):
        level = [
            x for x in Gift.objects.filter(rank=4) if self.name in x.allowed["garou"]
        ]
        return [f'<a href="{x.get_absolute_url()}">{x}</a>' for x in level]

    def gifts_level_5(self):
        level = [
            x for x in Gift.objects.filter(rank=5) if self.name in x.allowed["garou"]
        ]
        return [f'<a href="{x.get_absolute_url()}">{x}</a>' for x in level]

    def gifts_level_6(self):
        level = [
            x for x in Gift.objects.filter(rank=6) if self.name in x.allowed["garou"]
        ]
        return [f'<a href="{x.get_absolute_url()}">{x}</a>' for x in level]


class Camp(Model):
    type = "camp"

    tribe = models.ForeignKey(Tribe, blank=True, null=True, on_delete=models.SET_NULL)
    camp_type = models.CharField(
        max_length=100,
        default="camp",
        choices=[
            ("camp", "Camp"),
            ("lodge", "Lodge"),
            ("house", "House"),
            ("philosophy", "Philosophy"),
        ],
    )

    class Meta:
        verbose_name = "Camp"
        verbose_name_plural = "Camps"

    def get_absolute_url(self):
        return reverse("wod:characters:werewolf:camp", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("wod:characters:werewolf:update_camp", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wta_heading"


class Gift(Model):
    type = "gift"

    rank = models.IntegerField(default=0)
    allowed = models.JSONField(default=dict)

    class Meta:
        verbose_name = "Gift"
        verbose_name_plural = "Gifts"

    def save(self, *args, **kwargs):
        if "garou" not in self.allowed:
            self.allowed["garou"] = []
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("wod:characters:werewolf:gift", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("wod:characters:werewolf:update_gift", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wta_heading"


class Rite(Model):
    type = "rite"

    level = models.IntegerField(default=0)
    rite_type = models.CharField(max_length=100, default="")

    class Meta:
        verbose_name = "Rite"
        verbose_name_plural = "Rites"

    def get_absolute_url(self):
        return reverse("wod:characters:werewolf:rite", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("wod:characters:werewolf:update_rite", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wta_heading"


class Werewolf(WtAHuman):
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
    tribe = models.ForeignKey(Tribe, blank=True, null=True, on_delete=models.SET_NULL)
    camps = models.ManyToManyField(Camp, blank=True)

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
    fetishes_owned = models.ManyToManyField(Fetish, blank=True)

    first_change = models.TextField(default="")
    battle_scars = models.ManyToManyField("BattleScar", blank=True)
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

    class Meta:
        verbose_name = "Werewolf"
        verbose_name_plural = "Werewolves"

    def get_update_url(self):
        return reverse(
            "wod:characters:werewolf:update_werewolf", kwargs={"pk": self.pk}
        )

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
        if self.tribe.name == "Black Spiral Dancers":
            self.random_derangement()
        self.save()
        return True

    def random_tribe(self):
        value = True
        while self.tribe is None:
            value = self.set_tribe(Tribe.objects.order_by("?").first())
        return value

    def has_camp(self):
        return self.camps.count() != 0

    def add_camp(self, camp):
        self.camps.add(camp)
        self.save()
        return True

    def random_camp(self, camp_type="camp"):
        if self.tribe.name == "Silver Fangs":
            lodge = (
                Camp.objects.filter(camp_type="lodge", tribe=self.tribe)
                .order_by("?")
                .first()
            )
            house = (
                Camp.objects.filter(camp_type="house", tribe=self.tribe)
                .order_by("?")
                .first()
            )
            philosophy = (
                Camp.objects.filter(camp_type="philosophy", tribe=self.tribe)
                .order_by("?")
                .first()
            )
            return (
                self.add_camp(lodge)
                and self.add_camp(house)
                and self.add_camp(philosophy)
            )
        fltr = Q(tribe=self.tribe) | Q(tribe=None)
        return self.add_camp(
            Camp.objects.filter(fltr).filter(camp_type=camp_type).order_by("?").first()
        )

    def add_gift(self, gift):
        if gift in self.gifts.all():
            return False
        self.gifts.add(gift)
        self.save()
        return True

    def filter_gifts(self):
        return Gift.objects.filter(rank__lte=self.rank).exclude(pk__in=self.gifts.all())

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
                if "kinfolk" in choice.allowed["garou"]:
                    return False
                if breed and self.breed not in choice.allowed["garou"]:
                    correct = False
                if auspice and self.auspice not in choice.allowed["garou"]:
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
            if self.camps.count() != 0:
                possible_gifts.extend(
                    [
                        x
                        for x in possible_gifts
                        if len(
                            set(x.name for x in self.camps.all()).intersection(
                                set(x.allowed["garou"])
                            )
                        )
                        != 0
                    ]
                )
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
        return Rite.objects.exclude(pk__in=self.rites_known.all())

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

    def add_renown_incident(self, r, rite=None):
        if r.breed != "":
            if r.breed != self.breed:
                return False
        if r.rite is not None:
            if r.rite not in self.rites_known.all():
                return False
        if r.only_once and r.name in self.renown_incidents:
            return False
        if len(self.renown_incidents) != 0:
            if RenownIncident.objects.get(name=self.renown_incidents[-1]).posthumous:
                return False
        self.renown_incidents.append(r.name)
        self.temporary_glory += r.glory
        self.temporary_honor += r.honor
        self.temporary_wisdom += r.wisdom
        self.temporary_glory = max(0, self.temporary_glory)
        self.temporary_honor = max(0, self.temporary_honor)
        self.temporary_wisdom = max(0, self.temporary_wisdom)
        if r.name == "Learning a new rite":
            if rite is not None:
                self.add_rite(rite)
            else:
                self.random_rite()
            self.renown_incidents[-1] += f"({self.rites_known.last().name})"
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
        cost = super().xp_cost(trait)
        if cost != 10000:
            return cost
        costs = defaultdict(
            lambda: 10000, {"gift": 3, "outside gift": 5, "rage": 1, "gnosis": 2,},
        )
        return costs[trait]

    def freebie_cost(self, trait):
        cost = super().freebie_cost(trait)
        if cost != 10000:
            return cost
        costs = defaultdict(lambda: 10000, {"gift": 7, "rage": 1, "gnosis": 2,},)
        return costs[trait]

    def has_werewolf_history(self):
        return (self.first_change != "") and (self.age_of_first_change != 0)

    def add_battle_scar(self, scar):
        if scar not in self.battle_scars.all():
            self.battle_scars.add(scar)
            self.temporary_glory += scar.glory
            self.update_renown()
            self.save()
            return True
        return False

    def random_battle_scar(self):
        scars = BattleScar.objects.exclude(pk__in=self.battle_scars.all())
        if scars.count() > 0:
            choice = scars.order_by("?").first()
            return self.add_battle_scar(choice)
        return False

    def random_werewolf_history(self):
        self.first_change = "Young"
        self.age_of_first_change = 13
        self.save()

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

    def freebie_frequencies(self):
        return {
            "attribute": 15,
            "ability": 8,
            "background": 10,
            "willpower": 2,
            "meritflaw": 50,
            "gift": 25,
            "rage": 2,
            "gnosis": 2,
        }

    def random_freebie_functions(self):
        return {
            "attribute": self.random_freebies_attributes,
            "ability": self.random_freebies_abilities,
            "background": self.random_freebies_background,
            "willpower": self.random_freebies_willpower,
            "meritflaw": self.random_freebies_meritflaw,
            "gift": self.random_freebies_gift,
            "rage": self.random_freebies_rage,
            "gnosis": self.random_freebies_gnosis,
        }

    def random_freebies_gift(self):
        all_possible = list(self.filter_gifts())
        breed = [x for x in all_possible if self.breed in x.allowed["garou"]]
        auspice = [x for x in all_possible if self.auspice in x.allowed["garou"]]
        tribe = [x for x in all_possible if self.tribe.name in x.allowed["garou"]]
        possible = breed + auspice + tribe
        if len(possible) != 0:
            trait = random.choice(possible).name
            return self.spend_freebies(trait)
        return False

    def random_freebies_rage(self):
        return self.spend_freebies("rage")

    def random_freebies_gnosis(self):
        return self.spend_freebies("gnosis")

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

    def xp_frequencies(self):
        return {
            "attribute": 15,
            "ability": 20,
            "background": 15,
            "willpower": 5,
            "gift": 35,
            "rage": 5,
            "gnosis": 5,
        }

    def random_xp_functions(self):
        return {
            "attribute": self.random_xp_attributes,
            "ability": self.random_xp_abilities,
            "background": self.random_xp_background,
            "willpower": self.random_xp_willpower,
            "gift": self.random_xp_gift,
            "rage": self.random_xp_rage,
            "gnosis": self.random_xp_gnosis,
        }

    def random_xp_gift(self):
        trait = self.choose_random_gift()
        return self.spend_xp(trait)

    def random_xp_rage(self):
        return self.spend_xp("rage")

    def random_xp_gnosis(self):
        return self.spend_xp("gnosis")

    def random_xp(self):
        frequencies = self.xp_frequencies()
        counter = 0
        starting_xp = self.xp
        renown_frequency_at_rank = {
            1: 3,
            2: 3,
            3: 3,
            4: 3,
            5: 3,
        }
        while counter < 10000 and self.xp > 0:
            choice = weighted_choice(frequencies)
            spent = self.random_xp_functions()[choice]()
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

    def random_fetishes(self, total_rating=0):
        total = self.total_fetish_rating() + total_rating
        while self.total_fetish_rating() < total:
            self.random_fetish(
                max_rating=total - self.total_fetish_rating(), min_rating=1
            )

    def total_fetish_rating(self):
        return sum(x.rank for x in self.fetishes_owned.all())

    def random(self, freebies=15, xp=0, ethnicity=None):
        self.update_status("Ran")
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
        self.mf_based_corrections()
        self.random_xp()
        self.random_specialties()
        self.random_fetishes(total_rating=self.fetish)
        self.save()


class Pack(Group):
    type = "pack"

    totem = models.ForeignKey(Totem, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Pack"
        verbose_name_plural = "Packs"

    def get_update_url(self):
        return reverse("wod:characters:werewolf:update_pack", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wta_heading"

    def random(self, num_chars=None, new_characters=True, freebies=15, xp=0, user=None):
        super().random(
            num_chars=num_chars,
            new_characters=new_characters,
            freebies=freebies,
            xp=xp,
            user=user,
            member_type=Werewolf,
        )
        self.random_totem()

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


class RenownIncident(Model):
    type = "renown_incident"

    glory = models.IntegerField(default=0)
    honor = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)

    posthumous = models.BooleanField(default=False)
    only_once = models.BooleanField(default=False)
    breed = models.CharField(default="", max_length=10)
    rite = models.ForeignKey(Rite, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Renown Incident"
        verbose_name_plural = "Renown Incidents"

    def get_absolute_url(self):
        return reverse("wod:characters:werewolf:renownincident", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse(
            "wod:characters:werewolf:update_renownincident", kwargs={"pk": self.pk}
        )

    def get_heading(self):
        return "wta_heading"


class BattleScar(Model):
    type = "battle_scar"

    glory = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Battle Scar"
        verbose_name_plural = "Battle Scars"

    def get_absolute_url(self):
        return reverse("wod:characters:werewolf:battlescar", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse(
            "wod:characters:werewolf:update_battlescar", kwargs={"pk": self.pk}
        )

    def get_heading(self):
        return "wta_heading"
