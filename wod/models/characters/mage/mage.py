import random

from django.contrib.auth.models import User
from django.db import models

from accounts.models import WoDProfile
from core.utils import add_dot, weighted_choice
from wod.models.characters.human import Character, Human
from wod.models.items.mage import Grimoire, Library
from wod.models.locations.mage import Node

from .faction import MageFaction
from .focus import Instrument, Paradigm, Practice
from .resonance import Resonance, ResRating
from .rote import Rote


# Create your models here.
class Mage(Human):
    type = "mage"

    affiliation = models.ForeignKey(
        MageFaction,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="affiliations",
    )
    faction = models.ForeignKey(
        MageFaction,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="factions",
    )
    subfaction = models.ForeignKey(
        MageFaction,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subfactions",
    )

    essence = models.CharField(
        default="",
        max_length=100,
        choices=[
            ("dynamic", "Dynamic"),
            ("pattern", "Pattern"),
            ("primordial", "Primordial"),
            ("questing", "Questing"),
        ],
    )

    awareness = models.IntegerField(default=0)
    art = models.IntegerField(default=0)
    leadership = models.IntegerField(default=0)
    animal_kinship = models.IntegerField(default=0)
    blatancy = models.IntegerField(default=0)
    carousing = models.IntegerField(default=0)
    do = models.IntegerField(default=0)
    flying = models.IntegerField(default=0)
    high_ritual = models.IntegerField(default=0)
    lucid_dreaming = models.IntegerField(default=0)
    search = models.IntegerField(default=0)
    seduction = models.IntegerField(default=0)
    martial_arts = models.IntegerField(default=0)
    meditation = models.IntegerField(default=0)
    research = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    technology = models.IntegerField(default=0)
    acrobatics = models.IntegerField(default=0)
    archery = models.IntegerField(default=0)
    biotech = models.IntegerField(default=0)
    energy_weapons = models.IntegerField(default=0)
    hypertech = models.IntegerField(default=0)
    jetpack = models.IntegerField(default=0)
    riding = models.IntegerField(default=0)
    torture = models.IntegerField(default=0)
    cosmology = models.IntegerField(default=0)
    enigmas = models.IntegerField(default=0)
    esoterica = models.IntegerField(default=0)
    law = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    politics = models.IntegerField(default=0)
    area_knowledge = models.IntegerField(default=0)
    belief_systems = models.IntegerField(default=0)
    cryptography = models.IntegerField(default=0)
    demolitions = models.IntegerField(default=0)
    finance = models.IntegerField(default=0)
    lore = models.IntegerField(default=0)
    media = models.IntegerField(default=0)
    pharmacopeia = models.IntegerField(default=0)

    allies = models.IntegerField(default=0)
    alternate_identity = models.IntegerField(default=0)
    arcane = models.IntegerField(default=0)
    avatar = models.IntegerField(default=0)
    backup = models.IntegerField(default=0)
    blessing = models.IntegerField(default=0)
    certification = models.IntegerField(default=0)
    chantry = models.IntegerField(default=0)
    cult = models.IntegerField(default=0)
    demesne = models.IntegerField(default=0)
    destiny = models.IntegerField(default=0)
    dream = models.IntegerField(default=0)
    enhancement = models.IntegerField(default=0)
    fame = models.IntegerField(default=0)
    familiar = models.IntegerField(default=0)
    influence = models.IntegerField(default=0)
    legend = models.IntegerField(default=0)
    library = models.IntegerField(default=0)
    node = models.IntegerField(default=0)
    past_lives = models.IntegerField(default=0)
    patron = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    requisitions = models.IntegerField(default=0)
    resources = models.IntegerField(default=0)
    retainers = models.IntegerField(default=0)
    sanctum = models.IntegerField(default=0)
    secret_weapons = models.IntegerField(default=0)
    spies = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    totem = models.IntegerField(default=0)
    wonder = models.IntegerField(default=0)

    correspondence = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    spirit = models.IntegerField(default=0)
    mind = models.IntegerField(default=0)
    entropy = models.IntegerField(default=0)
    prime = models.IntegerField(default=0)
    forces = models.IntegerField(default=0)
    matter = models.IntegerField(default=0)
    life = models.IntegerField(default=0)

    paradigms = models.ManyToManyField(Paradigm, blank=True)
    practices = models.ManyToManyField(Practice, blank=True)
    instruments = models.ManyToManyField(Instrument, blank=True)

    arete = models.IntegerField(default=0)

    affinity_sphere = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=[
            ("correspondence", "Correspondence"),
            ("time", "Time"),
            ("spirit", "Spirit"),
            ("mind", "Mind"),
            ("entropy", "Entropy"),
            ("prime", "Prime"),
            ("forces", "Forces"),
            ("matter", "Matter"),
            ("life", "Life"),
        ],
    )

    corr_name = models.CharField(
        default="correspondence",
        choices=[("correspondence", "Correspondence"), ("data", "Data")],
        max_length=100,
    )
    prime_name = models.CharField(
        default="prime",
        choices=[("prime", "Prime"), ("primal_utility", "Primal Utility")],
        max_length=100,
    )
    spirit_name = models.CharField(
        default="spirit",
        choices=[("spirit", "Spirit"), ("dimensional_science", "Dimensional Science")],
        max_length=100,
    )

    awakening = models.TextField(default="")
    seekings = models.TextField(default="")
    quiets = models.TextField(default="")
    age_of_awakening = models.IntegerField(default=0)
    avatar_description = models.TextField(default="")

    resonance = models.ManyToManyField("Resonance", through="ResRating")

    rote_points = models.IntegerField(default=6)
    rotes = models.ManyToManyField(Rote, blank=True)

    quintessence = models.IntegerField(default=0)
    paradox = models.IntegerField(default=0)

    library_owned = models.ForeignKey(
        Library, on_delete=models.CASCADE, null=True, blank=True
    )
    node_owned = models.ForeignKey(
        Node, on_delete=models.CASCADE, null=True, blank=True
    )

    background_points = 7

    def __init__(self, *args, **kwargs):
        kwargs["willpower"] = kwargs.get("willpower") or 5
        super().__init__(*args, **kwargs)

    def get_talents(self):
        tmp = super().get_talents()
        tmp.update(
            {
                "awareness": self.awareness,
                "art": self.art,
                "leadership": self.leadership,
                "animal_kinship": self.animal_kinship,
                "blatancy": self.blatancy,
                "carousing": self.carousing,
                "do": self.do,
                "flying": self.flying,
                "high_ritual": self.high_ritual,
                "lucid_dreaming": self.lucid_dreaming,
                "search": self.search,
                "seduction": self.seduction,
            }
        )
        return tmp

    def get_skills(self):
        tmp = super().get_skills()
        tmp.update(
            {
                "martial_arts": self.martial_arts,
                "meditation": self.meditation,
                "research": self.research,
                "survival": self.survival,
                "technology": self.technology,
                "acrobatics": self.acrobatics,
                "archery": self.archery,
                "biotech": self.biotech,
                "energy_weapons": self.energy_weapons,
                "hypertech": self.hypertech,
                "jetpack": self.jetpack,
                "riding": self.riding,
                "torture": self.torture,
            }
        )
        return tmp

    def get_knowledges(self):
        tmp = super().get_knowledges()
        tmp.update(
            {
                "cosmology": self.cosmology,
                "enigmas": self.enigmas,
                "esoterica": self.esoterica,
                "law": self.law,
                "occult": self.occult,
                "politics": self.politics,
                "area_knowledge": self.area_knowledge,
                "belief_systems": self.belief_systems,
                "cryptography": self.cryptography,
                "demolitions": self.demolitions,
                "finance": self.finance,
                "lore": self.lore,
                "media": self.media,
                "pharmacopeia": self.pharmacopeia,
            }
        )
        return tmp

    def add_ability(self, ability, maximum=4):
        if ability == "do":
            if self.faction is not None:
                if self.faction.name != "Akashayana":
                    return False
                return add_dot(self, ability, maximum=min(maximum, self.count_limbs()))
            return False
        return add_dot(self, ability, maximum)

    def count_limbs(self):
        dharmamukti = self.alertness + self.athletics + self.do
        dhyana = self.awareness + self.enigmas + self.meditation
        jivahasta = self.esoterica + self.medicine + self.survival
        karma = self.art + self.crafts + self.etiquette
        prajna = self.academics + self.belief_systems + self.cosmology
        shastamarga = self.academics + self.crafts + self.melee
        sunyakaya = self.medicine + self.stealth + self.subterfuge
        tricanmarga = self.acrobatics + self.athletics + self.esoterica
        limbs = [
            dharmamukti,
            dhyana,
            jivahasta,
            karma,
            prajna,
            shastamarga,
            sunyakaya,
            tricanmarga,
        ]
        limbs = [x for x in limbs if x >= 2]
        return len(limbs)

    def get_backgrounds(self):
        tmp = super().get_backgrounds()
        tmp.update(
            {
                "allies": self.allies,
                "alternate_identity": self.alternate_identity,
                "arcane": self.arcane,
                "avatar": self.avatar,
                "backup": self.backup,
                "blessing": self.blessing,
                "certification": self.certification,
                "chantry": self.chantry,
                "cult": self.cult,
                "demesne": self.demesne,
                "destiny": self.destiny,
                "dream": self.dream,
                "enhancement": self.enhancement,
                "fame": self.fame,
                "familiar": self.familiar,
                "influence": self.influence,
                "legend": self.legend,
                "library": self.library,
                "node": self.node,
                "past_lives": self.past_lives,
                "patron": self.patron,
                "rank": self.rank,
                "requisitions": self.requisitions,
                "resources": self.resources,
                "retainers": self.retainers,
                "sanctum": self.sanctum,
                "secret_weapons": self.secret_weapons,
                "spies": self.spies,
                "status": self.status,
                "totem": self.totem,
                "wonder": self.wonder,
            }
        )
        return tmp

    def get_spheres(self):
        return {
            "correspondence": self.correspondence,
            "time": self.time,
            "spirit": self.spirit,
            "mind": self.mind,
            "entropy": self.entropy,
            "prime": self.prime,
            "forces": self.forces,
            "matter": self.matter,
            "life": self.life,
        }

    def has_faction(self):
        return self.faction is not None

    def set_faction(self, affiliation, faction, subfaction=None):
        if faction.parent != affiliation:
            return False
        if subfaction is not None:
            if subfaction.parent != faction:
                return False
        self.affiliation = affiliation
        self.faction = faction
        self.subfaction = subfaction
        return True

    def random_faction(self):
        self.affiliation = MageFaction.objects.filter(parent=None).order_by("?").first()
        self.faction = (
            MageFaction.objects.filter(parent=self.affiliation).order_by("?").first()
        )
        if (
            random.random() < 0.25
            or self.faction.name == "Order of Hermes"
            or self.affiliation.name == "Technocratic Union"
        ):
            if MageFaction.objects.filter(parent=self.faction).exists():
                self.subfaction = (
                    MageFaction.objects.filter(parent=self.faction)
                    .order_by("?")
                    .first()
                )

    def has_focus(self):
        return (
            self.paradigms.count() > 0
            and self.practices.count() > 0
            and self.instruments.count() >= 7
        )

    def set_focus(self, paradigms, practices, instruments):
        if len(instruments) < 7:
            return False
        self.paradigms.set(paradigms)
        self.practices.set(practices)
        self.instruments.set(instruments)
        return True

    def random_focus(self):
        paradigms = {x: 1 for x in Paradigm.objects.all()}
        practices = {x: 1 for x in Practice.objects.all()}
        instruments = {x: 1 for x in Instrument.objects.all()}
        if self.affiliation:
            for paradigm in self.affiliation.paradigms.all():
                paradigms[paradigm] += 1
            for practice in self.affiliation.practices.all():
                practices[practice] += 1
        if self.faction:
            for paradigm in self.faction.paradigms.all():
                paradigms[paradigm] += 1
            for practice in self.faction.practices.all():
                practices[practice] += 1
        if self.subfaction:
            for paradigm in self.subfaction.paradigms.all():
                paradigms[paradigm] += 1
            for practice in self.subfaction.practices.all():
                practices[practice] += 1
        self.paradigms.add(weighted_choice(paradigms))
        while random.random() < 0.1:
            self.paradigms.add(
                weighted_choice(
                    {
                        k: v
                        for k, v in paradigms.items()
                        if k not in self.paradigms.all()
                    }
                )
            )
        for paradigm in self.paradigms.all():
            for practice in paradigm.practices.all():
                practices[practice] += 1

        self.practices.add(weighted_choice(practices))
        while random.random() < 0.1:
            self.practices.add(
                weighted_choice(
                    {
                        k: v
                        for k, v in practices.items()
                        if k not in self.practices.all()
                    }
                )
            )

        for practice in self.practices.all():
            for instrument in practice.instruments.all():
                instruments[instrument] += 1
        while self.instruments.count() < 7:
            self.instruments.add(weighted_choice(instruments))

    def add_background(self, background, maximum=5):
        if background in ["requisitions", "secret_weapons"]:
            if self.affiliation is not None:
                if self.affiliation.name != "Technocratic Union":
                    return False
                return add_dot(self, background, maximum)
            return False
        return add_dot(self, background, maximum)

    def total_backgrounds(self):
        return (
            super().total_backgrounds() + self.enhancement + self.sanctum + self.totem
        )

    def add_sphere(self, sphere):
        if self.faction is not None:
            if self.faction.name == "Ahl-i-Batin" and sphere == "entropy":
                return False
        return add_dot(self, sphere, self.arete)

    def filter_spheres(self, minimum=0, maximum=5):
        return {
            k: v
            for k, v in self.get_spheres().items()
            if minimum <= v <= min(maximum, self.arete - 1)
        }

    def total_spheres(self):
        return sum(self.get_spheres().values())

    def has_spheres(self):
        if self.affinity_sphere is not None:
            aff_flag = getattr(self, self.affinity_sphere) > 0
        else:
            aff_flag = False
        total = self.total_spheres() == 6
        return aff_flag and total

    def set_affinity_sphere(self, affinity):
        self.affinity_sphere = affinity
        self.add_sphere(affinity)
        return True

    def has_affinity_sphere(self):
        return self.affinity_sphere is not None

    def random_affinity_sphere(self):
        self.set_affinity_sphere(random.choice(list(self.get_spheres().keys())))

    def random_sphere(self):
        if len(self.filter_spheres(maximum=self.arete - 1).keys()) != 0:
            choice = weighted_choice(self.filter_spheres(maximum=self.arete - 1))
            self.add_sphere(choice)
        else:
            raise ValueError(f"All Spheres Maxed out at Arete {self.arete}")

    def random_spheres(self):
        if self.affinity_sphere is None:
            self.random_affinity_sphere()
        while self.total_spheres() < 6:
            self.random_sphere()

    def add_arete(self, freebies=False):
        if freebies:
            cap = 3
        else:
            cap = 10
        return add_dot(self, "arete", cap)

    def random_arete(self):
        self.arete = random.randint(1, 3)
        self.freebies -= (self.arete - 1) * 4

    def has_essence(self):
        return self.essence != ""

    def set_essence(self, essence):
        self.essence = essence
        return True

    def random_essence(self):
        options = ["Dynamic", "Pattern", "Primordial", "Questing"]
        choice = random.choice(options)
        self.set_essence(choice)

    def add_resonance(self, resonance):
        r, _ = ResRating.objects.get_or_create(resonance=resonance, mage=self)
        if r.rating == 5:
            return False
        r.rating += 1
        r.save()
        return True

    def total_resonance(self):
        return sum([x.rating for x in ResRating.objects.filter(mage=self)])

    def resonance_rating(self, resonance):
        if resonance not in self.resonance.all():
            return 0
        return ResRating.objects.get(mage=self, resonance=resonance).rating

    def filter_resonance(self, minimum=0, maximum=5):
        if minimum > 0:
            all_res = Resonance.objects.filter(mage__name__contains=self.name)
        else:
            all_res = Resonance.objects.all()

        all_res = [x for x in all_res if minimum <= self.resonance_rating(x) <= maximum]
        return all_res

    def random_resonance(self):
        if random.random() < 0.7:
            possible = self.filter_resonance(minimum=1, maximum=4)
            if len(possible) > 0:
                choice = random.choice(possible)
                if self.add_resonance(choice):
                    return True
        while True:
            index = random.randint(1, Resonance.objects.last().id)
            if Resonance.objects.filter(pk=index).exists():
                choice = Resonance.objects.get(pk=index)
                if self.resonance_rating(choice) < 5:
                    if self.add_resonance(choice):
                        return True

    def random_ability(self, maximum=4):
        possibilities = self.filter_abilities(maximum=maximum)
        for practice in self.practices.all():
            for ability in practice.abilities:
                if ability in possibilities:
                    possibilities[ability] += 3
        choice = weighted_choice(possibilities, ceiling=100)
        self.add_ability(choice, 5)

    def random_abilities(self):
        ability_types = [13, 9, 5]
        random.shuffle(ability_types)
        while self.total_talents() < ability_types[0]:
            possibilities = self.get_talents()
            for practice in self.practices.all():
                for ability in practice.abilities:
                    if ability in possibilities:
                        possibilities[ability] += 3
            ability_choice = weighted_choice(possibilities, ceiling=100)
            self.add_ability(ability_choice, maximum=3)
        while self.total_skills() < ability_types[1]:
            possibilities = self.get_skills()
            for practice in self.practices.all():
                for ability in practice.abilities:
                    if ability in possibilities:
                        possibilities[ability] += 3
            ability_choice = weighted_choice(possibilities, ceiling=100)
            self.add_ability(ability_choice, maximum=3)
        while self.total_knowledges() < ability_types[2]:
            possibilities = self.get_knowledges()
            for practice in self.practices.all():
                for ability in practice.abilities:
                    if ability in possibilities:
                        possibilities[ability] += 3
            ability_choice = weighted_choice(possibilities, ceiling=100)
            self.add_ability(ability_choice, maximum=3)

    def add_rote(self, rote):
        if rote.is_learnable(self):
            self.rotes.add(rote)
            self.rote_points -= rote.cost()
            return True
        return False

    def has_rotes(self):
        return self.rote_points == 0

    def filter_rotes(self, max_cost=100):
        return [
            x
            for x in Rote.objects.all()
            if x.cost() <= max_cost and x.is_learnable(self)
        ]

    def random_rote(self):
        options = self.filter_rotes(max_cost=self.rote_points)
        rote = random.choice(options)
        self.add_rote(rote)

    def random_rotes(self):
        while self.rote_points > 0:
            self.random_rote()

    def total_rotes(self):
        return sum([x.cost() for x in self.rotes.all()])

    def has_specialties(self):
        output = super().has_specialties()
        for sphere in self.filter_spheres(minimum=4):
            output = output and (self.specialties.filter(stat=sphere).count() > 0)
        return output

    def random_specialties(self):
        super().random_specialties()
        for sphere in self.filter_spheres(minimum=4):
            self.specialties.add(random.choice(self.filter_specialties(stat=sphere)))

    def has_mage_history(self):
        return (
            self.awakening != ""
            and self.seekings != ""
            and self.quiets != ""
            and self.age_of_awakening != 0
            and self.avatar_description != ""
        )

    def random_mage_history(self):
        self.awakening = "A thing that happened"
        self.seekings = "None"
        self.quiets = "None"
        self.age_of_awakening = 15
        self.avatar_description = "An Avatar"

    def random_xp(self):
        frequencies = {
            "attribute": 1,
            "ability": 1,
            "background": 1,
            "willpower": 1,
            "sphere": 1,
            "arete": 1,
        }
        counter = 0
        while counter < 10 and self.xp > 0:
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
            if choice == "arete":
                spent = self.spend_xp(choice)
            if choice == "sphere":
                trait = weighted_choice(self.get_spheres())
                spent = self.spend_xp(trait)
            if not spent:
                counter += 1

    def freebie_cost(self, trait):
        if trait == "attribute":
            return 5
        if trait == "ability":
            return 2
        if trait == "background":
            return 1
        if trait == "willpower":
            return 1
        if trait == "meritflaw":
            return 1
        if trait == "sphere":
            return 7
        if trait == "arete":
            return 4
        if trait == "quintessence":
            return 1
        return 10000

    def spend_freebies(self, trait):
        output = super().spend_freebies(trait)
        if output in [True, False]:
            return output
        if trait in self.get_spheres():
            cost = self.freebie_cost("sphere")
            if cost <= self.freebies:
                if self.add_sphere(trait):
                    self.freebies -= cost
                    return True
                return False
            return False
        if trait == "arete":
            cost = self.freebie_cost("arete")
            if cost <= self.freebies:
                if self.add_arete(trait):
                    self.freebies -= cost
                    return True
                return False
            return False
        if trait == "quintessence":
            cost = self.freebie_cost("quintessence")
            if cost <= self.freebies:
                if self.quintessence < 17:
                    self.quintessence += 4
                    self.freebies -= cost
                    return True
                return False
            return False
        return trait

    def spend_xp(self, trait):
        output = super().spend_xp(trait)
        if output in [True, False]:
            return output
        if trait == "arete":
            cost = self.xp_cost("arete") * getattr(self, trait)
            if cost <= self.xp:
                if self.add_arete():
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if trait in self.get_spheres():
            if self.affinity_sphere == trait:
                cost = self.xp_cost("affinity sphere") * getattr(self, trait)
            else:
                cost = self.xp_cost("sphere") * getattr(self, trait)
            if cost == 0:
                cost = 10
            if cost <= self.xp:
                if self.add_sphere(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        return trait

    def xp_cost(self, trait):
        if trait == "attribute":
            return 4
        if trait == "ability":
            return 2
        if trait == "new ability":
            return 3
        if trait == "background":
            return 3
        if trait == "new background":
            return 5
        if trait == "willpower":
            return 1
        if trait == "affinity sphere":
            return 7
        if trait == "new sphere":
            return 10
        if trait == "sphere":
            return 8
        if trait == "arete":
            return 8
        return 10000

    def random_freebies(self):
        frequencies = {
            "attribute": 1,
            "ability": 1,
            "background": 1,
            "willpower": 1,
            "meritflaw": 1,
            "sphere": 1,
            "arete": 1,
            "quintessence": 1,
        }
        counter = 0
        while counter < 10 and self.freebies > 0:
            choice = weighted_choice(frequencies)
            if choice == "attribute":
                trait = weighted_choice(self.get_attributes())
                spent = self.spend_freebies(trait)
            if choice == "ability":
                trait = weighted_choice(self.get_abilities())
                spent = self.spend_freebies(trait)
            if choice == "background":
                trait = weighted_choice(self.get_backgrounds())
                spent = self.spend_freebies(trait)
            if choice == "willpower":
                spent = self.spend_freebies(choice)
            if choice == "meritflaw":
                trait = random.choice([x.name for x in self.filter_mfs()])
                spent = self.spend_freebies(trait)
            if choice == "sphere":
                trait = weighted_choice(self.get_spheres())
                spent = self.spend_freebies(trait)
            if choice == "arete":
                spent = self.spend_freebies(choice)
            if choice == "quintessence":
                spent = self.spend_freebies(choice)
            if not spent:
                counter += 1

    def has_library(self):
        if self.library_owned is not None:
            return self.library_owned.rank == self.library
        return False

    def random_library(self):
        if self.library > 0:
            l = Library.objects.create(name=f"{self.name}'s Library", rank=self.library)
            l.random()
            l.save()
            self.library_owned = l
            self.save()

    def has_node(self):
        if self.node_owned is not None:
            return self.node_owned.rank == self.node
        return False

    def random_node(self):
        if self.node > 0:
            n = Node.objects.create(name=f"{self.name}'s Node")
            n.random(rank=self.node)
            n.save()
            self.node_owned = n
            self.save()

    def random(self, freebies=15, xp=0):
        self.freebies = freebies
        self.xp = xp
        self.random_name()
        self.random_concept()
        self.random_archetypes()
        self.random_essence()
        self.random_faction()
        self.random_focus()
        self.random_attributes()
        self.random_abilities()
        self.random_backgrounds()
        self.random_arete()
        self.random_affinity_sphere()
        self.random_spheres()
        self.random_history()
        self.random_resonance()
        self.random_rotes()
        self.random_finishing_touches()
        self.random_mage_history()
        self.random_freebies()
        self.random_xp()
        self.random_specialties()
        self.random_node()
        self.random_library()

    def random_name(self):
        if not self.has_name():
            self.set_name(f"Mage {Character.objects.count() - 1}")


class Cabal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(Mage, blank=True)
    leader = models.ForeignKey(
        Mage, blank=True, related_name="leads", on_delete=models.CASCADE, null=True
    )

    def random(self, num_chars, new_characters=False):
        if not new_characters and Mage.objects.count() < num_chars:
            raise ValueError("Not enough Mages!")
        if not new_characters:
            self.members.set(Mage.objects.order_by("?")[:num_chars])
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
                m = Mage.objects.create(
                    name=f"{self.name} {self.members.count() + 1}",
                    player=user.wod_profile,
                )
                m.random()
                self.members.add(m)
        self.leader = self.members.order_by("?").first()
        self.save()

    def __str__(self):
        return self.name
