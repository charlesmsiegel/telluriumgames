from django.db import models
from wod.models.characters.human import Human

class Werewolf(Human):
    type = "werewolf"

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
    pass

class Totem(models.Model):
    pass
