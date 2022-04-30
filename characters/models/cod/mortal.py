import random
from attr import attributes
from django.db import models
from ..character import Character

from characters.utils import weighted_choice

# Create your models here.
class Mortal(Character):
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
    # Add 1 die to rolls when relevant

    # merits: 7 dots

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
        sum(self.get_mental_skills().values())

    def physical_skill_sum(self):
        sum(self.get_physical_skills().values())

    def social_skill_sum(self):
        sum(self.get_social_skills().values())

    def random_creation(self):
        self.random_attributes()
        self.random_skills()
        self.random_specialties()
        self.random_merits()
        self.assign_advantages()

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
        while self.physical_skill_sum() < skill_types[0] + 3:
            skill_choice = weighted_choice(self.get_physical_skills())
            if getattr(self, skill_choice) <= 4:
                setattr(self, skill_choice, getattr(self, skill_choice) + 1)
        while self.social_skill_sum() < skill_types[1] + 3:
            skill_choice = weighted_choice(self.get_social_skills())
            if getattr(self, skill_choice) <= 4:
                setattr(self, skill_choice, getattr(self, skill_choice) + 1)
        while self.mental_skill_sum() < skill_types[2] + 3:
            skill_choice = weighted_choice(self.get_mental_skills())
            if getattr(self, skill_choice) <= 4:
                setattr(self, skill_choice, getattr(self, skill_choice) + 1)

    def random_specialties(self, num_specs=3):
        pass

    def random_merits(self, merit_dots=7):
        pass

    def assign_advantages(self):
        self.willpower = self.resolve + self.composure
        self.speed = self.strength + self.dexterity + 5
        self.health = self.size + self.stamina
        self.initiative_modifier = self.dexterity + self.composure
        self.defense = min([self.wits, self.dexterity]) + self.athletics


class Specialty(models.Model):
    ability_keys = [
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
    abilities = [
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

    ability = models.CharField(
        max_length=3, choices=zip(ability_keys, abilities), default="aca"
    )
    specialty = models.CharField(max_length=100)
