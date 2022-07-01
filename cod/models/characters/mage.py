from django.db import models
from cod.models.characters.mortal import Mortal

# Create your models here.
class Path(models.Model):
    name = models.CharField(max_length=100)
    ruling_arcana = models.JSONField(default=list)
    inferior_arcanum = models.CharField(max_length=40, default="")

class Order(models.Model):
    name = models.CharField(max_length=100)
    rote_skills = models.JSONField(default=list)

class Legacy(models.Model):
    name = models.CharField(max_length=100)
    path = models.ForeignKey(Path, null=True, blank=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)

class Spell(models.Model):
    name = models.CharField(max_length=100)
    practice = models.CharField(max_length=40, choices=[
		("compelling", "Compelling"),
		("knowing", "Knowing"),
		("unveiling", "Unveiling"),
		("ruling", "Ruling"),
		("shielding", "Shielding"),
		("veiling", "Veiling"),
		("fraying", "Fraying"),
		("perfecting", "Perfecting"),
		("weaving", "Weaving"),
		("patterning", "Patterning"),
		("unraveling", "Unraveling"),
		("making", "Making"),
		("unmaking", "Unmaking"),
	])

class Rote(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=0)
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)

class Mage(Mortal):
    type = "mage"
    
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE)
    path = models.ForeignKey(Path, blank=True, null=True, on_delete=models.CASCADE)
    
    gnosis = models.IntegerField(default=0)

    death = models.IntegerField(default=0)
    
    rotes = models.ManyToManyField(Rote, blank=True)
    
    nimbus = models.TextField(default="")
    mana = models.IntegerField(default=0)
    
    def has_path(self):
        return self.path is not None
    
    def set_path(self, path):
        pass
    
    def random_path(self):
        pass
    
    def has_order(self):
        return self.order is not None
    
    def set_order(self, order):
        pass
    
    def random_order(self):
        pass
    
    def has_rote_skills(self):
        pass
    
    def set_rote_skills(self, rote_skills):
        pass
    
    def add_gnosis(self):
        pass
    
    def has_gnosis(self):
        return self.gnosis > 0
    
    def set_gnosis(self, gnosis):
        pass

    def filter_arcana(self, minimum=0, maximum=5):
        return []
    
    def get_arcana(self):
        pass
    
    def has_arcana(self):
        pass
    
    def total_arcana(self):
        pass
    
    def add_arcanum(self, arcanum):
        pass
    
    def random_arcanum(self):
        pass
    
    def random_arcana(self):
        pass
    
    def has_legacy(self):
        pass
    
    def random_legacy(self):
        pass
    
    def has_mana(self):
        pass
    
    def set_mana(self, mana):
        pass
    
    def has_rotes(self):
        pass
    
    def add_rote(self, rote):
        pass
    
    def total_rotes(self):
        pass
    
    def random_rote(self):
        pass

    def random_rotes(self):
        pass
    
    def has_nimbus(self):
        return self.nimbus != ""
    
    def set_nimbus(self, nimbus):
        self.numbus = nimbus
        return True
    
    def random_nimbus(self):
        pass
    
    @staticmethod
    def practice_level(practice):
        pass
