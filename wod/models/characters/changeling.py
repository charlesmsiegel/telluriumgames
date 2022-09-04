from django.db import models
from wod.models.characters.human import Human, Group
from core.models import Model

class Kith(Model):
    type = "kith"
    
    birthrights = models.JSONField(default=list)
    frailty = models.TextField(default="")
    
class House(Model):
    type = "house"
    
    court = models.CharField(max_length=20, choices=[
        ("seelile", "Seelie"), ('unseelie', "Unseelie")
    ], blank=True, null=True)
    boon = models.TextField(default="")
    flaw = models.TextField(default="")
    factions = models.JSONField(default=list)

class CtDLegacy(Model):
    type = "legacy"
    
    court = models.CharField(max_length=20, choices=[
        ("seelile", "Seelie"), ('unseelie', "Unseelie")
    ], blank=True, null=True)

class CtDHuman(Human):
    type = "ctd_human"
    
    kenning = models.IntegerField(default=0)
    leadership = models.IntegerField(default=0)
    
    animal_ken = models.IntegerField(default=0)
    larceny = models.IntegerField(default=0)
    performance = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    
    enigmas = models.IntegerField(default=0)
    gremayre = models.IntegerField(default=0)
    law = models.IntegerField(default=0)
    politics = models.IntegerField(default=0)
    technology = models.IntegerField(default=0)

    chimera = models.IntegerField(default=0)
    dreamers = models.IntegerField(default=0)
    holdings = models.IntegerField(default=0)
    remembrance = models.IntegerField(default=0)
    resources = models.IntegerField(default=0)
    retinue = models.IntegerField(default=0)
    title = models.IntegerField(default=0)
    treasure = models.IntegerField(default=0)

class Changeling(CtDHuman):
    type = "changeling"
    
    kith = models.ForeignKey(Kith, null=True, blank=True, on_delete=models.CASCADE)
    
    banality = models.IntegerField(default=3)
    glamour = models.IntegerField(default=4)
    
    def has_court(self):
        pass
    
    def set_court(self, court):
        pass
    
    def random_court(self):
        pass
    
    def has_seelie_legacy(self):
        pass
    
    def set_seelie_legacy(self, legacy):
        pass
    
    def random_seelie_legacy(self):
        pass
    
    def has_unseelie_legacy(self):
        pass
    
    def set_unseelie_legacy(self, legacy):
        pass
    
    def random_unseelie_legacy(self):
        pass
    
    def has_seeming(self):
        pass
    
    def set_seeming(self, seeming):
        pass
    
    def random_seeming(self):
        pass
    
    def add_art(self, art):
        pass
    
    def get_arts(self):
        pass
    
    def filter_arts(self, minimum=0, maximum=5):
        return []
    
    def has_arts(self):
        pass
    
    def total_arts(self):
        return 0
    
    def random_art(self):
        pass
    
    def random_arts(self):
        pass

    def add_realm(self, realm):
        pass
    
    def get_realms(self):
        pass
    
    def filter_realms(self, minimum=0, maximum=5):
        return []
    
    def has_realms(self):
        pass
    
    def total_realms(self):
        return 0
    
    def random_realm(self):
        pass
    
    def random_realms(self):
        pass
    
    def add_banality(self):
        pass
    
    def add_glamour(self):
        pass
    
    def has_musing_threshold(self):
        pass
    
    def set_musing_threshold(self, threshold):
        pass
    
    def random_musing_threshold(self):
        pass
    
    def has_ravaging_threshold(self):
        pass
    
    def set_ravaging_threshold(self, threshold):
        pass
    
    def random_ravaging_threshold(self):
        pass
    
    def set_antithesis(self, antithesis):
        pass
    
    def has_antithesis(self):
        pass
    
    def random_antithesis(self):
        pass
    
    def has_changeling_history(self):
        pass

    def has_changeling_appearance(self):
        pass



class Motley(Group):
    type = "motley"
