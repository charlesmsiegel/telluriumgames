import random
from tokenize import Special

from attr import attributes

from accounts.models import CoDProfile
from core.utils import weighted_choice
from django.db import models
from django.shortcuts import reverse
from polymorphic.models import PolymorphicModel


# Create your models here.
class Mortal(PolymorphicModel):
    player = models.ForeignKey(
        CoDProfile, on_delete=models.CASCADE, related_name="characters"
    )
    name = models.CharField(max_length=100, unique=True)
    concept = models.CharField(max_length=300)
    status_keys = ["Un", "Sub", "App", "Ret", "Dec"]
    statuses = ["Unfinished", "Submitted", "Approved", "Retired", "Deceased"]
    status = models.CharField(
        max_length=3, choices=zip(status_keys, statuses), default="Un"
    )
    minor = models.BooleanField(default=False)

    type = "mortal"
    short_term_aspiration_1 = models.CharField(max_length=100, blank=True, null=True)
    short_term_aspiration_2 = models.CharField(max_length=100, blank=True, null=True)
    long_term_aspiration = models.CharField(max_length=100, blank=True, null=True)

    virtue = models.CharField(max_length=100, blank=True, null=True)
    # example virtues: competitive, generous, just, loyal
    vice = models.CharField(max_length=100, blank=True, null=True)
    # example vices: ambitious, arrogant, competitive, greedy

    # attributes: physical, social, and mental, 5/4/3
    intelligence = models.IntegerField(default=1)
    wits = models.IntegerField(default=1)
    resolve = models.IntegerField(default=1)

    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)

    presence = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    composure = models.IntegerField(default=1)

    # skills: physical, social, menta, start at zero, 11/7/4
    # Attribute -1 for physical or social at 0, -3 for mental
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

    # skill specialties: pick three specialties (no requirements other than "has skill"!!!)
    specialties = models.ManyToManyField("Specialty", blank=True)
    # Add 1 die to rolls when relevant

    # merits: 7 dots
    merits = models.ManyToManyField("Merit", through="MeritRating")

    willpower = models.IntegerField(default=1)
    integrity = models.IntegerField(default=7)
    size = models.IntegerField(default=5)
    speed = models.IntegerField(default=1)
    health = models.IntegerField(default=1)
    initiative_modifier = models.IntegerField(default=1)
    defense = models.IntegerField(default=1)

    # finishing touches

    # 5 breaking points:
    # What is the worst thing your character has ever done?
    # What is the worst thing your character can imagine himself doing?
    # What is the worst thing your character can imagine someone else doing?
    # What has your character forgotten?
    # What is the most traumatic thing that has ever happened to your character?

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cod:character", args=[str(self.id)])

    def has_name(self):
        if self.name != "":
            return True
        return False

    def has_concept(self):
        if self.concept != "":
            return True
        return False

    def random_basis(self):
        self.vice = "Vice"
        self.virtue = "Virtue"
        self.concept = "Concept"

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

    def physical_attribute_sum(self):
        return sum(self.get_physical_attributes().values())

    def mental_attribute_sum(self):
        return sum(self.get_mental_attributes().values())

    def social_attribute_sum(self):
        return sum(self.get_social_attributes().values())

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

    def mental_skill_sum(self):
        return sum(self.get_mental_skills().values())

    def physical_skill_sum(self):
        return sum(self.get_physical_skills().values())

    def social_skill_sum(self):
        return sum(self.get_social_skills().values())

    def random_creation(self):
        self.random_basis()
        self.random_attributes()
        self.random_skills()
        self.random_specialties()
        self.random_merits()
        self.assign_advantages()
        self.apply_merits()
        self.save()

    def random_attributes(self, primary=5, secondary=4, tertiary=3):
        attribute_types = [primary, secondary, tertiary]
        random.shuffle(attribute_types)
        while self.physical_attribute_sum() < attribute_types[0] + 3:
            attribute_choice = weighted_choice(self.get_physical_attributes())
            if getattr(self, attribute_choice) <= 4:
                setattr(self, attribute_choice, getattr(self, attribute_choice) + 1)
        while self.social_attribute_sum() < attribute_types[1] + 3:
            attribute_choice = weighted_choice(self.get_social_attributes())
            if getattr(self, attribute_choice) <= 4:
                setattr(self, attribute_choice, getattr(self, attribute_choice) + 1)
        while self.mental_attribute_sum() < attribute_types[2] + 3:
            attribute_choice = weighted_choice(self.get_mental_attributes())
            if getattr(self, attribute_choice) <= 4:
                setattr(self, attribute_choice, getattr(self, attribute_choice) + 1)

    def random_skills(self, primary=11, secondary=7, tertiary=4):
        skill_types = [primary, secondary, tertiary]
        random.shuffle(skill_types)
        while self.physical_skill_sum() < skill_types[0]:
            skill_choice = weighted_choice(self.get_physical_skills())
            if getattr(self, skill_choice) <= 4:
                setattr(self, skill_choice, getattr(self, skill_choice) + 1)
        while self.social_skill_sum() < skill_types[1]:
            skill_choice = weighted_choice(self.get_social_skills())
            if getattr(self, skill_choice) <= 4:
                setattr(self, skill_choice, getattr(self, skill_choice) + 1)
        while self.mental_skill_sum() < skill_types[2]:
            skill_choice = weighted_choice(self.get_mental_skills())
            if getattr(self, skill_choice) <= 4:
                setattr(self, skill_choice, getattr(self, skill_choice) + 1)

    def random_specialties(self, num_specs=3):
        all_skills = {}
        all_skills.update(self.get_physical_skills())
        all_skills.update(self.get_social_skills())
        all_skills.update(self.get_mental_skills())
        all_skills = {k: v - 1 for k, v in all_skills.items()}
        while self.specialties.count() < num_specs:
            skill_to_specialize = weighted_choice(all_skills)
            spec = (
                Specialty.objects.filter(skill=skill_to_specialize[:3])
                .order_by("?")
                .first()
            )
            if spec not in self.specialties.all():
                self.specialties.add(spec)

    def total_merits(self):
        merits = MeritRating.objects.filter(character=self)
        return sum([x.rating for x in merits])

    def random_merits(self, merit_dots=7):
        while self.total_merits() < merit_dots:
            all_merits = Merit.objects.all()
            merits_that_are_cheap_enough = [
                x
                for x in all_merits
                if len(
                    [
                        r
                        for r in x.allowed_ratings
                        if int(r) <= merit_dots - self.total_merits()
                    ]
                )
                != 0
            ]
            merits_not_possessed = [
                x
                for x in merits_that_are_cheap_enough
                if (x.name not in [x.name for x in self.merits.all()] or x.needs_detail)
            ]
            allowed_merits = [x for x in merits_not_possessed if x.check_prereqs(self)]
            if "Anonymity" in [x.name for x in self.merits.all()]:
                merits_not_possessed = [x for x in merits_not_possessed if x.name != "Fame"]
            if "Fame" in [x.name for x in self.merits.all()]:
                merits_not_possessed = [x for x in merits_not_possessed if x.name != "Anonymity"]
            chosen = random.choice(allowed_merits)
            rating = int(random.choice(
                [
                    x
                    for x in chosen.allowed_ratings
                    if x <= merit_dots - self.total_merits()
                ]
            ))
            if chosen.needs_detail:
                detail = chosen.choose_detail(self)
            else:
                detail = None
            MeritRating.objects.create(
                character=self, merit=chosen, rating=rating, detail=detail
            )

    def assign_advantages(self):
        self.willpower = self.resolve + self.composure
        self.speed = self.strength + self.dexterity + 5
        self.health = self.size + self.stamina
        self.initiative_modifier = self.dexterity + self.composure
        self.defense = min([self.wits, self.dexterity]) + self.athletics

    # TODO: Tone down bias towards 5 dots of Skills (in fact, make 4 and 5 less likely)
    # TODO: Tweak Professional Training to avoid scientists without science
    def apply_merits(self):
        for merit in MeritRating.objects.filter(character=self):
            if merit.merit.name == "Giant":
                self.size += 1
                self.health += 1
            if merit.merit.name == "Fast Reflexes":
                self.initiative_modifier += merit.rating
            if merit.merit.name == "Small-Framed":
                self.size -= 1
                self.health -= 1
            if merit.merit.name == "Fleet of Foot":
                self.speed += merit.rating
            if merit.merit.name == "Vice-Ridden":
                self.vice += ", Vice 2"
            if merit.merit.name == "Virtuous":
                self.virtue += ", Virtue 2"
            if merit.merit.name == "Defensive Combat (Brawl)":
                self.defense += self.brawl - self.athletics
            if merit.merit.name == "Defensive Combat (Weaponry)":
                self.defense += self.weaponry - self.athletics


class Specialty(models.Model):
    skill_keys = [
        "aca",
        "com",
        "cra",
        "inv",
        "med",
        "occ",
        "pol",
        "sci",
        "ath",
        "bra",
        "dri",
        "fir",
        "lar",
        "ste",
        "sur",
        "wea",
        "ani",
        "emp",
        "exp",
        "int",
        "per",
        "soc",
        "str",
        "sub",
    ]
    skill_name = [
        "academics",
        "computer",
        "crafts",
        "investigation",
        "medicine",
        "occult",
        "politics",
        "science",
        "athletics",
        "brawl",
        "drive",
        "firearms",
        "larceny",
        "stealth",
        "survival",
        "weaponry",
        "animal_ken",
        "empathy",
        "expression",
        "intimidation",
        "persuasion",
        "socialize",
        "streetwise",
        "subterfuge",
    ]

    skill = models.CharField(
        max_length=3, choices=zip(skill_keys, skill_name), default="aca"
    )
    specialty = models.CharField(max_length=100)
    
    def display_skill(self):
        return self.skill_name[self.skill_keys.index(self.skill)].replace("_", " ").title()


class Merit(models.Model):
    name = models.CharField(max_length=100)
    needs_detail = models.BooleanField(default=False)
    style = models.BooleanField(default=False)
    allowed_ratings = models.JSONField()
    attribute_and_skill_prereqs = models.JSONField(null=True)
    merit_prereqs = models.JSONField(null=True)
    list_of_details = models.JSONField(null=True)
    merit_type = models.CharField(max_length=100)

    def check_prereqs(self, character):
        if self.attribute_and_skill_prereqs is not None:
            for prereq in self.attribute_and_skill_prereqs:
                if prereq[1] == "specialty":
                    specs = character.specialties.all()
                    if prereq[0][:3] not in [x.skill for x in specs]:
                        return False
                elif prereq[0] == "specialty":
                    tmp = {}
                    tmp.update(character.get_physical_skills())
                    tmp.update(character.get_mental_skills())
                    tmp.update(character.get_social_skills())
                    high_enough_skills = [key for key, value in tmp.items() if value >= prereq[1]]
                    if len(high_enough_skills) == 0:
                        return False
                    specs = character.specialties.all()
                    if len([x.skill for x in specs if x.skill in [y[:3] for y in high_enough_skills]]) == 0:
                        return False
                else:
                    if prereq[0] == "skill":
                        tmp = {}
                        tmp.update(character.get_physical_skills())
                        tmp.update(character.get_mental_skills())
                        tmp.update(character.get_social_skills())
                        if sum([x >= prereq[1] for x in tmp.values()]) == 0:
                            return False
                    elif getattr(character, prereq[0]) < prereq[1]:
                        return False
        if self.merit_prereqs is not None:
            for prereq in self.merit_prereqs:
                if MeritRating.objects.filter(character=character, merit__name=prereq[0], rating__gte=prereq[1]).count() == 0:
                    return False
        return True
    
    def get_max_rating(self):
        return max(self.allowed_ratings)

    def choose_detail(self, character):
        already_used_details = [x.detail for x in MeritRating.objects.filter(merit=self, character=character)]
        if self.name == "Area of Expertise":
            possible_details = [x.specialty for x in character.specialties.all() if x.specialty not in already_used_details]
        elif self.name == "Interdisciplinary Specialty":
            possible_details = [x for x in character.specialties.all() if x.specialty not in already_used_details]
            possible_details = [x.specialty for x in possible_details if getattr(character, x.get_skill_display()) >= 3]
        elif self.name == "Investigative Aide":
            tmp = {}
            tmp.update(character.get_physical_skills())
            tmp.update(character.get_mental_skills())
            tmp.update(character.get_social_skills())
            possible_details = [key for key, value in tmp.items() if value >= 3]
        elif self.name == "Hobbyist Clique":
            tmp = {}
            tmp.update(character.get_physical_skills())
            tmp.update(character.get_mental_skills())
            tmp.update(character.get_social_skills())
            possible_details = [key for key, value in tmp.items() if value >= 2]
        elif self.name == "Hobbyist Clique":
            tmp = {}
            tmp.update(character.get_physical_skills())
            tmp.update(character.get_mental_skills())
            tmp.update(character.get_social_skills())
            possible_details = [key for key, value in tmp.items() if value >= 2]
        else:
            possible_details = self.list_of_details
        possible_details = [x for x in possible_details if x not in already_used_details]
        if len(possible_details) > 0:
            detail = random.choice(possible_details)
        elif self.name == "Mentor":
            mentor_list = random.choices(self.list_of_details, k=3)
            detail = ", ".join(mentor_list)
        else:
            detail = f"Detail {character.merits.count()}"
        return detail

class MeritRating(models.Model):
    character = models.ForeignKey("Mortal", null=False, blank=False, on_delete=models.CASCADE)
    merit = models.ForeignKey("Merit", null=False, blank=False, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    detail = models.CharField(max_length=100, null=True, blank=True)
