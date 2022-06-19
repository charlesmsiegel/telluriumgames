from django.db import models
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

    rites = models.IntegerField(default=0)

    gnosis = models.IntegerField(default=0)
    rage = models.IntegerField(default=0)
    
    glory = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    honor = models.IntegerField(default=0)
    
    gifts = models.ManyToManyField(Gift, blank=True)
    rites_known = models.ManyToManyField(Rite, blank=True)
    
    def has_breed(self):
        pass
    
    def set_breed(self, breed):
        pass
    
    def random_breed(self):
        pass
    
    def has_auspice(self):
        pass
    
    def set_auspice(self, auspice):
        pass
    
    def random_auspice(self):
        pass
    
    def has_tribe(self):
        pass

    def set_tribe(self, tribe):
        pass
    
    def random_tribe(self):
        pass
    
    def has_camp(self):
        pass
    
    def set_camp(self, camp):
        pass
    
    def random_camp(self):
        pass
    
    def add_gift(self, gift):
        pass
    
    def filter_gifts(self):
        return []
    
    def has_gifts(self):
        pass
    
    def random_gift(self):
        pass
    
    def random_gifts(self):
        pass
    
    def add_rite(self, rite):
        pass
    
    def filter_rites(self):
        return []
    
    def has_rites(self):
        pass
    
    def random_rites(self):
        pass
    
    def set_glory(self, glory):
        pass
    
    def set_honor(self, honor):
        pass
    
    def set_wisdom(self, wisdom):
        pass
    
    def has_renown(self):
        pass
    
    def add_gnosis(self):
        pass
    
    def add_rage(self):
        pass
    
    def set_rank(self, rank):
        pass
    
    def increase_rank(self):
        pass

    def has_werewolf_history(self):
        pass

# Create your models here.
# # Talents
# Leadership
# Primal Urge

# # Skills
# Animal Ken
# Larceny
# Performance
# Survival

# # Knowledges
# Enigmas
# Law
# Occult
# Rituals
# Technology

# # Backgrounds
# Allies
# Ancestors
# Fate
# Fetish
# Kinfolk
# Pure Breed
# Resources
# Rites
# Spirit Heritage
# Totem

class Pack(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(Werewolf, blank=True)

    def random(self, num_chars, new_characters=False):
        pass
    
    def set_totem(self, totem):
        pass
    
    def has_totem(self):
        pass
    
    def random_totem(self):
        pass
    
    def total_totem(self):
        pass
