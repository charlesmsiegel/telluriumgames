from django.db.models import Q
from django.db import models
from cod.models.characters.mortal import Mortal
from core.utils import add_dot

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
    arcanum = models.CharField(max_length=10, choices=[
		("death", "Death"),
        ("matter", "Matter"),
        ("life", "Life"),
        ("spirit", "Spirit"),
        ("time", "Time"),
        ("fate", "Fate"),
        ("mind", "Mind"),
        ("space", "Space"),
        ("prime", "Prime"),
        ("forces", "Forces"),
	])
    level = models.IntegerField(default=0)

class Rote(models.Model):
    name = models.CharField(max_length=100)
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
    

class Mage(Mortal):
    type = "mage"
    
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE)
    path = models.ForeignKey(Path, blank=True, null=True, on_delete=models.CASCADE)
    legacy = models.ForeignKey(Legacy, blank=True, null=True, on_delete=models.CASCADE)
    
    rote_skills = models.JSONField(default=list)
    
    gnosis = models.IntegerField(default=0)

    death = models.IntegerField(default=0)
    matter = models.IntegerField(default=0)
    life = models.IntegerField(default=0)
    spirit = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    fate = models.IntegerField(default=0)
    mind = models.IntegerField(default=0)
    space = models.IntegerField(default=0)
    prime = models.IntegerField(default=0)
    forces = models.IntegerField(default=0)

    rotes = models.ManyToManyField(Rote, blank=True)
    
    nimbus = models.TextField(default="")
    mana = models.IntegerField(default=0)
    
    def has_path(self):
        return self.path is not None
    
    def set_path(self, path):
        self.path = path
        self.save()
        return True
    
    def random_path(self):
        path = Path.objects.order_by("?").first()
        return self.set_path(path)
    
    def has_order(self):
        return self.order is not None
    
    def set_order(self, order):
        self.order = order
        self.save()
        return True
    
    def random_order(self):
        order = Order.objects.order_by("?").first()
        return self.set_order(order)
    
    def has_rote_skills(self):
        return len(self.rote_skills) == 3
    
    def set_rote_skills(self, rote_skills):
        self.rote_skills = rote_skills
        return True
    
    def add_gnosis(self):
        return add_dot(self, "gnosis", maximum=10)
    
    def has_gnosis(self):
        return self.gnosis > 0
    
    def set_gnosis(self, gnosis):
        if gnosis < 1:
            gnosis = 1
        if gnosis > 10:
            gnosis = 10
        self.gnosis = gnosis
        self.save()
        return True

    def filter_arcana(self, minimum=0, maximum=5):
        return [k for k, v in self.get_arcana().items() if minimum <= v <= maximum]
    
    def get_arcana(self):
        return {
            "death": self.death,
            "matter": self.matter,
            "life": self.life,
            "spirit": self.spirit,
            "time": self.time,
            "fate": self.fate,
            "mind": self.mind,
            "space": self.space,
            "prime": self.prime,
            "forces": self.forces,
		}
    
    def has_arcana(self):
        nonzero_values = [x for x in self.get_arcana().values() if x != 0]
        nonzero_values.sort()
        if nonzero_values not in [[3, 2, 1], [3, 1, 1, 1], [2, 2, 2], [2, 2, 1, 1], [2, 1, 1, 1, 1]]:
            return False
        for ruling in self.path.ruling_arcana:
            if self.get_arcana()[ruling] == 0:
                return False
        if self.get_arcana()[self.path.inferior_arcanum] != 0:
            return False
        return True        
    
    def total_arcana(self):
        return sum(v for k, v in self.get_arcana().items())
    
    def add_arcanum(self, arcanum):
        return add_dot(self, arcanum, maximum=5)
    
    def random_arcanum(self):
        pass
    
    def random_arcana(self):
        pass
    
    def has_legacy(self):
        return self.legacy is not None
    
    def set_legacy(self, legacy):
        pass
    
    def random_legacy(self):
        pass
    
    def filter_legacies(self):
        return []
    
    def has_mana(self):
        return self.mana != 0
    
    def set_mana(self, mana):
        self.mana = mana
        self.save()
        return True
    
    def has_rotes(self):
        pass
    
    def add_rote(self, rote):
        if getattr(self, rote.spell.arcanum) >= rote.spell.level:
            self.rotes.add(rote)
            self.save()
            return True
        return False
    
    def total_rotes(self):
        return self.rotes.count()
    
    def random_rote(self):
        pass

    def random_rotes(self):
        pass
    
    def filter_rotes(self):
        arcana_dict = self.get_arcana()
        q = Q()
        for arcana, level in arcana_dict.items():
            q |= Q(spell__arcanum=arcana, spell__level__lte=level)
        allowed_rotes = Rote.objects.filter(q)
        return allowed_rotes.exclude(pk__in=self.rotes.all())
    
    def has_nimbus(self):
        return self.nimbus != ""
    
    def set_nimbus(self, nimbus):
        self.numbus = nimbus
        return True
    
    def random_nimbus(self):
        pass
    
    @staticmethod
    def practice_level(practice):
        if practice in ["compelling", "knowing", "unveiling"]:
            return 1
        if practice in ["ruling", "shielding", "veiling"]:
            return 2
        if practice in ["fraying", "perfecting", "weaving"]:
            return 3
        if practice in ["patterning", "unraveling"]:
            return 4
        if practice in ["making", "unmaking"]:
            return 5
        return 0

    @staticmethod
    def practices_at_level(level):
        if level == 1:
            return ["compelling", "knowing", "unveiling"]
        if level == 2:
            return ["ruling", "shielding", "veiling"]
        if level == 3:
            return ["fraying", "perfecting", "weaving"]
        if level == 4:
            return ["patterning", "unraveling"]
        if level == 5:
            return ["making", "unmaking"]
        return []
