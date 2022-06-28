from time import time

from django.contrib.auth.models import User

player, _ = User.objects.get_or_create(username="Test")

from wod.models.characters.mage import Mage
from wod.models.characters.werewolf import Werewolf
from wod.models.items.mage import Grimoire
from wod.models.locations.mage import Node

mage_start = time()
for i in range(10):
    mage = Werewolf.objects.create(
        name=f"Werewolf {Werewolf.objects.count()}", player=player.wod_profile
    )
    mage.random()
    mage.save()
print("Average Random Werewolf Time:", (time() - mage_start) / 10, "original", "1.46")

mage_start = time()
for i in range(10):
    mage = Mage.objects.create(
        name=f"Mage {Mage.objects.count()}", player=player.wod_profile
    )
    mage.random()
    mage.save()
print("Average Random Mage Time:", (time() - mage_start) / 10, "original", "1.21")


node_start = time()
for i in range(10):
    node = Node.objects.create(name=f"Node {Node.objects.count()}")
    node.random(rank=(i % 5) + 1)
    node.save()
print("Average Random Node Time:", (time() - node_start) / 10, "original", "0.09")


grimoire_start = time()
for i in range(10):
    grimoire = Grimoire.objects.create(name=f"Grimoire {Grimoire.objects.count()}")
    grimoire.random(rank=(i % 5) + 1)
    grimoire.save()
print(
    "Average Random Grimoire Time:", (time() - grimoire_start) / 10, "original", "0.07"
)

from cod.models.characters.mortal import Mortal

mortal_start = time()
for i in range(10):
    mortal = Mortal.objects.create(
        name=f"Mortal {Mortal.objects.count()}", player=player.cod_profile
    )
    mortal.random()
    mortal.save()
print("Average CoD Mortal Time:", (time() - mortal_start) / 10, "original", "0.85")

from tc.models.characters.aberrant import Aberrant
from tc.models.characters.human import Human
from tc.models.characters.talent import Talent

human_start = time()
for i in range(10):
    human = Human.objects.create(
        name=f"Human {Human.objects.count()}", player=player.tc_profile
    )
    human.random(xp=0)
    human.save()
print("Average Random TC Human Time:", (time() - human_start) / 10, "original", "0.56")
talent_start = time()
for i in range(10):
    talent = Talent.objects.create(
        name=f"Talent {Talent.objects.count()}", player=player.tc_profile
    )
    talent.random(xp=50)
    talent.save()
print("Average Random Talent Time:", (time() - talent_start) / 10, "original", "2.64")
aberrant_start = time()
for i in range(10):
    aberrant = Aberrant.objects.create(
        name=f"Aberrant {Aberrant.objects.count()}", player=player.tc_profile
    )
    aberrant.random(xp=150)
    aberrant.save()
print(
    "Average Random Aberrant Time:", (time() - aberrant_start) / 10, "original", "3.43"
)
