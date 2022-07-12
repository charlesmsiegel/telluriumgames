import random
from collections import defaultdict

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from core.utils import add_dot, weighted_choice
from wod.models.characters.human import Character, Group, Human
from wod.models.items.mage import Grimoire, Library
from wod.models.locations.mage import Node

from .faction import MageFaction
from .focus import Instrument, Paradigm, Practice
from .resonance import Resonance, ResRating
from .rote import Rote
from .utils import PRIMARY_ABILITIES

PRIMARY_ABILITY_WEIGHTING = 5
PRACTICE_ABILITY_WEIGHTING = 3


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
            ("Dynamic", "Dynamic"),
            ("Pattern", "Pattern"),
            ("Primordial", "Primordial"),
            ("Questing", "Questing"),
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

    cooking = models.IntegerField(default=0)
    diplomacy = models.IntegerField(default=0)
    instruction = models.IntegerField(default=0)
    intrigue = models.IntegerField(default=0)
    intuition = models.IntegerField(default=0)
    mimicry = models.IntegerField(default=0)
    negotiation = models.IntegerField(default=0)
    newspeak = models.IntegerField(default=0)
    scan = models.IntegerField(default=0)
    scrounging = models.IntegerField(default=0)
    style = models.IntegerField(default=0)
    blind_fighting = models.IntegerField(default=0)
    climbing = models.IntegerField(default=0)
    disguise = models.IntegerField(default=0)
    elusion = models.IntegerField(default=0)
    escapology = models.IntegerField(default=0)
    fast_draw = models.IntegerField(default=0)
    fast_talk = models.IntegerField(default=0)
    fencing = models.IntegerField(default=0)
    fortune_telling = models.IntegerField(default=0)
    gambling = models.IntegerField(default=0)
    gunsmith = models.IntegerField(default=0)
    heavy_weapons = models.IntegerField(default=0)
    hunting = models.IntegerField(default=0)
    hypnotism = models.IntegerField(default=0)
    jury_rigging = models.IntegerField(default=0)
    microgravity_operations = models.IntegerField(default=0)
    misdirection = models.IntegerField(default=0)
    networking = models.IntegerField(default=0)
    pilot = models.IntegerField(default=0)
    psychology = models.IntegerField(default=0)
    security = models.IntegerField(default=0)
    speed_reading = models.IntegerField(default=0)
    swimming = models.IntegerField(default=0)
    conspiracy_theory = models.IntegerField(default=0)
    chantry_politics = models.IntegerField(default=0)
    covert_culture = models.IntegerField(default=0)
    cultural_savvy = models.IntegerField(default=0)
    helmsman = models.IntegerField(default=0)
    history_knowledge = models.IntegerField(default=0)
    power_brokering = models.IntegerField(default=0)
    propaganda = models.IntegerField(default=0)
    theology = models.IntegerField(default=0)
    unconventional_warface = models.IntegerField(default=0)
    vice = models.IntegerField(default=0)

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
                "cooking": self.cooking,
                "diplomacy": self.diplomacy,
                "instruction": self.instruction,
                "intrigue": self.intrigue,
                "intuition": self.intuition,
                "mimicry": self.mimicry,
                "negotiation": self.negotiation,
                "newspeak": self.newspeak,
                "scan": self.scan,
                "scrounging": self.scrounging,
                "style": self.style,
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
                "blind_fighting": self.blind_fighting,
                "climbing": self.climbing,
                "disguise": self.disguise,
                "elusion": self.elusion,
                "escapology": self.escapology,
                "fast_draw": self.fast_draw,
                "fast_talk": self.fast_talk,
                "fencing": self.fencing,
                "fortune_telling": self.fortune_telling,
                "gambling": self.gambling,
                "gunsmith": self.gunsmith,
                "heavy_weapons": self.heavy_weapons,
                "hunting": self.hunting,
                "hypnotism": self.hypnotism,
                "jury_rigging": self.jury_rigging,
                "microgravity_operations": self.microgravity_operations,
                "misdirection": self.misdirection,
                "networking": self.networking,
                "pilot": self.pilot,
                "psychology": self.psychology,
                "security": self.security,
                "speed_reading": self.speed_reading,
                "swimming": self.swimming,
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
                "conspiracy_theory": self.conspiracy_theory,
                "chantry_politics": self.chantry_politics,
                "covert_culture": self.covert_culture,
                "cultural_savvy": self.cultural_savvy,
                "helmsman": self.helmsman,
                "history_knowledge": self.history_knowledge,
                "power_brokering": self.power_brokering,
                "propaganda": self.propaganda,
                "theology": self.theology,
                "unconventional_warface": self.unconventional_warface,
                "vice": self.vice,
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
        affiliation_weights = defaultdict(int)
        for faction in MageFaction.objects.filter(parent=None):
            if faction.name == "Traditions":
                affiliation_weights[faction] = 40
            elif faction.name == "Technocratic Union":
                affiliation_weights[faction] = 40
            elif faction.name == "The Disparate Alliance":
                affiliation_weights[faction] = 10
            elif faction.name == "Nephandi":
                affiliation_weights[faction] = 5
            elif faction.name == "Marauders":
                affiliation_weights[faction] = 5
            else:
                affiliation_weights[faction] = 1

        self.affiliation = weighted_choice(affiliation_weights, ceiling=100)
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
        return add_dot(self, sphere, min(self.arete, 5))

    def filter_spheres(self, minimum=0, maximum=5):
        return {k: v for k, v in self.get_spheres().items() if minimum <= v <= maximum}

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
        target = random.randint(1, 3)
        self.arete = 1
        for _ in range(target - 1):
            self.spend_freebies("arete")

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
        return sum(x.rating for x in ResRating.objects.filter(mage=self))

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
        choice = self.choose_random_resonance()
        return self.add_resonance(choice)

    def choose_random_resonance(self):
        if random.random() < 0.7:
            possible = self.filter_resonance(minimum=1, maximum=4)
            if len(possible) > 0:
                choice = random.choice(possible)
                return choice
        while True:
            index = random.randint(1, Resonance.objects.last().id)
            if Resonance.objects.filter(pk=index).exists():
                choice = Resonance.objects.get(pk=index)
                if self.resonance_rating(choice) < 5:
                    return choice

    def random_ability(self, maximum=4):
        possibilities = self.filter_abilities(maximum=maximum)
        for practice in self.practices.all():
            for ability in practice.abilities:
                if ability in possibilities:
                    possibilities[ability] += PRACTICE_ABILITY_WEIGHTING
        for ability in possibilities:
            if ability in PRIMARY_ABILITIES:
                possibilities[ability] *= PRIMARY_ABILITY_WEIGHTING
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
        rotes = Rote.objects.filter(rote_cost__lte=max_cost)

        return [x for x in rotes if x.is_learnable(self)]

    def random_rote(self):
        options = self.filter_rotes(max_cost=self.rote_points)
        rote = random.choice(options)
        self.add_rote(rote)

    def random_rotes(self):
        while self.rote_points > 0:
            self.random_rote()

    def total_rotes(self):
        return sum(x.cost() for x in self.rotes.all())

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

    def xp_frequencies(self):
        return {
            "attribute": 16,
            "ability": 20,
            "background": 13,
            "willpower": 1,
            "sphere": 37,
            "arete": 10,
            "rote points": 2,
        }

    def random_xp_functions(self):
        return {
            "attribute": self.random_xp_attributes,
            "ability": self.random_xp_abilities,
            "background": self.random_xp_background,
            "willpower": self.random_xp_willpower,
            "sphere": self.random_xp_sphere,
            "arete": self.random_xp_arete,
            "rote points": self.random_xp_rote_points,
        }

    def random_xp_sphere(self):
        trait = weighted_choice(self.get_spheres())
        return self.spend_xp(trait)

    def random_xp_arete(self):
        return self.spend_xp("arete")

    def random_xp_rote_points(self):
        return self.spend_xp("rote points")

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
        if trait == "rote points":
            cost = self.xp_cost("rote points")
            if cost <= self.xp:
                self.rote_points += 3
                self.xp -= cost
                self.add_to_spend(trait, getattr(self, trait.replace(" ", "_")), cost)
                return True
            return False
        return trait

    def xp_cost(self, trait):
        cost = super().xp_cost(trait)
        if cost != 10000:
            return cost
        costs = defaultdict(
            lambda: 10000,
            {
                "affinity sphere": 7,
                "new sphere": 10,
                "sphere": 8,
                "arete": 8,
                "rote points": 1,
            },
        )
        return costs[trait]

    def freebie_frequencies(self):
        return {
            "attribute": 15,
            "ability": 8,
            "background": 10,
            "willpower": 1,
            "meritflaw": 50,
            "sphere": 25,
            "arete": 5,
            "quintessence": 1,
            "rote points": 5,
            "resonance": 10,
        }

    def random_freebie_functions(self):
        return {
            "attribute": self.random_freebies_attributes,
            "ability": self.random_freebies_abilities,
            "background": self.random_freebies_background,
            "willpower": self.random_freebies_willpower,
            "meritflaw": self.random_freebies_meritflaw,
            "sphere": self.random_freebies_sphere,
            "arete": self.random_freebies_arete,
            "quintessence": self.random_freebies_quintessence,
            "rote points": self.random_freebies_rote_points,
            "resonance": self.random_freebies_resonance,
        }

    def freebie_cost(self, trait):
        cost = super().freebie_cost(trait)
        if cost != 10000:
            return cost
        costs = defaultdict(
            lambda: 10000,
            {
                "sphere": 7,
                "arete": 4,
                "quintessence": 1,
                "rote points": 1,
                "resonance": 3,
            },
        )
        return costs[trait]

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
                if self.add_arete(freebies=True):
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
        if trait == "rote points":
            cost = self.freebie_cost("rote points")
            if cost <= self.freebies:
                self.rote_points += 4
                self.freebies -= cost
                return True
            return False
        if Resonance.objects.filter(name=trait).exists():
            cost = self.freebie_cost("resonance") * (self.total_resonance() - 1)
            if cost <= self.freebies:
                if self.add_resonance(trait):
                    self.freebies -= cost
                    return True
                return False
            return False
        return trait

    def random_freebies_sphere(self):
        trait = weighted_choice(self.get_spheres())
        self.spend_freebies(trait)

    def random_freebies_arete(self):
        self.spend_freebies("arete")

    def random_freebies_quintessence(self):
        self.spend_freebies("quintessence")

    def random_freebies_rote_points(self):
        self.spend_freebies("rote points")

    def random_freebies_resonance(self):
        trait = self.choose_random_resonance()
        self.spend_freebies(trait)

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

    def random_node(self, favored_list=None):
        if self.node > 0:
            n = Node.objects.create(name=f"{self.name}'s Node")
            n.random(rank=self.node, favored_list=favored_list)
            n.save()
            self.node_owned = n
            self.save()

    def random(self, freebies=15, xp=0, ethnicity=None):
        self.freebies = freebies
        self.xp = xp
        self.random_name(ethnicity=ethnicity)
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
        self.random_finishing_touches()
        self.random_mage_history()
        self.random_freebies()
        self.random_xp()
        self.random_rotes()
        self.random_specialties()
        self.random_node(favored_list=self.resonance.all())
        self.random_library()


class Cabal(Group):
    type = "cabal"

    def random(self, num_chars=None, new_characters=True, freebies=15, xp=0, user=None):
        super().random(
            num_chars=num_chars,
            new_characters=new_characters,
            freebies=freebies,
            xp=xp,
            user=user,
            member_type=Mage,
        )
