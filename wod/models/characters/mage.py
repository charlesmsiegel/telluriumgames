import random

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.utils.timezone import now
from polymorphic.models import PolymorphicModel

from accounts.models import WoDProfile
from core.models import Language, Material, Medium
from core.utils import add_dot, weighted_choice
from wod.models.characters import HumanCharacter, MeritFlaw


# Create your models here.
class Mage(HumanCharacter):
    """Class for Mage Characters"""

    affiliation = models.ForeignKey(
        "MageFaction",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="affiliations",
    )
    faction = models.ForeignKey(
        "MageFaction",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="factions",
    )
    subfaction = models.ForeignKey(
        "MageFaction",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subfactions",
    )

    essence = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        choices=[
            ("DYN", "Dynamic"),
            ("PAT", "Pattern"),
            ("PRI", "Primordial"),
            ("QUE", "Questing"),
        ],
    )

    correspondence = models.IntegerField(default=0)
    forces = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    life = models.IntegerField(default=0)
    spirit = models.IntegerField(default=0)
    matter = models.IntegerField(default=0)
    prime = models.IntegerField(default=0)
    mind = models.IntegerField(default=0)
    entropy = models.IntegerField(default=0)
    correspondence_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    forces_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    time_specialty = models.CharField(max_length=100, default="", blank=True, null=True)
    life_specialty = models.CharField(max_length=100, default="", blank=True, null=True)
    spirit_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    matter_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    prime_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    mind_specialty = models.CharField(max_length=100, default="", blank=True, null=True)
    entropy_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )

    corr_name = models.CharField(
        max_length=3,
        default="COR",
        choices=[("COR", "Correspondence"), ("DAT", "Data")],
    )
    prime_name = models.CharField(
        max_length=3,
        default="PRI",
        choices=[("PRI", "Prime"), ("PU", "Primal Utility")],
    )
    spirit_name = models.CharField(
        max_length=3,
        default="SPI",
        choices=[("SPI", "Spirit"), ("DS", "Dimensional Science")],
    )

    # # Talents
    alertness = models.IntegerField(default=0)
    art = models.IntegerField(default=0)
    athletics = models.IntegerField(default=0)
    awareness = models.IntegerField(default=0)
    brawl = models.IntegerField(default=0)
    empathy = models.IntegerField(default=0)
    expression = models.IntegerField(default=0)
    intimidation = models.IntegerField(default=0)
    leadership = models.IntegerField(default=0)
    streetwise = models.IntegerField(default=0)
    subterfuge = models.IntegerField(default=0)
    # # Skills
    crafts = models.IntegerField(default=0)
    drive = models.IntegerField(default=0)
    etiquette = models.IntegerField(default=0)
    firearms = models.IntegerField(default=0)
    martial_arts = models.IntegerField(default=0)
    meditation = models.IntegerField(default=0)
    melee = models.IntegerField(default=0)
    research = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    technology = models.IntegerField(default=0)
    # # Knowledges
    academics = models.IntegerField(default=0)
    computer = models.IntegerField(default=0)
    cosmology = models.IntegerField(default=0)
    enigmas = models.IntegerField(default=0)
    esoterica = models.IntegerField(default=0)
    investigation = models.IntegerField(default=0)
    law = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    politics = models.IntegerField(default=0)
    science = models.IntegerField(default=0)

    # Secondary Traits
    animal_kinship = models.IntegerField(default=0)
    blatancy = models.IntegerField(default=0)
    carousing = models.IntegerField(default=0)
    do = models.IntegerField(default=0)
    flying = models.IntegerField(default=0)
    high_ritual = models.IntegerField(default=0)
    lucid_dreaming = models.IntegerField(default=0)
    search = models.IntegerField(default=0)
    seduction = models.IntegerField(default=0)

    acrobatics = models.IntegerField(default=0)
    archery = models.IntegerField(default=0)
    biotech = models.IntegerField(default=0)
    energy_weapons = models.IntegerField(default=0)
    hypertech = models.IntegerField(default=0)
    jetpack = models.IntegerField(default=0)
    riding = models.IntegerField(default=0)
    torture = models.IntegerField(default=0)

    area_knowledge = models.IntegerField(default=0)
    belief_systems = models.IntegerField(default=0)
    cryptography = models.IntegerField(default=0)
    demolitions = models.IntegerField(default=0)
    finance = models.IntegerField(default=0)
    lore = models.IntegerField(default=0)
    media = models.IntegerField(default=0)
    pharmacopeia = models.IntegerField(default=0)

    # # Talents
    alertness_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    art_specialty = models.CharField(max_length=100, default="", blank=True, null=True)
    athletics_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    awareness_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    brawl_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    empathy_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    expression_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    intimidation_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    leadership_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    streetwise_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    subterfuge_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    # # Skills
    crafts_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    drive_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    etiquette_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    firearms_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    martial_arts_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    meditation_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    melee_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    research_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    stealth_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    survival_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    technology_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    # # Knowledges
    academics_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    computer_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    cosmology_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    enigmas_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    esoterica_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    investigation_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    law_specialty = models.CharField(max_length=100, default="", blank=True, null=True)
    medicine_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    occult_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    politics_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    science_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )

    # Secondary Traits
    animal_kinship_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    blatancy_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    carousing_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    do_specialty = models.CharField(max_length=100, default="", blank=True, null=True)
    flying_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    high_ritual_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    lucid_dreaming_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    search_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    seduction_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )

    acrobatics_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    archery_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    biotech_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    energy_weapons_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    hypertech_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    jetpack_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    riding_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    torture_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )

    area_knowledge_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    belief_systems_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    cryptography_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    demolitions_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    finance_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    lore_specialty = models.CharField(max_length=100, default="", blank=True, null=True)
    media_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )
    pharmacopeia_specialty = models.CharField(
        max_length=100, default="", blank=True, null=True
    )

    sphere_key = ["Cor", "Ent", "For", "Lif", "Mat", "Min", "Pri", "Spi", "Tim"]
    spheres = [
        "Correspondence",
        "Entropy",
        "Forces",
        "Life",
        "Matter",
        "Mind",
        "Prime",
        "Spirit",
        "Time",
    ]
    affinity_sphere = models.CharField(
        max_length=3, choices=zip(sphere_key, spheres), default="Cor"
    )
    arete = models.IntegerField(default=1)

    # Backgrounds
    allies = models.IntegerField(default=0)
    alternate_identity = models.IntegerField(default=0)
    backup = models.IntegerField(default=0)
    certification = models.IntegerField(default=0)
    contacts = models.IntegerField(default=0)
    destiny = models.IntegerField(default=0)
    dream = models.IntegerField(default=0)
    fame = models.IntegerField(default=0)
    influence = models.IntegerField(default=0)
    mentor = models.IntegerField(default=0)
    patron = models.IntegerField(default=0)
    resources = models.IntegerField(default=0)
    retainers = models.IntegerField(default=0)
    spies = models.IntegerField(default=0)

    arcane = models.IntegerField(default=0)
    avatar = models.IntegerField(default=0)
    chantry = models.IntegerField(default=0)
    cult = models.IntegerField(default=0)
    demesne = models.IntegerField(default=0)
    enhancement = models.IntegerField(default=0)
    familiar = models.IntegerField(default=0)
    legend = models.IntegerField(default=0)
    library = models.IntegerField(default=0)
    node = models.IntegerField(default=0)
    past_lives = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    requisitions = models.IntegerField(default=0)
    sanctum = models.IntegerField(default=0)
    secret_weapons = models.IntegerField(default=0)
    totem = models.IntegerField(default=0)
    wonder = models.IntegerField(default=0)

    willpower = models.IntegerField(default=5)
    rote_points = models.IntegerField(default=6)
    rotes = models.ManyToManyField("Rote", blank=True)
    resonance = models.ManyToManyField("Resonance", through="ResRating")

    quintessence = models.IntegerField(default=0)
    paradox = models.IntegerField(default=0)

    paradigms = models.ManyToManyField("Paradigm", blank=True)
    practices = models.ManyToManyField("Practice", blank=True)
    instruments = models.ManyToManyField("Instrument", blank=True)

    awakening = models.TextField(default="")
    seekings = models.TextField(default="")
    quiets = models.TextField(default="")
    avatar_description = models.TextField(default="")
    age_of_awakening = models.IntegerField(default=16)

    background_points = 7
    type = "mage"

    def total_spheres(self):
        return sum(self.get_spheres().values())

    def get_talents(self):
        return {
            "alertness": self.alertness,
            "awareness": self.awareness,
            "art": self.art,
            "athletics": self.athletics,
            "brawl": self.brawl,
            "empathy": self.empathy,
            "intimidation": self.intimidation,
            "leadership": self.leadership,
            "expression": self.expression,
            "streetwise": self.streetwise,
            "subterfuge": self.subterfuge,
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

    def total_talents(self):
        return sum(self.get_talents().values())

    def get_skills(self):
        return {
            "crafts": self.crafts,
            "drive": self.drive,
            "etiquette": self.etiquette,
            "firearms": self.firearms,
            "martial_arts": self.martial_arts,
            "meditation": self.meditation,
            "melee": self.melee,
            "research": self.research,
            "stealth": self.stealth,
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

    def total_skills(self):
        return sum(self.get_skills().values())

    def get_knowledges(self):
        return {
            "academics": self.academics,
            "computer": self.computer,
            "cosmology": self.cosmology,
            "enigmas": self.enigmas,
            "esoterica": self.esoterica,
            "investigation": self.investigation,
            "law": self.law,
            "medicine": self.medicine,
            "occult": self.occult,
            "politics": self.politics,
            "science": self.science,
            "area_knowledge": self.area_knowledge,
            "belief_systems": self.belief_systems,
            "cryptography": self.cryptography,
            "demolitions": self.demolitions,
            "finance": self.finance,
            "lore": self.lore,
            "media": self.media,
            "pharmacopeia": self.pharmacopeia,
        }

    def total_knowledges(self):
        return sum(self.get_knowledges().values())

    def abilities(self):
        tmp = {}
        tmp.update(self.get_talents())
        tmp.update(self.get_skills())
        tmp.update(self.get_knowledges())
        return tmp

    def random_arete(self, maximum=3):
        self.arete = random.randint(1, maximum)
        self.freebies -= 4 * (self.arete - 1)

    def set_affinity(self, affinity):
        self.affinity_sphere = affinity
        affinity_sphere_name = self.spheres[
            self.sphere_key.index(self.affinity_sphere)
        ].lower()
        add_dot(self, affinity_sphere_name, self.arete)

    def random_affinity(self):
        affinity_choice = random.choice(self.sphere_key)
        self.set_affinity(affinity_choice)

    def random_faction(self):
        self.affiliation = MageFaction.objects.filter(parent=None).order_by("?").first()
        self.faction = (
            MageFaction.objects.filter(parent=self.affiliation).order_by("?").first()
        )
        if random.random() < 0.25:
            self.subfaction = (
                MageFaction.objects.filter(parent=self.faction).order_by("?").first()
            )

    @staticmethod
    def backgrounds():
        return [
            "allies",
            "alternate_identity",
            "backup",
            "certification",
            "contacts",
            "destiny",
            "dream",
            "fame",
            "influence",
            "mentor",
            "patron",
            "resources",
            "retainers",
            "spies",
            "arcane",
            "avatar",
            "chantry",
            "cult",
            "demesne",
            "enhancement",
            "familiar",
            "legend",
            "library",
            "node",
            "past_lives",
            "rank",
            "requisitions",
            "sanctum",
            "secret_weapons",
            "totem",
            "wonder",
        ]

    def total_backgrounds(self):
        values = [getattr(self, x) for x in self.backgrounds()]
        values.extend([self.enhancement, self.sanctum, self.totem])
        return sum(values)

    def random_essence(self):
        options = ["DYN", "PAT", "PRI", "QUE"]
        self.essence = random.choice(options)

    def get_spheres(self):
        return {
            "correspondence": self.correspondence,
            "entropy": self.entropy,
            "forces": self.forces,
            "life": self.life,
            "matter": self.matter,
            "mind": self.mind,
            "prime": self.prime,
            "spirit": self.spirit,
            "time": self.time,
        }

    def random_spheres(self, sphere_total):
        while self.total_spheres() < sphere_total:
            chosen_sphere = weighted_choice(self.get_spheres())
            add_dot(self, chosen_sphere, self.arete)

    def add_resonance_dot(self, resonance):
        if resonance in self.resonance.all():
            res = ResRating.objects.get(mage=self, resonance=resonance)
            res.rating += 1
            res.save()
        else:
            ResRating.objects.create(mage=self, resonance=resonance, rating=1)

    def total_resonance(self):
        return sum([x.rating for x in ResRating.objects.filter(mage=self)])

    def learn_rote(self, rote):
        rote_cost = (
            rote.correspondence
            + rote.time
            + rote.spirit
            + rote.matter
            + rote.forces
            + rote.life
            + rote.prime
            + rote.mind
            + rote.entropy
        )
        if rote_cost < self.rote_points:
            self.rotes.add(rote)
            self.rote_points -= rote_cost
            self.save()

    def random_abilities(self, primary, secondary, tertiary):
        options = [primary, secondary, tertiary]
        random.shuffle(options)
        while self.total_talents() < options[0]:
            ability = weighted_choice(self.get_talents())
            add_dot(self, ability, 3)
        while self.total_skills() < options[1]:
            ability = weighted_choice(self.get_skills())
            add_dot(self, ability, 3)
        while self.total_knowledges() < options[2]:
            ability = weighted_choice(self.get_knowledges())
            add_dot(self, ability, 3)

    def check_starting_abilities(self):
        counts = [self.total_talents(), self.total_skills(), self.total_knowledges()]
        counts.sort()
        return counts == [5, 9, 13]

    def random_focus(self):
        paradigms = list(Paradigm.objects.all())
        practices = list(Practice.objects.all())
        instruments = list(Instrument.objects.all())
        if self.affiliation:
            paradigms.extend(self.affiliation.paradigms.all())
            practices.extend(self.affiliation.practices.all())
        if self.faction:
            paradigms.extend(self.faction.paradigms.all())
            practices.extend(self.faction.practices.all())
        if self.subfaction:
            paradigms.extend(self.subfaction.paradigms.all())
            practices.extend(self.subfaction.practices.all())
        self.paradigms.add(random.choice(paradigms))
        while random.random() < 0.1:
            paradigms = [x for x in paradigms if x not in self.paradigms.all()]
            self.paradigms.add(random.choice(paradigms))
        for paradigm in self.paradigms.all():
            practices.extend(paradigm.practices.all())
        self.practices.add(random.choice(practices))
        while random.random() < 0.1:
            practices = [x for x in practices if x not in self.practices.all()]
            self.practices.add(random.choice(practices))
        for practice in self.practices.all():
            instruments.extend(practice.instruments.all())
        while self.instruments.count() < 7:
            instruments = [x for x in instruments if x not in self.instruments.all()]
            self.instruments.add(random.choice(instruments))

    def total_flaws(self):
        return sum([x.cost for x in self.merits_and_flaws.filter(cost__lt=0)])

    def random_backgrounds(self):
        while self.background_points > 0:
            backgrounds_with_multiplicity = []
            tmp_list = [
                [background] * (getattr(self, background) + 1)
                for background in self.backgrounds()
                if getattr(self, background) < 3
            ]
            for background in tmp_list:
                backgrounds_with_multiplicity.extend(background)
            background = random.choice(backgrounds_with_multiplicity)
            if self.freebie_cost(background) <= self.background_points:
                setattr(self, background, getattr(self, background) + 1)
                self.background_points -= self.freebie_cost(background)

    def freebie_cost(self, trait_name):
        if MeritFlaw.objects.filter(name=trait_name).exists():
            return MeritFlaw.objects.get(name=trait_name).cost
        trait_name = trait_name.lower().replace(" ", "_")
        if trait_name in self.attributes():
            return 5
        if trait_name in self.abilities():
            return 2
        if trait_name in self.backgrounds():
            if trait_name in ["enhancement", "sanctum", "totem"]:
                return 2
            return 1
        if trait_name in [x.lower() for x in self.spheres]:
            return 7
        if trait_name == "arete":
            return 4
        if trait_name == "willpower":
            return 1
        if trait_name == "quintessence":
            return 1
        return 0

    def random_freebies(self):
        spheres = [x.lower() for x in self.spheres]
        options = (
            self.attributes()
            + list(self.abilities().keys())
            + self.backgrounds()
            + spheres
            + ["arete", "willpower", "quintessence"]
            + [x.name for x in MeritFlaw.objects.all()]
        )
        while self.freebies > 0:
            filtered_options = [
                x
                for x in options
                if self.freebie_cost(x) <= self.freebies and x not in spheres
            ]
            if self.total_flaws() <= -7:
                filtered_options = [
                    x for x in filtered_options if self.freebie_cost(x) > 0
                ]
            filtered_options.extend(
                [
                    x
                    for x in spheres
                    if getattr(self, x) < self.arete and self.freebies > 6
                ]
            )
            option = random.choice(filtered_options)
            self.freebies -= self.freebie_cost(option)
            if option in self.attributes() + list(
                self.abilities().keys()
            ) + self.backgrounds() + spheres + ["arete", "willpower",]:
                setattr(self, option, getattr(self, option) + 1)
            elif option == "quintessence":
                self.quintessence += 4
            else:
                option = MeritFlaw.objects.get(name=option)
                self.merits_and_flaws.add(option)
        self.save()

    def xp_cost(self, trait_name):
        trait_name = trait_name.lower().replace(" ", "_")
        if trait_name in self.attributes():
            return getattr(self, trait_name) * 4
        if trait_name in self.abilities():
            if getattr(self, trait_name) == 0:
                return 3
            return getattr(self, trait_name) * 2
        if trait_name in [x.lower() for x in self.spheres]:
            rating = getattr(self, trait_name)
            if rating == 0:
                return 10
            if (
                trait_name
                == self.spheres[self.sphere_key.index(self.affinity_sphere)].lower()
            ):
                return rating * 7
            return rating * 8
        if trait_name == "arete":
            return getattr(self, trait_name) * 8
        if trait_name == "willpower":
            return getattr(self, trait_name)
        return 0

    def random(self):
        self.random_faction()
        self.random_nature()
        self.random_demeanor()
        self.random_attributes()
        self.random_abilities(13, 9, 5)
        self.random_backgrounds()
        self.random_focus()
        self.random_arete()
        self.random_spheres(6)
        self.quintessence = self.avatar
        self.random_freebies()
        self.save()

    def spend_xp(self, trait_name):
        trait_name = trait_name.lower().replace(" ", "_")
        if self.xp_cost(trait_name) <= self.xp:
            self.xp -= self.xp_cost(trait_name)
            setattr(self, trait_name, getattr(self, trait_name) + 1)
            if self.spent_xp == "":
                self.spent_xp = f"{trait_name} {getattr(self, trait_name)}"
            else:
                self.spent_xp += f", {trait_name} {getattr(self, trait_name)}"

    def has_mage_history(self):
        output = True
        output = output and self.awakening
        output = output and self.seekings
        output = output and self.quiets
        output = output and self.age_of_awakening
        output = output and self.avatar_description
        return output

    def consistency_check(self):
        consistent = True
        if self.affiliation is not None:
            if self.affiliation.name != "Technocratic Union" and (
                self.secret_weapons > 0 or self.requisitions > 0
            ):
                consistent = False
        if self.faction is not None:
            if self.faction.name != "Akashayana" and self.do != 0:
                consistent = False
            if self.faction.name == "Ahl-i-Batin" and self.entropy > 0:
                consistent = False
            if self.faction.parent != self.affiliation:
                consistent = False
        if self.subfaction is not None:
            if self.subfaction.parent != self.faction:
                consistent = False
        if self.do > 0:
            dhyana = self.awareness + self.enigmas + self.meditation
            jivahasta = self.esoterica + self.medicine + self.survival
            karma = self.art + self.crafts + self.etiquette
            prajna = self.academics + self.belief_systems + self.cosmology
            shastamarga = self.academics + self.crafts + self.melee
            sunyakaya = self.meditation + self.stealth + self.subterfuge
            tricanmarga = self.acrobatics + self.athletics + self.esoterica
            limbs = [
                dhyana,
                jivahasta,
                karma,
                prajna,
                shastamarga,
                sunyakaya,
                tricanmarga,
            ]
            limbs = [x for x in limbs if x >= 2]
            if self.do > len(limbs):
                consistent = False
        return consistent


class Practice(models.Model):
    """Class for Practices as part of Focus"""

    name = models.CharField(max_length=100)
    abilities = models.JSONField(default=list, null=True)
    instruments = models.ManyToManyField("Instrument")

    def __str__(self):
        return self.name


class Instrument(models.Model):
    """Class for Instruments as part of Focus"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Paradigm(models.Model):
    """Class for Paradigm as part of Focus"""

    name = models.CharField(max_length=100)
    practices = models.ManyToManyField("Practice")

    def __str__(self):
        return self.name


class MageFaction(models.Model):
    """Class for managing Mage Factions"""

    name = models.CharField(max_length=100)
    paradigms = models.ManyToManyField("Paradigm", blank=True)
    practices = models.ManyToManyField("Practice", blank=True)
    affinities = models.JSONField(null=True, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    materials = models.ManyToManyField(Material, blank=True)
    media = models.ManyToManyField(Medium, blank=True)
    founded = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Resonance(models.Model):
    """Class for managing Resonance"""

    name = models.CharField(max_length=100)
    correspondence = models.BooleanField(default=False)
    entropy = models.BooleanField(default=False)
    forces = models.BooleanField(default=False)
    life = models.BooleanField(default=False)
    matter = models.BooleanField(default=False)
    mind = models.BooleanField(default=False)
    prime = models.BooleanField(default=False)
    spirit = models.BooleanField(default=False)
    time = models.BooleanField(default=False)
    data = models.BooleanField(default=False)
    dimensional_science = models.BooleanField(default=False)
    primal_utility = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ResRating(models.Model):
    """Class for managing Resonance Ratings"""

    mage = models.ForeignKey("Mage", on_delete=models.CASCADE)
    resonance = models.ForeignKey("Resonance", on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


class Rote(models.Model):
    """Class for managing Rotes"""

    name = models.CharField(max_length=100)
    correspondence = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    spirit = models.IntegerField(default=0)
    entropy = models.IntegerField(default=0)
    prime = models.IntegerField(default=0)
    mind = models.IntegerField(default=0)
    matter = models.IntegerField(default=0)
    forces = models.IntegerField(default=0)
    life = models.IntegerField(default=0)


class Cabal(models.Model):
    """Class for managing Cabals"""

    name = models.CharField(max_length=100)
    members = models.ManyToManyField("Mage", blank=True)
    leader = models.ForeignKey(
        Mage, blank=True, related_name="leads", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name

    def random(self, number_of_members, new_characters=False):
        if not new_characters:
            if Mage.objects.count() < number_of_members:
                raise ValueError("Not enough characters to create a cabal")
            mages = list(Mage.objects.all().order_by("?"))[:number_of_members]
            self.members.set(mages)
            self.leader = self.members.order_by("?").first()
            self.save()
        else:
            for i in range(number_of_members):
                if WoDProfile.objects.filter(storyteller=True).count() != 0:
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
                mage = Mage.objects.create(
                    name=f"TempName {i}", cabal=self, player=user.wod_profile
                )
                mage.random()
                mage.save()
                self.members.add(mage)
                self.leader = self.members.order_by("?").first()
                self.save()
