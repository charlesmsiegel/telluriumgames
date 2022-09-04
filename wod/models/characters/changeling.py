from django.db import models
from wod.models.characters.human import Human, Group
from core.models import Model

class Kith(Model):
    type = "kith"
    
class House(Model):
    type = "house"

class CtDLegacy(Model):
    type = "legacy"

class CtDHuman(Human):
    type = "ctd_human"

class Changeling(CtDHuman):
    type = "changeling"

# Create your models here.
# # Talents
# Kenning
# Leadership

# # Skills
# Animal Ken
# Larceny
# Performance
# Survival

# # Knowledges
# Enigmas
# Gremayre
# Law
# Politics
# Technology


# # Backgrounds
# Chimera
# Dreamers
# Holdings
# Remembrance
# Resources
# Retinue
# Title
# Treasure

class Motley(Group):
    type = "motley"
